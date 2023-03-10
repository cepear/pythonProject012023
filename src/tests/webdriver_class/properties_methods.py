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
driver.implicitly_wait(20)

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
    time.sleep(3)
    print("--------Switching between browser windows (or tab)-----------")
    # we are on  /browser-window page, get current window handle
    driver.get(host)
    first_window_handle = driver.current_window_handle
    time.sleep(1)
    print(" ID of the page opened: ", first_window_handle)
    # click on the new tab button, this opens new tab
    driver.find_element(By.ID, 'tabButton').click()
    time.sleep(1)
    # now we have 2 tabs, get window handles (list), tabs are in order handles=[id_of_first_tab, id_of_second_tab]
    handles = driver.window_handles
    print("Number of handles found is: ", len(handles))
    print(" IDs of all tabs:", handles)
    print("Current browser window ID :", driver.current_window_handle)
    # switch to the second tab, switch to handles[1] or handle[-1]
    print("--------------Here I am switching to new window---------")
    driver.switch_to.window(handles[1])
    print('Getting text of new page :', driver.find_element(By.ID, 'sampleHeading').text)
    time.sleep(2)
    print("Current URL :", driver.current_url)
    time.sleep(2)
    driver.switch_to.window(handles[0])
    print("Switched to first window")
    time.sleep(1)
    print("Current URL :", driver.current_url)
    driver.find_element(By.ID, 'windowButton').click()
    new_window = driver.find_element(By.ID, 'sampleHeading').text
    print("Text of new  window is:", new_window)



except (Exception) as err:
    print(err)
    print('Python Exception: Test failed with above error')
except (NoSuchElementException, TimeoutException) as err:
    print("Selenium Exception: Test failed with above error")

finally:
    driver.quit()