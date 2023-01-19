import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *

host = "https://demoqa.com/automation-practice-form"
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



except (Exception) as err:
    print(err)
    print('Python Exception: Test failed with above error')
except (NoSuchElementException, TimeoutException) as err:
    print("Selenium Exception: Test failed with above error")

finally:
    driver.quit()