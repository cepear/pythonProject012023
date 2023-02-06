from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.utilities import *

logfile = f'{ROOT_DIR}/logs/{get_str_day()}.log'
log = create_logger(logfile)
class BasePage():
    """
    - abstract model (python class that includes common functions for selenium
    - 'page': python class that represents the attributes and methods
    - other pages will inherit base_page, hence they will share the common
    - base page will contain a lot of wrapper functions
    """

# All Locators (all values are ID locators):
    fn_input = 'firstName'
    ln_input = 'lastName'
    email_input = 'userEmail'
    gender_male_xpath = '//input[@id="gender-radio-1"]/..'
    mobile_number_input = 'userNumber'
    date_of_birth_input = 'dateOfBirthInput'
    hobbies_sp_xpath = '//input[@id="hobbies-checkbox-1"]/..'
    hobbies_reading_xpath = '//input[@id="hobbies-checkbox-2"]/..'
    upload_pic_input = 'uploadPicture'
    address_textarea = 'currentAddress'
    state_list = 'state'
    state_input = 'react-select-3-input'
    city_list = 'city'
    city_input = 'react-select-4-input'
    submit_button = 'submit'
    confirmation_msg = 'example-modal-sizes-title-lg'
    close_cm_button = 'closeLargeModal'

    def __init__(self, driver):
        self.driver = driver
        self.wdwait = WebDriverWait(self.driver, 10)

    # METHODS: create common selenium functions:
    # enter_text_by_id(id, text)
    # click_element_by_id(id)
    # click_element_by_xpath(id)
    # select_from_drop_down_by_id()
    # get_text_by_id()  -> returns string text
    # and many more, but create whenever you need them in few places.

    def enter_text_by_id(self, id, text):
        """General function to enter any text to any element found by ID"""
        try:
            log.info("Entering the text by ID...")
            # element = self.driver.find_element(By.ID, id) this regular way of finding element
            element =  self.wdwait.until(EC.presence_of_element_located((By.ID)))
            element.clear()
            element.send_keys(text)
            log.info(f"{text} is entered by ID")

        except (NoSuchElementException, TimeoutException) as err:
            time.sleep(10)
            log.error("Selenium Exception: test failed with following exception. \n{err}")
            print(err)

    def click_element_by_id(self, id):
        """General function to click on any element found by ID"""
        try:
            log.info("Clicking element by ID...")
            # element = self.driver.find_element(By.ID, id) this regular way of finding element
            element = self.wdwait.until(EC.element_to_be_clickable((By.ID)))
            element.click()
            log.info(f"Element is clicked", id)

        except (NoSuchElementException, TimeoutException) as err:
            time.sleep(10)
            log.error("Selenium Exception: test failed with following exception. \n{err}")
            print(err)

    def click_element_by_xpath(self, xpath):
        """General function to click on any element found by XPATH"""
        try:
            log.info("Clicking element by XPATH...")
            # element = self.driver.find_element(By.ID, id) this regular way of finding element
            element = self.wdwait.until(EC.element_to_be_clickable((By.XPATH)))
            element.click()
            log.info(f"Element is clicked", xpath)

        except (NoSuchElementException, TimeoutException) as err:
            time.sleep(10)
            log.error("Selenium Exception: test failed with following exception. \n{err}")
            print(err)

    def get_text_by_id(self, id):
        """General function to get text from any  found by ID"""
        try:
            log.info("Getting text by ID...")
            element = self.wdwait.until(EC.presence_of_element_located((By.ID)))
            result = element.text
            log.info(f"Returning the text.", id)
            return  element.text

        except (NoSuchElementException, TimeoutException) as err:
            time.sleep(10)
            log.error("Selenium Exception: test failed with following exception. \n{err}")
            print(err)



