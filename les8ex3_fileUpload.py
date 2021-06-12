from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os


link = "http://suninjuly.github.io/file_input.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)
    input1 = browser.find_element_by_css_selector("input[name='firstname']").send_keys('MyName')
    input2 = browser.find_element_by_css_selector("input[name='lastname']").send_keys('MyLastName')
    input3 = browser.find_element_by_css_selector("input[name='email']").send_keys('MyEmail')
    input4 = browser.find_element_by_css_selector("input[name='file']").send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(10)
    browser.quit()