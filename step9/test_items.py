from selenium import webdriver
import time
import pytest

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_the_button(browser):
    browser.get(link)

    time.sleep(5)

    assert browser.find_element_by_class_name("btn"), "The button is founded!"

    time.sleep(30)
