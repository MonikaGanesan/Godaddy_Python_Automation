from selenium import webdriver
import time
from behave import *
from selenium.webdriver.support.ui import Select

Driver = webdriver.Chrome("C:\\Users\\monika.g\\Downloads\\chromedriver_win32\\chromedriver.exe")
Driver.get("https://login.salesforce.com/")
Driver.find_element_by_xpath("//input[@id='username']").send_keys("g.monikacit@brave-otter-45ku2w.com")
Driver.find_element_by_id("password").send_keys("iwillbeinGermany@123")
Driver.find_element_by_id("Login").click()

Code = input("Enter code to open:")
Driver.find_element_by_xpath("//input[@id='emc']").send_keys(Code)
time.sleep(5)
Driver.find_element_by_id("save").click()
time.sleep(30)

@given('We have a SF application to be logged in')
def login(context):
 Driver.get("https://login.salesforce.com/")
 Driver.find_element_by_xpath("//input[@id='username']").send_keys("g.monikacit@brave-otter-45ku2w.com")
 Driver.find_element_by_id("password").send_keys("iwillbeinGermany@123")
 Driver.find_element_by_id("Login").click()

 Code = input("Enter code to open:")
 Driver.find_element_by_xpath("//input[@id='emc']").send_keys(Code)
 time.sleep(5)

@when('you find the home page, goto Lead pages')
def LeadClick(context):
 print('i m here inside LeadClick')
 Driver.find_element_by_id("save").click()
 time.sleep(30)
 Driver.find_element_by_xpath("//a[@title ='Leads Tab']").click()
 #Driver.find_element_by_xpath("//select[@id='fcf']").click()
 sel = Select(Driver.find_element_by_xpath("//select[@id='fcf']"))
 sel.select_by_value("00B2v00000OJmUf")


#Driver.quit()
