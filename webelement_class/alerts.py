from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time

from selenium.webdriver.support.select import Select

#from utilities import *

HOST = "https://demoqa.com/alerts"

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
# chr_options.add_experimental_option('excludeSwitches',["disable-popup-blocking"])
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()
# This sets a sticky timeout to implicitly wait for an element to be found, or a command to complete.
driver.implicitly_wait(20)
time.sleep(0)

try:
    # Input DATA:
    alert_input = 'United States'


    # All Locators (all values are ID locators):
    alert_notify = 'alertButton'
    alert_confirm = 'confirmButton'
    confirm_result1 = 'confirmResult'
    alert_prompt = 'promtButton'
    prompt_result = 'promptResult'

  # Steps:
    driver.get(HOST)
    time.sleep(5)

    print("Scenario 1: click alert1 button, click OK button to close alert")
    driver.find_element(By.ID, alert_notify).click()
    alert = driver.switch_to.alert
    print(f"Text on the alert : , '{alert.text}'")
    alert.accept()
    print("-----------------------------")
    time.sleep(5)

    # click alert 2 button, confirm the alert, verify OK button clicked in result text.
    print("Scenario 2: click alert2 button, click OK button to close alert")
    driver.find_element(By.ID, alert_confirm).click()
    alert = driver.switch_to.alert
    print(f"Text on the alert : , '{alert.text}'")
    alert.accept()
    result_msg = driver.find_element(By.ID, confirm_result1).text
    print(f"Result message: {result_msg}")
    print("------------------------------")
    time.sleep(5)

    # click alert 2 button, dismiss the alert, verify Cancel button is clicked in result text.
    print("Scenario 3: click alert2 button, click Cancel button to close alert")
    driver.find_element(By.ID, alert_confirm).click()
    alert = driver.switch_to.alert
    print(f"Text on the alert : , '{alert.text}'")
    alert.dismiss()
    result_msg = driver.find_element(By.ID, confirm_result1).text
    print(f"Result message: {result_msg}")
    print("------------------------------")
    time.sleep(5)

    # click alert 3 button, enter alert_input, click OK, verify alert_input message in result text.
    print("Scenario 4: click alert3 button, click OK button to close alert")
    driver.find_element(By.ID, alert_prompt).click()
    alert = driver.switch_to.alert
    print(f"Text on the alert : , '{alert.text}'")
    alert.send_keys(alert_input)
    alert.accept()
    result_msg = driver.find_element(By.ID, prompt_result).text
    print(f"Result message: {result_msg}")
    print("------------------------------")
    time.sleep(5)

    # click alert 3 button, dismiss alert_input, click OK, verify no result message.
    print("Scenario 5: click alert3 button, click Cancel button to close alert")
    driver.find_element(By.ID, alert_prompt).click()
    alert = driver.switch_to.alert
    #print(f"Text on the alert : , '{alert.text}'")
    alert.dismiss()
    #result_msg = driver.find_element(By.ID, prompt_result).text
    #print(f"Result message: {result_msg}")
    print("------------------------------")
    time.sleep(5)



    time.sleep(2)
    print("Dropdown Test completed successfully")

except Exception as err:
    time.sleep(10)
    print("Python Exception: test failed with following exception.")
    print(err)
except (NoSuchElementException, TimeoutException) as err:
    time.sleep(10)
    print("Selenium Exception: test failed with following exception.")
    print(err)
finally:
    # close all tabs:
    driver.quit()
    print("TEST Completed!!")