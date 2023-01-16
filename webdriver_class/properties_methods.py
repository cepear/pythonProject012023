import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

host = "https://demoqa.com/browser-windows"
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
print("Maximizing the browser")
driver.maximize_window()

try:
    print("-----Starting test with WebDriver properties------------")
    driver.get(host)
    time.sleep(2)

    print("This is my current URL: ", driver.current_url)
    print("My driver.name : ", driver.name)
    #print("Driver.orientation is:", driver.orientation)
    print("Driver.title: ", driver.title)
    print("Driver.current_window_handle:", driver.current_window_handle)
    print('Driver.window_handles:', driver.window_handles)
    time.sleep(3)
    print("-----WebDriver Methods -------------")
    next_page = "https://www.google.com/"
    driver.get(next_page)
    time.sleep(1)
    driver.back()
    print("We are here now:  'QA Tools' ", driver.current_url)
    time.sleep(1)
    driver.forward()
    print("We are here now: Google.com ", driver.current_url)
    time.sleep(1)
    driver.refresh()
    print("We are here now: Google.com ", driver.current_url)
except (Exception) as err:
    print(err)
    print('Python Exception: Test failed with above error')
except (NoSuchElementException, TimeoutException) as err:
    print("Selenium Exception: Test failed with above error")

finally:
    driver.quit()