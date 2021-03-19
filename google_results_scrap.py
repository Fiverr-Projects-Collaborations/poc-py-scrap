from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

import os

driver = None
response = ""
companies = []
sources = []
links = []


def scrap_source_for_company(company_name):
    driver.get('https://www.google.com')
    driver.find_element_by_name("q").send_keys(company_name + Keys.ENTER)
    sources.append(driver.page_source)
    time.sleep(3)
    for x in range(2, 3):
        driver.find_element_by_id('pnnext').click()
        sources.append(driver.page_source)
        time.sleep(3)


def scrap_urls_for_search():
    for source in sources:
        soup = BeautifulSoup(source, 'html.parser')
        for h in soup.find_all('div', {"class": "r"}):
            a = h.find('a')
            links.append(a.attrs['href'])


if __name__ == '__main__':
    try:
        # TODO implement
        print("Starting Scrapping")
        chrome_options = Options()
        # response = "BLANC RESPONSE1"
        # chrome_options.add_argument('--headless')
        # response = "BLANC RESPONSE2"
        # chrome_options.add_argument('--no-sandbox')
        # response = "BLANC RESPONSE3"
        # chrome_options.add_argument('--disable-gpu')
        # response = "BLANC RESPONSE4"
        # chrome_options.add_argument('--window-size=1280x1696')
        # response = "BLANC RESPONSE5"
        # chrome_options.add_argument('--user-data-dir=/tmp/user-data')
        # response = "BLANC RESPONSE6"
        # chrome_options.add_argument('--hide-scrollbars')
        # response = "BLANC RESPONSE7"
        # chrome_options.add_argument('--enable-logging')
        # response = "BLANC RESPONSE8"
        # chrome_options.add_argument('--log-level=0')
        # response = "BLANC RESPONSE9"
        # chrome_options.add_argument('--v=99')
        # response = "BLANC RESPONSE10"
        # chrome_options.add_argument('--single-process')
        # response = "BLANC RESPONSE11"
        # chrome_options.add_argument('--data-path=/tmp/data-path')
        # response = "BLANC RESPONSE12"
        # chrome_options.add_argument('--ignore-certificate-errors')
        # response = "BLANC RESPONSE13"
        # chrome_options.add_argument('--homedir=/tmp')
        # response = "BLANC RESPONSE14"
        # chrome_options.add_argument('--disk-cache-dir=/tmp/cache-dir')
        # response = "BLANC RESPONSE15"
        chrome_options.add_argument(
            'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')
        # response = "BLANC RESPONSE16"
        # chrome_options.binary_location = os.getcwd() + "/bin/headless-chromium"
        # response = "BLANC RESPONSE17"
        companies.append("AERO CLUB")
        companies.append("LALLUBHAI AMICHAND LIMITED")
        #browser version specific chromedriver
        driver = webdriver.Chrome('/Users/anirudhnegi/Downloads/lambda_function/bin/chromedriver',
                                  chrome_options=chrome_options)
        for company in companies:
            scrap_source_for_company(company)
        driver.close()

        scrap_urls_for_search()

        print(links)

    except Exception as e:
        print(str(e))
        print("EXCEPTION OCCURED!")
