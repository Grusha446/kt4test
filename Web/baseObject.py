from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
class BaseObject:
    def __init__(self, driver, logger):
        self.driver = driver
        self.base_url = "https://demo-opencart.ru/"
        self.logger = logger

    def find_element(self, locator, time=10):
        self.logger.info(f"Поиск элемента: {locator}")
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        self.logger.info(f"Поиск элементов: {locator}")
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))

    def go(self):
        return self.driver.get(self.base_url)