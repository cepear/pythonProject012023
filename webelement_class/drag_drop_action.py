from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains

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
    # verify drop box text before dropping, expected: 'Drop here'
    drag_obj = driver.find_element(By.ID, draggable_id)
    drop_obj = driver.find_element(By.ID, droppable_id)
    print(f"Text in the droppable object is :", drop_obj)
    print(f"Text in the droppable object before is :  {drop_obj.text}")
    assert drop_obj.text == 'Drop here', "Drop box text verification before drop action is failed"

    # drag and drop object into the box
    actions = ActionChains(driver)
    actions.drag_and_drop(drag_obj, drop_obj).perform()
    #actions.click_and_hold(drag_obj).pause(2).release(drop_obj).perform()   ---alt way for the above code.
    # verify drop box text after dropping, expected: 'Dropped'
    #print(f"Text in the droppable object is :", drop_obj).
    print(f"Text in the droppable object after is : {drop_obj.text}")
    assert drop_obj.text == 'Dropped!', "Drop box text verification after drop action is failed"



    time.sleep(2)
    print("Drag and drop Test completed successfully")

except (FileNotFoundError, ZeroDivisionError)  as err:
    time.sleep(10)
    print("Python Exception: test failed with following exception.")
    print(err)
except Exception as err:
    time.sleep(10)
    print("Selenium Exception: test failed with following exception.")
    print(err)
finally:
    # close all tabs:
    driver.quit()
    print("TEST Completed!!")