# This is shared fixture between modules
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


@pytest.fixture(scope='module')
def driver():
    print("\n--------Set Up!")
    print('Initializing a webdriver for a browser...!')
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
    yield driver
    print("\n---------Tear Down! ")
    print("Close all tabs!")
    driver.quit()
    print("TEST Completed!!")
    print("Fixture steps are completed!")