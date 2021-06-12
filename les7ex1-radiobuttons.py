from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    answer = browser.find_element_by_id("answer")
    answer.send_keys(calc(x))
    check1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    check1.click()
    radio1 = browser.find_element_by_id("robotsRule")
    radio1.click()
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    time.sleep(10)
    browser.quit()