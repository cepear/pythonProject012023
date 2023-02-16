
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

host = 'https://www.walmart.com'
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
time.sleep(3)
print("Maximizing the browser")
driver.maximize_window()
driver.implicitly_wait(20)


try:

    #Elements:
    driver.find_element(By.PARTIAL_LINK_TEXT, 'flex items-center no-underline ph3 white desktop-header-t').click()



except (Exception) as err:
    print(err)
    print('Python Exception: Test failed with above error')
except (NoSuchElementException, TimeoutException) as err:
    print("Selenium Exception: Test failed with above error")

finally:
    driver.quit()