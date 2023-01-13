from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

host = "https://demoqa.com/text-box"
chrome_options = Options()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

print("Maximizing the browser")
driver.maximize_window()

driver.get(host)
time.sleep(2)
