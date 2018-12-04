# test
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

        #self.driver.quit()
if __name__ == '__main__':
    unittest.main(verbosity=2)