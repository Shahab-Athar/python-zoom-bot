# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class EnglishClass():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_untitled(self):
        self.driver.get(
            "https://us04web.zoom.us/j/8521795787?pwd=OtBop0pjkng#success")
        self.driver.set_window_size(1260, 964)
        self.driver.find_element(By.CSS_SELECTOR, ".\\_1FvRrPS6").click()
        self.driver.close()
