# Linkedin-jobs-scraper
This is a Python scraper for customized job listings on LinkedIn. It automatically logs in to your Linkedin account and searches for the jobs according to the keyword you provided. It then gathers all the useful info such as Company, location, posted time, and requirements, and uploads it into a google sheet. Check this to setup the connection [How to automate google sheets with python](https://www.geeksforgeeks.org/how-to-automate-google-sheets-with-python/#) before running.

I found it very useful in my daily job search and it is convenient to keep track of what I applied for future reference without typing it in manually. 

## Disclaimer
The Linkedin_scraper module is heavily borrowed from this [Github repo](https://github.com/joeyism/linkedin_scraper/tree/master) with some bug fixes and customizations, check it out if you want to scrape candidates' info or any other Linkedin features.

## Setup
```bash
pip install -r requirements.txt
```

##
Make sure you change the job-searching keywords inside the run.py (default is 'Python developer')
```bash
Python3 run.py
```


