from selenium import webdriver
import time


link = "https://дарицветы.москва/"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)
    browser.set_window_size("1980", "1020")

    input1 = browser.find_element_by_css_selector("#rec105349634 > div > div:nth-child(1) > div:nth-child(1) > a")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    input1.click()
    print("woke up")
    button = browser.find_element_by_css_selector(".t-item:nth-child(1)")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    order = browser.find_element_by_xpath("//td[text()='Заказать!']").click()
    input2 = browser.find_element_by_css_selector("#form161969074 > div.t-form__inputsbox > div.t-input-group.t-input-group_nm > div.t-input-block > input")
    input2.send_keys("Александр")
    input3 = browser.find_element_by_css_selector("#form161969074 > div.t-form__inputsbox > div.t-input-group.t-input-group_em > div.t-input-block > input")
    input3.send_keys("Test@test.com")
    input4 = browser.find_element_by_css_selector("[name='tildaspec-phone-part[]']")
    input4.send_keys("9060844425")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input4)
    input5 = browser.find_element_by_css_selector("#form161969074 > div.t-form__inputsbox > div.t-input-group.t-input-group_dl > div.t-input-block > div.t-radio__wrapper.t-radio__wrapper-delivery > label:nth-child(5)")
    input5.click()
    input6 = browser.find_element_by_css_selector("#form161969074 > div.t-form__inputsbox > div.t-input-group.t-input-group_da > div.t-input-block.t-input-block_inited-date-picker > div.t-datepicker__wrapper > input").click()
    input7 = browser.find_element_by_css_selector("#form161969074 > div.t-form__inputsbox > div.t-input-group.t-input-group_da > div.t-input-block.t-input-block_inited-date-picker > div.date-picker > table > tbody > tr:nth-child(2) > td.current-month.week-end.selected-day").click()

finally:
    time.sleep(10)
    browser.quit()
