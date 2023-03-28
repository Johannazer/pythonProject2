from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import requests

import time
# -----------Selector-----------

url= 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login'
customer_login_selector= 'body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(1) > button'
user_selector= '#userSelect'
login_selector= 'body > div > div > div.ng-scope > div > form > button'
deposit_selector= 'body > div > div > div.ng-scope > div > div:nth-child(5) > button:nth-child(2)'
amount_selector= 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > div > input'
deposit_button_selector= 'body > div > div > div.ng-scope > div > div.container-fluid.mainBox.ng-scope > div > form > button:nth-child(2)'
text='Albus Dumbledore'
amount_number='250'
balance_selector= 'body > div > div > div.ng-scope > div > div:nth-child(3) > strong:nth-child(2)'
customers_selector='body > div > div > div.ng-scope > div > div.center > button:nth-child(3)'
Delete_Hermione_selector= 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > button'
number_rows_selector= 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody'
first_name_selector= 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input'
last_name_selector= 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input'
post_code_selector='body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input'
add_customer_button_selector= 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button'
Add_customer_selector= 'body > div > div > div.ng-scope > div > div.center > button:nth-child(1)'
new_number_rows_selector= 'body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(1) > td:nth-child(1)'
manager_selector ='body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button'

# ----------Fonction----------

def open_site(url):
    driver =webdriver.Chrome()
    driver.get(url)
    time.sleep(4)
    return driver

def customer_login(driver):
    customer_login = driver.find_element(By.CSS_SELECTOR, customer_login_selector)
    customer_login.click()
    time.sleep(3)
    return customer_login

def user(driver):
    user = driver.find_element(By.CSS_SELECTOR, user_selector)
    user.click()
    time.sleep(3)
    sel = Select(driver.find_element(By.CSS_SELECTOR, user_selector))
    sel.select_by_visible_text(text)
    time.sleep(3)
    login = driver.find_element(By.CSS_SELECTOR, login_selector)
    login.click()
    time.sleep(3)
    return user

def balance(driver):
    balance= driver.find_element(By.CSS_SELECTOR, balance_selector).text
    print(balance)
    return balance


def deposit(driver):
    deposit = driver.find_element(By.CSS_SELECTOR, deposit_selector)
    deposit.click()
    time.sleep(4)
    amount = driver.find_element(By.CSS_SELECTOR, amount_selector)
    amount.send_keys(amount_number)
    time.sleep(4)
    deposit_button = driver.find_element(By.CSS_SELECTOR, deposit_button_selector)
    deposit_button.click()
    time.sleep(5)
    return deposit

def Manager(driver):
    Manager= driver.find_element(By.CSS_SELECTOR,manager_selector)
    Manager.click()
    time.sleep(3)
    return Manager

def Customers(driver):
    Customers= driver.find_element(By.CSS_SELECTOR,customers_selector)
    Customers.click()
    time.sleep(3)
    return Customers

def Delete_customers(driver):
    Delete_hermione= driver.find_element(By.CSS_SELECTOR,Delete_Hermione_selector)
    Delete_hermione.click()
    time.sleep(3)
    return Delete_customers
def rows(driver):
    number_rows =driver.find_element(By.CSS_SELECTOR, number_rows_selector).text
    print(len(number_rows))
    time.sleep(3)
    return len(number_rows)

def New_customers(driver):
    Add_customer= driver.find_element(By.CSS_SELECTOR, Add_customer_selector)
    Add_customer.click()
    time.sleep(3)
    Firstname= driver.find_element(By.CSS_SELECTOR, first_name_selector)
    Firstname.send_keys('Severus')
    time.sleep(2)
    Lastname= driver.find_element(By.CSS_SELECTOR, last_name_selector)
    Lastname.send_keys('Snape')
    time.sleep(2)
    Postcode= driver.find_element(By.CSS_SELECTOR, post_code_selector)
    Postcode.send_keys('3344')
    time.sleep(2)
    Add_customer_button= driver.find_element(By.CSS_SELECTOR, add_customer_button_selector)
    Add_customer_button.click()
    time.sleep(2)
    driver.switch_to.alert.accept()
    time.sleep(2)
    return New_customers



# ---test1---
# driver = open_site(url)
# customer_login(driver)
# user(driver)
# balance(driver)
# deposit(driver,amount_number)

# # ---test2---כנס למערכת בהרשאות מנהל לחץ על כפתור משתמשים מחק אחד היוזרים לטעמך
# # כתוב טסט שבודק שהפעולה אכן בוצעה
# driver =open_site(url)
# time.sleep(3)
# Manager(driver)
# Customers(driver)
# rows(driver)
# Delete_customers(driver)
# rows(driver)

 # ---test3--- # כנס למערכת בתור מנהל תעשה הוספה ללקוח חדש, תחזור למסך של המנהל ותבדוק שהלקוח שהכנסת אכן
# # # נמצא
# driver= open_site(url)
# Manager(driver)
# Customers(driver)
# rows(driver)
# Customers(driver)
# time.sleep(2)
# rows(driver)
#

