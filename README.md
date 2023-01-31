# pythonProject012023
Selenium WebDriver with Python
Working with Git as Version Control System
Local git actions
git init >> pycharm initialize VCS> Git

git add files that needed to have versioning

harm select files
git commit "comments that summarizes the changes"

pycharm enter comment and click Commit
Remote
git pull : get updates from the origin (github repo)
git push : share updates to the origin (to github repo)
Branching
having the multiple copies of the same repository on the same server
Pull request, Merging to master
Create PR and get Approval > merg PR and close your Request
Selenium setup
download selenium go to the Terminal (pycharm)
pip install selenium # library, code written by developers, open source
pip freeze # to check the selenium is in the list
download chromedriver

check the version of your chrome browser (if you dont have chrome browser, donwload and install it)
download the chromedriver from this location: driver website
select chromedriver_win32.zip if you have windows
Extract the downloaded folder and copy the chromedriver file
save in the Python main location

Go to python main folder: "C:\Program Files\Python39"
paste the copied chromedriver file here
import selenium, run sample code

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# created the object for chromedriver that talks to Chrome Browser
chr_options = Options()
chr_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chr_options)
print('maximizing the browser window')
driver.maximize_window()

driver.get("https://www.google.com/")
time.sleep(5)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium")
search_box.send_keys(Keys.ENTER)
time.sleep(5)

result = driver.find_element(By.ID, 'result-stats')
print(f"Search is done and result text is : {result.text}")

print("closing the browser after test")
driver.quit()
print("Test completed!")
MD document type
create and save file with .md extention
# - title1
## - title2

*italics text*
**bold text**

- item1
- item2

* item1
* item2

 use 3 ` to display the code snippet 
  
  [text for the link](url here)
  ![text for image](location of the image)
  [![Watch the video](https://i.imgur.com/vKb2F1B.png)](https://youtu.be/vt5fpE0bzSY)

Example:

ls -l Documents
1. HTML DOM
HTML Introduction
HTML is the standard markup language for creating Web pages. Document Object Model - html document (DOM)

What is HTML?
HTML stands for Hyper Text Markup Language
HTML is the standard markup language for creating Web pages
HTML describes the structure of a Web page
HTML consists of a series of elements
HTML elements tell the browser how to display the content
HTML elements label pieces of content such as "this is a heading", "this is a paragraph", "this is a link", etc.
HTML DOM - html document object model this is where you find the web page elements and their 'description'.

<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
Elements of HTML forms
HTML forms

NOTE: Find out more about http messages and popular status codes here

Homework:
Read and try out

https://www.w3schools.com/html/html_intro.asp
https://www.w3schools.com/html/html_elements.asp
https://www.w3schools.com/html/html_attributes.asp
https://www.w3schools.com/html/html_links.asp
https://www.w3schools.com/html/html_forms.asp (all other pages for html forms)
What type of Elements we can see on the web page?
Element types are defined by tags in the HTML document (DOM)

images
<img src="img_girl.jpg" alt="Girl in a jacket" width="500" height="600">
buttons
<button name="submit" id="login" type="button">Login</button>
links
<a href="https://www.w3schools.com">Visit W3Schools.com!</a>
text box, checkbox, radio button, password etc. The <input> tag specifies an input field where the user can enter data.
The different input types are as follows:

<input type="button">
<input type="checkbox">
<input type="color">
<input type="date">
<input type="datetime-local">
<input type="email">
<input type="file">
<input type="hidden">
<input type="image">
<input type="month">
<input type="number">
<input type="password">
<input type="radio">
<input type="range">
<input type="reset">
<input type="search">
<input type="submit">
Sample:

<form action="/action_page.php">
  <label for="fname">First name:</label>
  <input type="text" id="fname" name="fname"><br><br>
  <label for="lname">Last name:</label>
  <input type="text" id="lname" name="lname"><br><br>
  <input type="submit" value="Submit">
</form>
drop down
<select><option>NY</option>State</select>
checkbox
radio buttons
videos
Find out about different tags used in the html document here

Attributes
Each element consist of attributes

<div class="myDiv" id="my-div">
  <h2>This is a heading in a div element</h2>
  <p>This is some text in a div element.</p>
</div>
here 'div' is a tag and 'class' is an attribute. type

Using chrome developers tools options to inspect web elements
Tags are purple
Attributes are in red
Values of the attributes will be in blue
text in the elements, that are in the tags, will be in black
Selenium WebDriver: Finding Elements (locating) on the Web page.
We need to tell Selenium how to find an element so that it can simulate a desired user action, or look at the attributes or state of an element so that we can perform a check. For example, if we want to search for a product, we need to find the search text field and search button visually. We enter the search term by pressing various keys on the keyboard and click on the search button to submit our search request.

We can automate the same actions using Selenium. However, Selenium does not understand these fields or buttons visually as we do. It needs to find the search textbox and search button to simulate keyboard entry and mouse click programmatically.

Selenium provides various find_element methods to find elements on a web page. These methods search for an element based on the criteria supplied to them. If a matching element is found, an instance of WebElement is returned or the NoSuchElementException exception is thrown if Selenium is not able to find any element matching the search criteria.

Locator (finding the elements)
Available locators in selenium (find_element(By.locator, 'value')):

ID
NAME
XPATH
CLASS_NAME
CSS_SELECTOR
LINK_TEXT
PARTIAL_LINK_TEXT
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("myapp.com")
# all of below methods return single element, 
# return first element if multiple elements found in html document by given locator
driver.find_element(By.ID, 'search')
driver.find_element(By.NAME, 'q')
driver.find_element(By.XPATH, '//form[0]/div[0]/input[0]')
driver.find_element(By.CSS_SELECTOR, '#search')
driver.find_element(By.CLASS_NAME, 'input-text')
driver.find_element(By.TAG_NAME, 'input')
driver.find_element(By.LINK_TEXT, 'Log In')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Log')
Selenium also provides various find_elements_by methods to locate multiple elements. These methods search and return a list of elements that match the supplied values.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("myapp.com")
# all of below methods return list of elements , [prod1, prod2, ..]
driver.find_elements(By.ID, 'products')
driver.find_elements(By.NAME, 'products')
driver.find_elements(By.CLASS_NAME, 'input-text')
driver.find_elements(By.TAG_NAME, 'a')
driver.find_elements(By.XPATH, '//div[contains(@class, "lists")]')
driver.find_elements(By.CSS_SELECTOR, '.input-class')
driver.find_elements(By.LINK_TEXT, 'Log In')
driver.find_elements(By.PARTIAL_LINK_TEXT, 'Add to')
Demo website: https://www.seleniumeasy.com/test/basic-first-form-demo.html

Example of Locating the element uniquely

1. xpath
msg_xpath = '//form/div/input[@id="user-message" and @class="form-control"]'
# Building xpath 
# //tag[@att='value']
# //tag[text()='value']

# option1: 
text_xpath = "//span[@class='mr-3' and @name='text1']"

# Using text of the element to build the xpath: 
# option2: 
text1_xpath = "//span[text()='Click Button to see alert ']"
# option3: 
text1_xpath = "//span[contains(text(), 'Click Button to')]"

# 12/03/2022 HW reading: https://www.guru99.com/xpath-selenium.html
This is the xpath for the below element.

<span class="mr-3" name="text1">Click Button to see alert </span>
<input type="text" class="form-control" name="input-message" placeholder="Please enter your Message" id="user-message">
Some text here
</input>
<div class="col">
	<button id="alertButton" type="button" class="btn btn-primary">Click me</button>
</div>
2. CSS Selector:
Syntax for Locating by CSS Selector Usage

||Method || Target Syntax || Example || |Tag and ID | css=tag#id | css=input#email | |Tag and Class | css=tag.class | css=input.inputtext | |Tag and Attribute| css=tag[attribute=value] | css=inp ut[name=lastName] | |Tag, Class, and Attribute| css=tag.class[attribute=value] | css=input.inputtext[tabindex=1] |

Find out more about CSS Selector here

** Converting Xpath to CSS selector ** HTML document elements you want to locate:

<span class="mr-3" name="text1">Click Button to see alert </span>
<input type="text" class="form-control" name="input-message" placeholder="Please enter your Message" id="user-message">
Some text here
</input>
<div class="col">
	<button id="alertButton" type="button" class="btn btn-primary">Click me</button>
</div>
CSS selectors to build based on above html elements:

"//span[text()='Click Button to see alert ']"
text_css_selector = "span:contains('Click Button to see alert ')"

text_xpath = "//span[@class='mr-3'" 
text_css_selector = "span.mr-3"

alert_xpath = "//span[@id='alert1']" 
alert_css_selector = "span#alert1"

alert_id = 'alertButton'
alert_xpath = "//button[@id='alertButton' and @type='button']"
alert_css_selector = 'button#alertButton'
alert_css_selector = 'button.btn-primary'
Tags to know:

links, images, forms (textbox, radio, checkbox, submit, fileupload, <input>, <label>, <select>, <textarea>, <button>)
    div - container to holds the styled elements
CSS - styling document, goes along with html document 
NOTE: read about html click here

2. WebDriver class
simulates browser action

properties: current_url, current_window_handle, window_handles, name, title,
methods: find_element(), send_keys(), switch_to.window(), back(), refresh() ....
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.back()
driver.forward()
driver.find_element(By.XPATH, 'somexpath')
driver.refresh()
driver.get()
driver.implicitly_wait(10)
driver.maximize_window()
API - application programming interface
SOAP - xml, older api type REST API - json, xml (http messages and responses)

add.resources('/query') def query(function, symbol, apikey): # verify apikey # find global quote for symbol

https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol=IBM&apikey=OZ8SJC8A5DGNC

https://dog.ceo/api/breed/hound/english/images/random

** Homework** Read about different message types, this will help you to understand the API and messages used in an API as a connection between server and webpage(local on the browser) Method: GET, POST, PUT, DELETE Note: remember status codes: 200, 401, 404, 500, 300, 201

3. WebElement class
simulates element actions Done topics:

Working with find_elements() - returns list of elements
Webelement properties (text, size, tag_name)
Webelement methods: clear(), click(), send_keys(), is_displayed(), is_enabled(), get_attribute()
Working with alerts and pop-up windows (from previous session, from webdriver class)
Working with forms, textboxes, checkboxes, and radio buttons
Working with dropdowns and lists
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

element = driver.find_element(By.XPATH, 'somexpath')
element.is_displayed()
element.is_enabled()
element.is_checked()
element.click()
element.send_keys("your message here ")
element.send_keys(Keys.RETURN)  # hitting the enter key 
element.send_keys(Keys.ESCAPE) 
element.send_keys(Keys.UP) 
element.text   # property - you must not use parenthesis
12/01/2022 Agenda of recent and future classes
11/27 - WebElement: forms, jscript execute, xpath

12/1 - Q&A - overall - Technical Interview Questions

12/3 - selenium WebElement: locators(xpath, css selector), drop down, alerts

12/4 - Selenium advanced: explicit waits

12/8 - Selenium advanced: mouse movements, screenshots, logs

12/8 - Unit Testing Framework: Pytest

12/10-12/11 - Automation Testing Framework: Pytest, page object modeling

Java - backend language (python, C#, ...)

javascript - UI/front end language (executed on the browser)

Assertion:

from python to verify something
it generates pass/fail status in unittests
Xpath="//tagname[@attribute='value']"
msg_xpah = "//input[@name = 'input-message']"
WebElement class : Forms
WebElement class : get_attribute
html document:

...
<input type="text" id="firstname" name="firstname" value=""
title="First Name" maxlength="255" class="input-text
required-entry">
...
python selenium code:

...
firstname_elem = driver.find_element(By.ID, fn_input)
print(firstname_elem.get_attribute('maxlength')) -> 255
print(firstname_elem.get_attribute('name')) -> 'firstname'
print(firstname_elem.get_attribute('class')) -> "input-text required-entry"
firstname_elem.send_keys(Keys.ENTER)
print(firstname_elem.get_attribute('class')) -> "input-text required-entry"
...
WebElement class : drop down list
Using Select class to handle drop down list element that is with 'select' tag and 'option' child elements

...
<select id="select-language" title="Your Language" onchange="window.location.href=this.value">
    <option value="http://demo.magentocommerce.com/?___store=default&amp;___from_store=default" selected="selected">English</option>
    <option value="http://demo.magentocommerce.com/?___store=french&amp;___from_store=default">French</option>
    <option value="http://demo.magentocommerce.com/?___store=german&amp;___from_store=default">German</option>
</select>
...
Python Selenium code for above element:

from selenium.webdriver.support.select import Select

drop_down_elem = driver.find_element(By.TAG_NAME, country_dd_tag)
country_selection = Select(drop_down_elem)
print('First Selected option: ', country_selection.first_selected_option.text)
country_selection.select_by_index(2)
print("Selected country: ", country_selection.all_selected_options[0].text)
country_selection.select_by_value('FRA')
country_selection.select_by_visible_text('United States')
WebElement class : Alerts
...
# switch to the alert
alert = driver.switch_to.alert()
# get the text from alert
alert_text = alert.text
alert.accept() # click OK button on alert box
alert.dismiss() # click Cancel button on alert box
alert.send_keys() # enter a text on the alert box
...
4. Synchronizing Tests
Difference between implicit and explicit waits What is explicit wait? How to build explicit wait with different conditions?

Synchronization methods: explicit wait : WebDriverWait class, expected_conditions class *practice here: https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver *

WebDriver provides the WebDriverWait and expected_conditions classes to implement an explicit wait. practice website

Using implicit wait
The implicit wait offers a generic way to synchronize the entire test or group of steps in WebDriver. Implicit wait is useful in dealing with situations where the application's response time is inconsistent due to network speed or applications that use dynamically rendered elements with Ajax calls.

When we set an implicit wait on WebDriver, it polls or searches the DOM for a certain amount of time to find an element or elements if they are not immediately available. By default, the implicit wait timeout is set to 0.

Once set, the implicit wait is set for the life of the WebDriver instance or for the entire duration of the test, and the WebDriver applies this implicit wait for all the steps that find the elements on the page unless we set it back to 0. The webdriver class provides the implicitly_wait() method to configure timeout.

Using explicit wait
The explicit wait is another wait mechanism available in WebDriver to synchronize tests. Explicit wait provides a better control when compared to implicit wait. Unlike an implicit wait, we can use a set of predefined or custom conditions for the script to wait for before proceeding with further steps.

An explicit wait can only be implemented in specific cases where script synchronization is needed. WebDriver provides the WebDriverWait and expected_conditions classes to implement an explicit wait. The expected_conditions class provides a set of predefined conditions to wait for before proceeding further in the code.

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.implicitly_wait(20)

# wait for the alert to present
# alert = WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())
alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
# wait for Clear All link to be visible
clear_all_link = WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.LINK_TEXT, "Clear All")))
wdwait = WebDriverWait(driver, 15)
wdwait.until(EC.text_to_be_present_in_element((By.ID, target_text_id), 'Selenium'))
wdwait.until(EC.visibility_of_element_located((By.ID, hidden_button_id)))
wdwait.until(EC.element_to_be_clickable((By.ID, disabled_button_id)))
wdwait.until(EC.element_to_be_selected(driver.find_element(By.ID, checkbox_id)))
You can see more examples of the conditions from expected_conditions class on page 94 of the book.

5. Chapter 9. Advanced Techniques of Selenium WebDriver
practice here: https://jqueryui.com/droppable/

In this chapter, you will learn more about:

Creating tests that simulate keyboard or mouse events using the Actions class
Simulating mouse operations such as drag-and-drop and double-click
Running JavaScript code: execute js >> alternative of button.click() (we have seen how to scroll down on the page)
Capturing screenshots and movies of test runs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# combination of shift + n  (key_down to press the shift key, then key_up to release that)
ActionChains(driver).key_down(Keys.SHIFT).send_keys('n').key_up(Keys.SHIFT).perform()

# MOUSE ACTIONS: HOVER OVER ELEMENT
age_field = driver.find_element(By.ID, "age")
ActionChains(driver).move_to_element(age_field).perform()
Taking screenshots with selenium
from selenium import webdriver

driver = webdriver.Chrome()
scrshot_dir = '../screenshots/'
driver.save_screenshot(scrshot_dir+'dragdrop1.png')
Logging with Python
import logging

def create_logger(file):
    logging.basicConfig(filename=file,
                        level=logging.INFO,
                        format='%(asctime)-15s [%(levelname)s]: %(message)s',
                        filemode='a')
    return logging.getLogger()
6. Chapter 8. Framework in Test Automation
The way of engineering your project, put your code in structured way:

Pytest - unit testing framework
to generate test reports with pass and fail status.
hooks(fixtures) this will help you to better manager your execution
how to run regression suites
Reading links:
Getting Started With Pytest and Selenium
Full and Complete information about pytest with examples
Pytest documentation
Optional Reading on Pytest implementation, it is from development point of view
Behaviour Driven Framework with Pytest-bdd
Detailed BDD Level Up recording
Please Send request to parent folder in order to have all Self Study Materials. Click here to Send Request for Self Study Materials google driver folder.
Please watch this recording that shows how to run Automation scripts with Jenkins and AWS
Page Object Modeling (designing pattern)
handle locators and page functions of each page
this is good when you work with complex project.
helps you to maintain changing web elements
Classes, Inheritance, encapsulation, polymorphism
General Understanding about Test Automation Frameworks
1. Data Driven Framework:
Driver Script per scenario -> Data File -> input/output file Driver script per scenario >> Data file >> execution >> compare with expected results

2. Keyword Driven Framework:
Driver Script > Keyword(steps consist of function names and inputs) >> data file

3. Behavior Driven Framework (from Test Automation perspective)
**Components of BDD Test Automation Framework

src: a. Feature file: Gherkin scenarios (plain english using Given, When, Then keywords) Given I am in login page.

b. Steps definition @Given("I am in login page.") def login(): # steps to login, code

c. pages: Page Object Modeling Design Pattern, The way of designing your selenium scripts - Object oriented programming concepts (class, object, Inheritance, encapsulation, polymorphism, abstraction)

d. utilities.py | helper.py | generic_helper.py >> functions to use to handle data file, reports, general python functions

e. Fixture files (in pytest it is confest.py ), some framework config files

Data

config.yml
stocks_buy.yml
Logs

05152022.log
Reports

051520221110052_stockbuy_report.html
PYTEST
running tests :

pytest -s -v test_scenarios.py
pytest -s -v test_scenarios.py::test_sample_pytst

# if you have marks for the functions
pytest -s -v -m sample1

$ pytest -s -v -m regression --disable-pytest-warnings >> reports/20211123_919_regression
Pytest Fixtures

SetUp : steps to execute before session/file/functions (scope)
TearDown : steps to execute after session/file/functions (scope)
Must-know for Automation Testing:
Web UI Functionality (python, selenium WebDriver, Yes)

API Automation

manual (Yes) : Postman tool, study API testing and webservices (Akmal to send a video about this)
Automation (maybe, REQUESTS library) (Akmal to send links for quick courses) NOTE: Find out more about http messages and popular status codes here
Backend Automation (NO, sql connection with python, server side automation with python)

Performance testing (NO - jmeter, LoadRunner etc.)

Security Testing (i.e.Penetration testing, NO)

Self Study Materials: Chapter 10 Integration with Other Tools and Frameworks
Videos to watch:

Bdd Framework Overview
CI/CD pipelines and working with Jenkins and AWS
All Mock interviews to watch
Automation practice websites:

https://courses.letskodeit.com/practice
https://jqueryui.com/droppable/
https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver
Useful links and References:
HTTP messages used in API calls
HTML document and tags
Learning Selenium Testing Tools with Python (book)
The Ultimate Selenium Python Cheat Sheet for Test Automation
What is xpath and how to build them.
Socratica playlist in youtube
