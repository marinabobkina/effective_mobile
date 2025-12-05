"""Page Object главной страницы: действия открытия и базовых проверок."""


import allure
from pages.base_page import BasePage
from locators import home_locators as L
from data import urls


class HomePage(BasePage):
    """
    Страница «Главная».
    Содержит высокоуровневые шаги работы с главной страницей сайта.
    """

    @allure.step("Открыть главную страницу")
    def open(self):
        """
        Открывает главную страницу и возвращает текущий Page Object.
            :return: текущий экземпляр `HomePage` для дальнейшей цепочки действий.
        """
        super().open(urls.BASE)
        return self

    @allure.step("Ожидать видимость заголовка на главной странице")
    def wait_visibility_home_page_title(self):
        """Ожидает видимость заголовка на главной странице (элемент `L.PAGE_TITLE`)."""
        self.visibility(L.PAGE_TITLE)
