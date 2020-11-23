import time

import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

from src import secrets

base_url = "https://www.depop.com/"
username = secrets.username


def bump():
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # login(driver)

    # time.sleep(2)  # Need to wait or else you are logged back out.
    driver.get(base_url + username)
    time.sleep(2)

    products = []
    i = 1
    while i < 100:
        try:
            print(driver.find_element_by_xpath(f'//*[@id="products-tab"]/div/ul/li[{i}]/a/div/img'))
            products.append(driver.find_element_by_xpath(f'//*[@id="products-tab"]/div/ul/li[{i}]/a/div/img'))
            i += 1
        except NoSuchElementException:
            break




    print(products)


def login(driver):
    driver.get(base_url + "login")
    driver.find_element_by_xpath('//*[@id="username"]') \
        .send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]') \
        .send_keys(secrets.password)
    driver.find_element_by_xpath('//*[@id="main"]/div[1]/form/button') \
        .click()


if __name__ == '__main__':
    bump()
