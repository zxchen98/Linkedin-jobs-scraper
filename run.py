from linkedin_scraper import JobSearch, actions
from selenium import webdriver
import pandas as pd
import numpy as np

driver = webdriver.Chrome()

email = "xiz643@ucsd.edu"
password = "980521Zxc!"

actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
job_search = JobSearch(driver=driver, close_on_complete=False, scrape=False)
# job_search contains jobs from your logged in front page:
# - job_search.recommended_jobs
# - job_search.still_hiring
# - job_search.more_jobs

job_listings = job_search.search("Python developer") # returns the list of `Job` from the first page

each = job_listings[0]
each.scrape()
print(each.job_description)