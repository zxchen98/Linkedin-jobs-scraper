from linkedin_scraper import JobSearch, actions,parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome()

email = input()
password = input()

actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
job_search = JobSearch(driver=driver, close_on_complete=False, scrape=False)
# job_search contains jobs from your logged in front page:
# - job_search.recommended_jobs
# - job_search.still_hiring
# - job_search.more_jobs

job_listings_sde = job_search.search("Python Developer") # returns the list of `Job` from the first page
# job_listings_ds = job_search.search("Data Scientist")


parse.main(job_listings_sde)
# job2df(job_listings_ds)