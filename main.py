from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time

url='https://www.globalsqa.com/angularJs-protractor/BankingProject/#/'
customer_login_selector= 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button'
user_selector= '#userSelect'
login_selector= 'body > div > div > div.ng-scope > div > form > button'
deposit_selector= 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)'
amount_selector= 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input'
deposit_button_selector= 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button:nth-child(2)'

def open_site(url):
    driver=webdriver.Chrome()
    driver.get(url)
    return driver

def customer_login(driver):
    customer_login = driver.find_element(By.CSS_SELECTOR, customer_login_selector)
    customer_login.click()
    return customer_login

def user(driver, text):
    user = driver.find_element(By.CSS_SELECTOR, user_selector)
    user.click()
    sel = Select(driver.find_element(By.CSS_SELECTOR, user_selector))
    sel.select_by_visible_text(text)
    login = driver.find_element(By.CSS_SELECTOR, login_selector)
    login.click()
    time.sleep(5)
    return user


def deposit(driver, amount_number):
    deposit = driver.find_element(By.CSS_SELECTOR, deposit_selector)
    deposit.click()
    amount = driver.find_element(By.CSS_SELECTOR, amount_selector)
    amount.send_keys(amount_number)
    deposit_button = driver.find_element(By.CSS_SELECTOR, deposit_button_selector)
    deposit_button.click()
    time.sleep(5)
    return deposit





