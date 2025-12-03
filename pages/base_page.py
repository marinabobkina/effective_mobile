import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.wait import wait_for


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть URL: 'https://www.effective-mobile.ru/'")
    def open(self):
        self.driver.get("https://www.effective-mobile.ru/")
        return self
