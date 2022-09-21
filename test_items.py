from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time


def test_button_is_present(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)

    browser.implicitly_wait(5)


    add_to_cart_button = browser.find_elements(By.XPATH, '//button[@class="b3tn btn-lg btn-primary btn-add-to-basket"]')

    assert len(add_to_cart_button) == 1, f'{len(add_to_cart_button)} buttons found, expected: 1'
