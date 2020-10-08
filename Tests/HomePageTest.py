import unittest

from selenium import webdriver

from PageObjects.HomePageObjects import HomePage
from Resources.TestData import TestData


class HomePageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(TestData.CHROME_EXECUTABLE_PATH)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        cls.driver.get(TestData.BASE_URL)

    def test_launch_browser(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_signin_button()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
