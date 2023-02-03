from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

# created object for chromedriver that talks to Chrome Browser
# driver = webdriver.Firefox()
# driver = webdriver.Edge()
# driver = webdriver.Ie()
#chrome_options = Options()
#chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome()
print("Maximizing the browser")
driver.maximize_window()

driver.get("https://www.google.com/")
time.sleep(2)
#
def search_google(keyword):
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("selenium")
    # search_box.send_keys("selenium"+Keys.RETURN) this is another option for keyboard actions ENTER=RETURN
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)

search_google("selenium")

result = driver.find_element(By.ID, 'result-stats')
print(f"Search is done and result text is : {result.text}")

print("Closing browser after test")
driver.quit()

print("Test completed")