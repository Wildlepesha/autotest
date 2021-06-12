from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/selects1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    select = Select(browser.find_element_by_id("dropdown"))

    def calc(x, y):
        x = int(x)
        y = int(y)
        return str(x + y)
    select.select_by_value(calc(x, y))
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()