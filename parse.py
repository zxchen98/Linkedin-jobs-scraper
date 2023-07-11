import pandas as pd
import numpy as np
from tqdm import tqdm

def job2df(job_listing):
    df = pd.DataFrame()
    job_cards = tqdm(job_listing)
    for i in job_cards:
        job_cards.set_description(f"Processing: {str(i)}")
        i.scrape(close_on_complete=False)

        job_df = pd.DataFrame([i.to_dict()])
        df = pd.concat([df,job_df],axis = 0)
    df.to_csv('jobs.csv')
    print("Begin Parsing....\n")
    return 