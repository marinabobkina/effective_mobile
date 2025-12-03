import allure
from pages.base_page import BasePage
from locators import home_locators as L


class HomePage(BasePage):
    URL = "https://effective-mobile.ru/"

    @allure.step("Открыть главную страницу")
    def open(self):
        super().open(self.URL)
        return self

    @allure.step("Переход: О нас")
    def click_about(self):
        self.click(L.NAV_ABOUT)
