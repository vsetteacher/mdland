# test
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from random import random
# define testing class
class mdTest(unittest.TestCase):
    def setUp(self):

        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        # navigate to the application home page
        self.driver.get("https://mdlanddev.mdland.com/eClinic/login_single.aspx")

# search username&password and submit
    def testLogin(self):

        elem = self.driver.find_element_by_class_name("inputLogin")
        elem.clear()
        elem.send_keys("ic-doctor")
        elem = self.driver.find_element_by_id("password")
        elem.clear()
        elem.send_keys("iClinic20151314")
        elem.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)
        self.driver.quit()

# navigate to waiting room page
    def testRegistry(self):
        elem = self.driver.find_element_by_class_name("inputLogin")
        elem.clear()
        elem.send_keys("ic-doctor")
        elem = self.driver.find_element_by_id("password")
        elem.clear()
        elem.send_keys("iClinic20151314")
        elem.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(10)

        elem = self.driver.find_element_by_id("WL")
        self.driver.execute_script("return arguments[0].scrollIntoView();", elem)
        elem.click()

    # create a new paitent record
        elem = self.driver.find_element_by_xpath("//*[@title='Registration']")
        elem.click()

        iframe = self.driver.find_elements_by_id('frm_reg_load_patient')[0]
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(iframe)
        elem = self.driver.find_element_by_id("txtPatientLastName")
        elem.clear()

        elem.send_keys("Peng")
        elem = self.driver.find_element_by_id("txtPatientFirstName")
        elem.clear()
        elem.send_keys("Richard")
        elem = self.driver.find_element_by_id("txtPatientDOB")
        elem.clear()
        elem.send_keys("12/07/1997")
        elem = self.driver.find_element_by_xpath("//*[@name='rdoPatientGender' and @value='M']")
        elem.click()
        elemList = self.driver.find_elements_by_xpath('//div[@id="divReg"]/table//input')
        for result in elemList:
            try:
                result.send_keys("133666666")
            except:
                continue
        elemList = self.driver.find_elements_by_xpath('//div[@id="divReg"]/table//select')

        for result in elemList:
                select = Select(result)
                select.select_by_index(2)

        elemList = self.driver.find_elements_by_link_text("Edit")
        elemList[0].click()

        elem = self.driver.find_element_by_xpath("//*[@name='PatientMutiRace']")
        elem.click()

        elem = self.driver.find_element_by_link_text("Save")
        elem.click()

        elemList[1].click()

        elem = self.driver.find_element_by_xpath("//*[@name='PatientMutiEthnicity']")
        elem.click()

        elem = self.driver.find_element_by_link_text("Save")
        elem.click()

        elem = self.driver.find_element_by_xpath("//div[@id='btnContinue']/table//span[@class='buttonTitle']")
        elem.click()

        elem = self.driver.find_element_by_link_text("Select")
        elem.click()















        #self.driver.quit()
"""if __name__ == '__main__':
    unittest.main(verbosity=2)"""
xTest = mdTest()
xTest.setUp()
xTest.testRegistry()

