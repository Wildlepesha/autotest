from selenium import webdriver
import math
import time
import os

link = "http://suninjuly.github.io/alert_accept.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    # Принять алерт
    # alert = browser.switch_to.alert
    # alert.accept()

    # Получить текст алерта
    # alert = browser.switch_to.alert
    # alert_text = alert.text

    # Принять или отменить конфирм
    # confirm = browser.switch_to.alert
    # confirm.accept() or confirm.dismiss()

    # Заполнить промпт
    # prompt = browser.switch_to.alert
    # prompt.send_keys("My answer")
    # prompt.accept()
    button = browser.find_element_by_css_selector("button.btn").click()
    time.sleep(1)
    confirm = browser.switch_to_alert().accept()
    time.sleep(1)
    value = browser.find_element_by_id("input_value").text
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    answer = browser.find_element_by_id("answer").send_keys(calc(value))
    button_send = browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(10)
    browser.quit()