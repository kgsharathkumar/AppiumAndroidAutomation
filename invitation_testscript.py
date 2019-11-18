import unittest
from appium import webdriver
from time import sleep

class InvitationAppTestAppium(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='5.1'
        desired_caps['deviceName']='RGS8DUAU99999999'
        desired_caps['appPackage']='com.pathtech.einvitation'
        desired_caps['appActivity']='.MainOptionActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_ClickPlusLink(self):
        self.PlusButton = self.driver.find_element_by_id("com.pathtech.einvitation:id/fab")
        self.PlusButton.click()
        sleep(5)
        self.PhotoButton = self.driver.find_element_by_id("com.pathtech.einvitation:id/galleryIcon")
        self.PhotoButton.click()
        sleep(5)



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(InvitationAppTestAppium)
    unittest.TextTestRunner(verbosity=2).run(suite)