from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)
browser.get("https://www.indeed.com/jobs?q=python&l=Remote&start=10")

soup = BeautifulSoup(browser.page_source, "html.parser")
print(soup.text)
job_list = soup.find("ul", class_="eu4oa1w0")

jobs = job_list.find_all('li', recursive=False)

for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:
        print("job li")
    else:
        print("mosaic li")
