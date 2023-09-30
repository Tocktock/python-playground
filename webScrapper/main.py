from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)
browser.get("https://www.indeed.com/jobs?q=python&l=Remote&start=10")

