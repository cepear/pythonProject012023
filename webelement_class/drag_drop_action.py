from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
import time

from selenium.webdriver.support.select import Select

#from utilities import *

HOST = "https://jqueryui.com/resources/demos/droppable/default.html"

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



    # All Locators (all values are ID locators):
    draggable_id = 'draggable'
    droppable_id = 'droppable'


  # Steps:
    driver.get(HOST)
    time.sleep(2)
    # disable_google_ads(driver)

    # Code for the drag and drop will be here
    # verify drop box text before dropping
    # drag and drop object into the box
    # verify drop box text after dropping



    time.sleep(2)
    print("Drag and drop Test completed successfully")

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