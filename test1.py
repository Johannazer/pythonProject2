from main import *
import pytest
import requests


class TestSelenium:

    def test(self):
        driver= open_site(url)
        customer_login(driver)
        user(driver)
        actual= int(balance(driver))
        deposit(driver)
        expected= int(balance(driver)) - 250
        assert actual== expected

    def test2(self):
        driver= open_site(url)
        Manager(driver)
        Customers(driver)
        actual= rows(driver)
        Delete_customers(driver)
        expected= rows(driver)
        assert actual != expected

    def test3(self):
        driver= open_site(url)
        Manager(driver)
        Customers(driver)
        actual= rows(driver)
        New_customers(driver)
        Customers(driver)
        expected= rows(driver)
        assert actual!= expected

class TestAPI:
    def test_Ignore(self):
        url= 'https://api.dictionaryapi.dev/api/v2/entries/en/ignore'
        response= requests.get(url)
        assert 400 > response.status_code >= 200

    def test_joy(self):
        url= 'https://api.dictionaryapi.dev/api/v2/entries/en/joy'
        response= requests.get(url)
        joy= response.json()
        actual= joy[1]['phonetic']
        expected= '/dʒɔɪ/'
        assert actual== expected


