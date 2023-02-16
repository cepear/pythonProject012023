from src.pages_Classes.base_page import BasePage
from src.utilities import *
from selenium.webdriver.common.keys import Keys

logfile = f'{ROOT_DIR}/logs/{get_str_day()}.log'
log = create_logger(logfile)


class LoginPage(BasePage):
    """ Page Model of Login webpage that defines
    all locators as variables and actions as methods"""
    # Input data:
    username = 'anna'
    password = 'Login@123'

    # All locators as variable:
    username_input = 'userName'   #ID
    password_input = 'password'   #ID
    login_button = '//*[@id="login"]' # XPATH
    go_to_bs = 'gotoStore'  # ID
    book_to_open = 'Learning JavaScript Design Patterns'  # link text
    add_to_your_collection = 'text-right fullButton'    # class name
    alert_displayed_click = ''    # driver.switchTo.alert.accept()
    back_to_book_store = "text-left fullButton"  # class name
    logout = ' // *[ @ id = "submit"]'  # XPATH

    # First I have to ask myself - What actions I can do in page? - Methods
    # enter_user_name(self, username)
    # enter_password(self, password)
    # click_login(self)
    # go_to_bs(self,









