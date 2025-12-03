import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utils.wait import wait_for


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть URL: {url}")
    def open(self, url: str):
        self.driver.get(url)
        return self

    @allure.step("Клик по элементу: {locator}")
    def click(self, locator: tuple):
        el = wait_for(self.driver, lambda d: d.find_element(*locator))
        el.click()
