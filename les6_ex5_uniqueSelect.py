from selenium import webdriver
import time


link = "http://suninjuly.github.io/registration1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_css_selector(".first_block .first_class .first")
    input1.send_keys("Имя")
    input2 = browser.find_element_by_css_selector(".first_block .second_class .second")
    input2.send_keys("Имя")
    input3 = browser.find_element_by_css_selector(".first_block .third_class .third")
    input3.send_keys("Имя")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()