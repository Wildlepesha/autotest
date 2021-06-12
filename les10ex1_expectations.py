from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from stepic_formula import calc
import time

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
    button = browser.find_element_by_id("book").click()

    value = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer").send_keys(calc(value))
    button_send = browser.find_element_by_id("solve").click()

finally:
    time.sleep(10)
    browser.quit()