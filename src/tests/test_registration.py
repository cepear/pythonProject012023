from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from src.utilities import*
from src.pages.forms_page import FormPage
import pytest




filepath1 = ROOT_DIR + '/data/forms.yml'
data = load_yaml_file(filepath1)


@pytest.mark.forms1
def test_forms_case1(driver):

        # Input DATA:
        first_name = data['case1']['first_name']
        last_name = data['case1']['last_name']
        email = data['case1']['email']
        HOST = data['case1']['host']

    # Page objects:
        form_page = FormPage(driver)

        # Steps:
        driver.get(HOST)
        time.sleep(5)
        disable_google_ads(driver)
        print("Starting test with various properties and methods for WebElement class.")
        # enter first name , last name and email
        form_page.enter_first_name('Delete me Please')
        time.sleep(5)
        form_page.enter_first_name(first_name)
        time.sleep(5)
        form_page.enter_last_name(last_name)
        form_page.enter_email(email)
        form_page.select_gender("male")
        # select radio button Gender=Male
        # mobile_number = 9876543210
        form_page.enter_mobile_number('9876543210')
        # select checkboxes, select Sports, Reading
        form_page.select_hobbies(['sports', 'reading'])
        # enter message in text_area = '2906 Shell Road, 12224'
        form_page.enter_current_address('2906 Shell Road, 12224')
        # check is City list is enabled.
        form_page.select_state_city('NCR', 'Delhi')
        # select state=NCR
        time.sleep(2)
        form_page.click_submit()
        time.sleep(5)
        print("all information was entered and submitted...")
        # verify the message='Thanks for submitting the form'
        form_page.close_confirmation_page()
        # close the confirmation window
        print("Test Successfully executed.")




