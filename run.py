from selenium import webdriver
import time
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

def teardown(active_driver):
    active_driver.close()
    active_driver.quit()


driver = webdriver.Chrome("C:\\Users\\monika.g\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("https://10.240.145.147:7025/OSF_WEB/")
driver.maximize_window()
driver.find_element_by_xpath("//button[@id = 'details-button']").click()
driver.find_element_by_xpath("//a[@id='proceed-link']").click()
actions = ActionChains(driver)
# phase - 1
driver.find_element_by_id("username").send_keys("mganesan")
driver.find_element_by_id("password").send_keys("Rujan002")
driver.find_element_by_id("kc-login").submit()
time.sleep(5)
assert_title = "One Sales Frontend (OSF)"
assert_time = 1
while str(driver.title).strip() != assert_title:
    if assert_time >= 30:
        print("Waited for {}, still web page not loaded.".format(assert_time))
        teardown(driver)
        sys.exit(1)
    assert_time = assert_time + 1
    print("waiting for OSF Title:`{}` current Title: `{}`".format(assert_title, driver.title))
    time.sleep(assert_time)
print("Success: App Title : {}".format(driver.title))
# pre-req
driver.get("http://oib.itcentrala.com/oib-generator/")
oibid = driver.find_element_by_xpath("//div[@class='oib']").text
print("OIB Generated:{}".format(oibid))
driver.back()
time.sleep(5)
# phase - 2
driver.find_element_by_id("tabForm:mainTabs:oibInput").send_keys(oibid)
time.sleep(3)
driver.find_element_by_id("tabForm:mainTabs:searchBtn").click()
time.sleep(8)
driver.find_element_by_xpath("//span[@class='ui-button-text ui-c' and contains(text(),'Novi')]").click()
time.sleep(8)
driver.find_element_by_id("tabForm:mainTabs:IfirstName").send_keys("monika")
driver.find_element_by_id("tabForm:mainTabs:IlastName").send_keys("ganesan")
driver.find_element_by_id("tabForm:mainTabs:IbirthDate_input").send_keys("31.10.1994")
time.sleep(6)
actions.send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
actions.move_to_element(driver.find_element_by_xpath("//div[@id='tabForm:mainTabs:Igender']")).click().perform()
driver.find_element_by_xpath("//li[contains(text(),'Mu')]").click()
actions.move_to_element(driver.find_element_by_id("tabForm:mainTabs:idDocNo")).perform()
time.sleep(5)
driver.find_element_by_id("tabForm:mainTabs:idDocNo").send_keys("123456789")
time.sleep(5)
driver.find_element_by_xpath("//div[@id='tabForm:mainTabs:j_idt548']//span[@class='ui-chkbox-icon ui-icon ui-icon-blank ui-c']").click()
driver.find_element_by_id("tabForm:mainTabs:partyContactMobile").send_keys("3851234564")
time.sleep(5)
driver.find_element_by_name("tabForm:mainTabs:street_input").click()
driver.find_element_by_xpath("//span[@id='tabForm:mainTabs:street']//button[@class='ui-autocomplete-dropdown ui-button ui-widget ui-state-default ui-corner-right ui-button-icon-only']").click()
time.sleep(10)
driver.find_element_by_id("tabForm:mainTabs:street_input").send_keys("ILICA")
time.sleep(6)
driver.find_element_by_xpath("//div[@id='tabForm:mainTabs:street_panel']//li[contains(text(),'(10000 ZAGREB)')]").click()
time.sleep(9)
driver.find_element_by_id("tabForm:mainTabs:streetNo").send_keys("13")
time.sleep(6)
driver.find_element_by_xpath("//a[@id='tabForm:mainTabs:newMobileEditBtn']").click()
time.sleep(20)
driver.find_element_by_xpath("//button//span[text()='Nastavi dalje unos']").click()
try:
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ID, "tabForm:mainTabs:billMedia_label"))
    )
except:
    print("no element found")

driver.find_element_by_id("tabForm:mainTabs:billMedia_label").click()
time.sleep(5)
driver.find_element_by_id("tabForm:mainTabs:billMedia_1").click()
time.sleep(10)
driver.find_element_by_id("tabForm:newMobileEditBtn").click()
time.sleep(20)
# try:
#     element = WebDriverWait(driver, 30).until(
#         EC.presence_of_element_located((By.XPATH, "//h1[@title='M']"))
#     )
# except:
#     print("no element found")
#print(driver.title)
print(driver.current_url)
val = driver.find_elements_by_xpath("//div[@class='card-header']/h1")
for each in val:
    print(each.text)
time.sleep(10)
print("bye")
sys.exit(1)
driver.find_element_by_xpath("//button[@class='btn btn-theme my-1']").click()
time.sleep(20)
driver.get("https://10.240.145.147:7025/OSF_WEB/osf/simSearchDis.jsf")
time.sleep(20)
s = Select(driver.find_element_by_id("tabForm:mainTabs:cardTypesOneMenu"))
s.select_by_value("Postpaid")
s = Select(driver.find_element_by_id("tabForm:mainTabs:physicalCardTypesOneMenu"))
s.select_by_value("SIM")
s = Select(driver.find_element_by_id("tabForm:mainTabs:statusesOneMenu"))
s.select_by_value("Available")
driver.find_element_by_id("tabForm:mainTabs:agentsACMenu_input").send_keys("Zg08")
driver.find_element_by_xpath("//li[@data-item-label ='ZG08']").click()
driver.find_element_by_id("tabForm:mainTabs:amountInput").send_keys("1")

#driver.find_element_by_id("tabForm:mainTabs:cardTypesOneMenu").click()
#teardown(driver)
