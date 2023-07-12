import pandas as pd
import numpy as np
from tqdm import tqdm

import pygsheets
from datetime import date
import re

def job2df(job_listing):
    df = pd.DataFrame()
    job_cards = tqdm(job_listing)
    for i in job_cards:
        job_cards.set_description(f"Processing: {str(i)}")
        i.scrape(close_on_complete=False)

        job_df = pd.DataFrame([i.to_dict()])
        df = pd.concat([df,job_df],axis = 0)
    i.driver.close()
    print("Parsing Jobs....\n")
    return df

#!/usr/bin/env python
# coding: utf-8

'''
simple helper function used to search for jobs requirements, will be rewriten in later version
'''
def find_requirements(string):
    if string:
        start = re.search("([rR]equire)|([Qq]ualifications)",string)
        start = start.start() if start else 0
        end = re.search("[bB]enefits",string)
        end  = end.start() if end else len(string)
        requirements_ls = string[start:end].split('\n')
        for i in requirements_ls:
            if len(i)<=5:
                requirements_ls.remove(i)
        return '$'.join(requirements_ls[1:])
    return ''


# In[49]:

'''
helper funtion used to sort the posted dates
'''
def calculate_date(string):
    for i in range(len(string)):
        res = int(string[i].split(' ')[0])
        unit = string[i].split(' ')[1]
        if unit == 'minutes' or unit =='minute':
            string[i] = res
        elif unit == 'hours' or unit =='hour':
            string[i] = res*60
        elif unit == 'days'or unit =='day':
            string[i] = res*60*24
        elif unit == 'weeks' or unit =='week':
            string[i] = res*60*24*7
        elif unit == 'months' or unit =='month':
            string[i] = res*60*24*30
        else:
            string[i] = res
    return string


# In[79]:


def parse_df(jobs):
    jobs.drop(index=jobs.loc[jobs['already_applied'].isna()==False].index,inplace = True)
    # jobs.drop(index=jobs.loc[jobs['easy_apply'].isna()==False].index,inplace = True)
    jobs.drop(columns=['already_applied','applicant_count'],inplace = True)
    
    #split columns
    jobs['location'] = jobs['company'].apply(lambda x:x.split('·')[1])
    try:
        jobs['applicants'] = jobs['company'].apply(lambda x:int(x.split('·')[2][:-10].replace(',','')))
    except:
        jobs['applicants'] = 0
    jobs['company'] = jobs['company'].apply(lambda x:x.split('·')[0])
    pattern = r"[0-9]+"
    jobs['posted_date'] = jobs['location'].apply(lambda x: x[re.search(pattern,x).start():])
    jobs['location'] = jobs['location'].apply(lambda x: x[:re.search(pattern,x).start()])
    
    jobs['requirements']=jobs['job_description'].apply(find_requirements)
    jobs.drop(columns=['job_description'],inplace=True)
    jobs.sort_values(by = 'posted_date', key = calculate_date, inplace=True)
    jobs = jobs[['job_title','linkedin_url','company','company_linkedin_url','location','posted_date','easy_apply','applicants','requirements','benefits']]
    return jobs


# In[80]:

'''
    The following function upload the parsed jobs dataframe into a online goodle sheets
    Please enable google sheets API, google drive API and create your own credentials
    put your key.json path inside path
'''
def upload_df(jobs, title, path):
# Update the google spreadsheet
    print("Uploading jobs...")
    gc=pygsheets.authorize(service_account_file=path)
    sh = gc.open(title)
    try:
        sh.add_worksheet(f"{str(date.today())}")
        current_sheet = sh.worksheets()[-1]
    except:
        current_sheet=sh.worksheet_by_title(f"{str(date.today())}")
        current_sheet.clear()

    current_sheet.set_dataframe(jobs,(1,1))
    res = []
    for i in range(2,len(jobs)+2):
        command = "=SUBSTITUTE(" + f"I{i}" + ',"$"'+",CHAR(10))"
        res.append([command])
    current_sheet.update_value("K1", "requirements_listed")
    current_sheet.update_values(f"K2:K{len(jobs)+2}",res,parse = True)
    return


# In[81]:


def main(job_listings,title,key_path):
    jobs = job2df(job_listings)
    job_df = parse_df(jobs)
    upload_df(job_df,title,key_path)



