from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


link = "http://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    input1 = browser.find_element_by_id("answer")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    input1.send_keys(calc(x))
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    checkbox = browser.find_element_by_id("robotCheckbox").click()
    radio = browser.find_element_by_id("robotsRule").click()
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()