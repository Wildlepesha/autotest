from selenium import webdriver
import math
import time
import os
from stepic_formula import calc

link = "http://suninjuly.github.io/redirect_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element_by_css_selector("button.btn").click()
    time.sleep(1)
    new_page = browser.window_handles[1]
    browser.switch_to_window(new_page)
    time.sleep(1)
    value = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer").send_keys(calc(value))
    button_send = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()