import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import *
from src.pages_Classes.login_page import LoginPage
from src.utilities import *
import pytest

filepath1 = ROOT_DIR + '/data/forms.yml'
data = load_yaml_file(filepath1)


@pytest.mark.login2
def test_login_case2(driver):
    # Input data
    username = data['case2']['username']
    password = data['case2']['password']
    HOST = data['case2']['host']
    # Objects
    login_page = LoginPage(driver)

    # STEPS
    driver.get(HOST)
    time.sleep(5)
    disable_google_ads(driver)
    print("Starting login to book store page testing")
# Actions that need to be done in login page:
#1. enter username
    login_page.enter_username(username)

# 2. Enter password
    login_page.enter_password(password)

# 3. Click  Login button
    login_page.click_login()

# 4. click Go to Book store
    login_page.click_go_tobs()

# 5 . Click on the second book
# 6. Click to Add to your collection
# 7. Verify alert window is displayed
# 8. Click OK on the alert.
# 9. click to logout