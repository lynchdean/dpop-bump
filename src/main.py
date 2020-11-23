import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from src import secrets

base_url = "https://www.depop.com/"


def bump():

    driver = webdriver.Chrome(ChromeDriverManager().install())

    login(driver)

    time.sleep(2)
    driver.get(base_url + secrets.username)
    # time.sleep(2000)


def login(driver):
    driver.get(base_url + "login")
    driver.find_element_by_xpath('//*[@id="username"]')\
        .send_keys(secrets.username)
    driver.find_element_by_xpath('//*[@id="password"]')\
        .send_keys(secrets.password)
    driver.find_element_by_xpath('//*[@id="main"]/div[1]/form/button')\
        .click()


if __name__ == '__main__':
    bump()
