import allure
from pages.base_page import BasePage
from locators import home_locators as L
from data import urls


class HomePage(BasePage):
    @allure.step("Открыть главную страницу")
    def open(self):
        super().open(urls.BASE)
        return self

    @allure.step("Ожидать видимость заголовка на главной странице")
    def wait_visibility_home_page_title(self):
        self.visibility(L.PAGE_TITLE)
