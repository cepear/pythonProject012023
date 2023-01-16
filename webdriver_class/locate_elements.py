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
print("Starting test with various locators used im find_element() method")
driver.get(host)
time.sleep(2)


full_name = driver.find_element(By.ID, 'userName')
full_name.send_keys('John Doe')

# email = driver.find_element(By.ID, "userEmail")
# email.send_keys('fake_email@gmail.com')

email = driver.find_element(By.ID, 'userEmail').send_keys("fake_email@gmail.com")

current_address = driver.find_element(By.TAG_NAME, 'textarea').send_keys("selenium found 'textarea' on html, this is first element of this type")

permanentAddress = driver.find_element(By.ID, 'permanentAddress').send_keys('330 Kendigs mill rd')

submit_buttom = driver.find_elements(By.CLASS_NAME, 'btn btn-primary')
print("Submit button found")
# primary_buttons = driver.find_elements(By.CLASS_NAME, 'btn btn-primary')
# print(primary_buttons)
# print(f"Primary buttons found: {len(primary_buttons)}")

elements_list = driver.find_elements(By.CLASS_NAME, 'form-control')
print(elements_list)
print(f"Number of elements in elements_list found: {len(elements_list)}")

driver.get("https://www.google.com/")

driver.find_element(By.LINK_TEXT, 'Gmail')
time.sleep(1)
print('Element found')
driver.find_element(By.PARTIAL_LINK_TEXT, 'mail').click()
print('Element found')
time.sleep(2)
driver.close()

# driver.find_elements(By.NAME, 'products')
# driver.find_elements(By.CLASS_NAME, 'input-text')
# driver.find_elements(By.TAG_NAME, 'a')
# driver.find_elements(By.XPATH, '//div[contains(@class, "lists")]')
# driver.find_elements(By.CSS_SELECTOR, '.input-class')
# driver.find_elements(By.LINK_TEXT, 'Log In')
# driver.find_elements(By.PARTIAL_LINK_TEXT, 'Add to')
