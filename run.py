from linkedin_scraper import JobSearch, actions,parse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--log-level=3')

email = input("please enter your email: ")
password = input("please enter your password:   ")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome()

print("Please follow the pop-up window\n")
actions.login(driver, email, password) # if email and password isnt given, it'll prompt in terminal
job_search = JobSearch(driver=driver, close_on_complete=False, scrape=False)

'''
    TODO: 1.Create your own job_search list, the default ones are python SDE and data Scientist
    2. replace the second argument to be the title of your google spreadsheets
    3. replace the third argument to be the path to your key.json, which is used to access the spreadsheet
'''
job_listings_sde = job_search.search("Python Developer")
# job_listings_ds = job_search.search("Data Scientist")
job_listings_ds = []

parse.main(job_listings_sde+job_listings_ds,'daily_linkedin_jobs','C:/Users/Muggl/Desktop/linkedin-jobs-392523-00de46c464a4.json')
print("SUCCESS! job list ready to view")