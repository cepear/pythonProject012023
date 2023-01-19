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
    # All Locators
    fn_input = 'firstName'
    ln_input = 'lastName'
    email_input = 'userEmail'
    gender_male = 'gender-radio-1'
    mobile_number = 'userNumber'
    date_of_birth = 'dateOfBirthInput'
    subjects = 'subjectsContainer'
    hobbies_sports = 'hobbies-checkbox-1'
    hobbies_reading = 'hobbies-checkbox-2'
    upload_picture_input = 'uploadPicture'
    address_textarea = 'currentAddress'
    city_list = 'react-select-4-input'
    state_list = 'react-select-3-input'
    submit_button = 'submit'
    confirmation_message = 'example_modal_sizes_title_lg'
    close_confirm_message = 'closeLargeModal'

    # Steps :
    print("-----Starting test with WebDriver properties------------")
    driver.get(host)
    time.sleep(2)
    #first name
    #last name
    # gender
    # email
    #mobile_number = 6564563989
    # (optional) enter date_of_birth = 27 Nov 2022
    # (optional) enter subjects = 'selenium forms testing
    # select checkboxes, select Sports, Reading
    # (optional) upload picture
    # enter message in text_area = '2906 Shell Rd, Brooklyn, NY, 12224"
    # check if city list is enabled
    # select state= NCR
    # select city = Delhi
    # check if Male gender is selected
    # check if Sports is selected in Hobbies.
    # click Submit
    # verify the message = 'Thanks for submitting the form"



except (Exception) as err:
    print(err)
    print('Python Exception: Test failed with above error')
except (NoSuchElementException, TimeoutException) as err:
    print("Selenium Exception: Test failed with above error")

finally:
    driver.quit()