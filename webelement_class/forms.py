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
    # INPUT DATA:
    first_name = 'john'
    last_name = 'doe'
    email = 'jdoe@email.com' \
            ''
    # All Locators
    fn_input = 'firstName'
    ln_input = 'lastName'
    email_input = 'userEmail'
    gender_male_xpath = '//input[@id="gender-radio-1"]/..'
    mobile_number_input = 'userNumber'
    date_of_birth = 'dateOfBirthInput'
    subjects = 'subjectsContainer'
    hobbies_sports = 'hobbies-checkbox-1'
    hobbies_reading = 'hobbies-checkbox-2'
    upload_picture_input = 'uploadPicture'
    address_textarea = 'currentAddress'
    city_list = 'city'
    city_input = 'react-select-4-input'
    state_list = 'state'
    state_input = 'react-select-3-input'
    submit_button = 'submit'
    confirmation_message = 'example_modal_sizes_title_lg'
    close_confirm_message = 'closeLargeModal'

    # Steps :
    print("-----Starting test with WebDriver properties------------")
    driver.get(host)
    time.sleep(2)
    driver.find_element(By.ID, fn_input).send_keys(first_name)
    driver.find_element(By.ID, ln_input).send_keys(last_name)
    driver.find_element(By.ID, email_input).send_keys(email)
    # gender
    driver.find_element(By.ID, gender_male_xpath).click()
    time.sleep(2)
    #mobile_number = 6564563989
    driver.find_element(By.ID, mobile_number_input).send_keys('6564563989')
    # (optional) enter date_of_birth = 27 Nov 2022
    # (optional) enter subjects = 'selenium forms testing
    # select checkboxes, select Sports, Reading
    driver.find_element(By.ID, hobbies_sports).click()
    driver.find_element(By.ID, hobbies_reading).click()
    # (optional) upload picture
    # enter message in text_area = '2906 Shell Rd, Brooklyn, NY, 12224"
    driver.find_element(By.ID, address_textarea).send_keys('2906 Shell Rd, Brooklyn, NY, 12224')
    # check if city list is enabled
    print('Is City list is enabled?', driver.find_element(By.ID, city_list).is_enabled())
    # select state= NCR
    print('Is State list is enabled?', driver.find_element(By.ID, state_list).is_enabled())
    driver.find_element(By.ID, state_input).send_keys('NCR')
    # check is City list is enabled after selecting state?
    print('Is City list is enabled after selecting state?', driver.find_element(By.ID, city_list).is_enabled())
    # select city = Delhi
    driver.find_element(By.ID, city_input).send_keys('Delhi')
    # check if Male gender is selected
    print('Is Male gender selected?', driver.find_element(By.XPATH, gender_male_xpath).is_selected())
    # check if Sports is selected in Hobbies.
    print('Is Sports selected from Hobbies??', driver.find_element(By.ID, hobbies_sports).is_selected())
    # click Submit
    driver.find_element(By.ID, submit_button).click()
    # verify the message = 'Thanks for submitting the form"
    print("Is Confirmation message displayed?", driver.find_element(By.ID, confirmation_message).is_displayed())
    # close the confirmation window
    driver.find_element(By.ID)



except (Exception) as err:
    print(err)
    print('Python Exception: Test failed with above error')
except (NoSuchElementException, TimeoutException) as err:
    print("Selenium Exception: Test failed with above error")

finally:
    driver.quit()