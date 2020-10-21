from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException

Driver = webdriver.Chrome("C:\\Users\\monika.g\\Downloads\\chromedriver_win32\\chromedriver.exe")
Driver.get("https://in.godaddy.com/")
time.sleep(5)
Driver.find_element_by_xpath("//a[@class ='pop']").click()
time.sleep(5)
Driver.find_element_by_xpath("//a[@id ='xid-0d47b1cc-e9d3-4069-94aa-d141fb4b0d7a']").click()
time.sleep(5)
Driver.find_element_by_xpath("//button[@id='id-wordpress-openexchange-tier1']").click()
time.sleep(10)
List = Driver.find_elements_by_class_name("custom-control-description")
#for i in List:
 #   if i.text == '24 months':
 #       Driver.find_element(i).click()
 #       Break

#Driver.find_element_by_name('24 months').click()
time.sleep(5)
Driver.find_element_by_xpath("//label[@id='label-wordpress-openexchange-tier1.term.numberOfTerms.24-{termType}']").click()
time.sleep(5)
Driver.find_element_by_xpath("//label[@id='label-Add-Essential-Website-Security']").click()
time.sleep(10)
#try:
 #Driver.find_element_by_xpath("//button[@class ='btn btn-purchase continue-button']").click()
#except:
 #ElementClickInterceptedException
 #time.sleep(5)
Driver.maximize_window()
Driver.find_element_by_xpath("//button[@class ='btn btn-purchase continue-button']").click()
time.sleep(5)
Driver.find_element_by_xpath("//input[@id='le']").send_keys("Like the Experience !")
time.sleep(2)
Driver.find_element_by_xpath("//button[@class='btn btn-primary btn-purchase']").click()
time.sleep(5)
Driver.find_element_by_xpath("//button[@class='btn btn-purchase btn-block']").click()
time.sleep(10)
Driver.find_element_by_class_name("dropdown-text").click()
time.sleep(10)
Driver.find_element_by_xpath("//a[@value='12']").click()
time.sleep(10)

Driver.find_element_by_xpath("//div[@class='item-product']/div[@class='product-info-no-icon clearfix']//button[@data-eid='gce.cart.basket.remove-group.click']").click()
time.sleep(5)
Driver.find_element_by_xpath("//button[@class='btn btn-primary btn-max-width']").click()
print("SUperb")
Driver.quit()




