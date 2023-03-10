from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time

from selenium.webdriver.support.select import Select

#from utilities import *

HOST = "https://www.globalsqa.com/demo-site/select-dropdown-menu/"

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
    country1 = 'United States'


    # All Locators (all values are ID locators):
    country_dd_tag = 'select'

  # Steps:
    driver.get(HOST)
    time.sleep(5)
    # disable_google_ads(driver)


    # Code for the dropdown here

    drop_down_elem = driver.find_element(By.TAG_NAME, country_dd_tag)
    country_selection = Select(drop_down_elem)

    print("check first selected option")
    print('First selected option: ', country_selection.first_selected_option.text)
    # select US from dropdown
    print("Selecting by index 2")
    country_selection.select_by_index(2)
    print("Selected country:", country_selection.all_selected_options[0].text)
    print("Selecting by value 'FRA'")
    country_selection.select_by_value('FRA')
    print("Selected country:", country_selection.all_selected_options[0].text)
    print("Selecting by visible text 'United States")
    country_selection.select_by_visible_text('United States')
    print("# verify US is selected: get_all_selected option")
    print("Selected country:", country_selection.all_selected_options[0].text)






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

