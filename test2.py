from main import *
import pytest

class Testselemum:
    kk

    def test1(self):
    driver = open_site(url)
    customer_login(driver)
    user(driver)
    actual = int(balance(driver))
    deposit(driver)
    expected = int(balance(driver)) - 250
    assert actual == expected

    def test(self):
        driver= open_site(url)
        Manager(driver)
        Customers(driver)
        actual= rows(driver)
        Delete_customers(driver)
        expected= new_rows(driver) + 3
        assert actual==expected

        # driver = open_site(url)
        # Manager(driver)
        # Customers(driver)
        # actual = rows(driver)
        # Delete_customers(driver)
        # expected = new_rows(driver) + 3
        # assert actual =expected

