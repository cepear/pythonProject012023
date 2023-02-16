from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from src.utilities import *


HOST = "https://jqueryui.com/resources/demos/droppable/default.html"
scrshot_dir = '../../../screenshots/'
#logfile = '../logs/20230131_drag_drop.log'    - this is hard coded, line above will generate new file name for each day
logfile = f'../logs/{get_str_day()}_drag_drop.log'
log = create_logger(logfile)

log.info("*****************Drag and drop scenario started*******************")
# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
# chr_options.add_experimental_option('excludeSwitches',["disable-popup-blocking"])
driver = webdriver.Chrome(options=chr_options)
log.warning('maximizing the browser window')
driver.maximize_window()
# This sets a sticky timeout to implicitly wait for an element to be found, or a command to complete.
driver.implicitly_wait(20)
time.sleep(0)

try:
    # All Locators (all values are ID locators):
    draggable_id = 'draggable'
    droppable_id = 'droppable'


  # Steps:
    driver.get(HOST)
    time.sleep(2)
    driver.save_screenshot(scrshot_dir+'dragdrop1.png')
    # disable_google_ads(driver)

    # Code for the drag and drop will be here
    log.info("verify drop box text before dropping, expected: 'Drop here'")
    drag_obj = driver.find_element(By.ID, draggable_id)
    drop_obj = driver.find_element(By.ID, droppable_id)
    log.info(f"Text in the droppable object before is :  {drop_obj.text}")
    assert drop_obj.text == 'Drop here', log.error("Drop box text verification before drop action is failed")
    driver.save_screenshot(scrshot_dir+'dragdrop2-before.png')


    log.info("drag and drop object into the box")
    actions = ActionChains(driver)
    actions.drag_and_drop(drag_obj, drop_obj).perform()
    #actions.click_and_hold(drag_obj).pause(2).release(drop_obj).perform()   ---alt way for the above code.
    # verify drop box text after dropping, expected: 'Dropped'
    log.info("verify drop box text after dropping, expected: 'Dropped'")
    log.info(f"Text in the droppable object after is : {drop_obj.text}")
    assert drop_obj.text == 'Dropped!', log.error("Drop box text verification after drop action is failed")
    driver.save_screenshot(scrshot_dir+'dragdrop3-after.png')




    time.sleep(2)
    log.info("Drag and drop Test completed successfully")

except (FileNotFoundError, ZeroDivisionError)  as err:
    time.sleep(10)
    log.error("Python Exception: test failed with following exception.")
    log.error(err)
    driver.save_screenshot(scrshot_dir+'PythonException.png')

except (NoSuchElementException, TimeoutException) as err:
    time.sleep(10)
    log.error("Selenium Exception: test failed with following exception.")
    log.error(err)
    driver.save_screenshot(scrshot_dir+'SeleniumException.png')

finally:
    # close all tabs:
    driver.quit()
    log.info("===========TEST Completed!!===================")