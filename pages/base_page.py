"""
Базовые действия для Page Object: открытие URL, скролл, ожидание видимости и клики.
Методы инкапсулируют ожидания и выбрасывают осмысленные AssertionError для удобства в тестах.
"""

import time
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from utils.wait import wait_for, clickable, url_contains, visible
from locators import home_locators as L


class BasePage:
    def __init__(self, driver):
        """Сохраняет экземпляр WebDriver для дальнейших действий на странице."""
        self.driver = driver

    @allure.step("Открыть URL: {url}")
    def open(self, url: str):
        """Открытие указанного URL и возврат текущего объекта класса."""
        self.driver.get(url)
        return self

    @allure.step("Прокрутка страницы к footer")
    def scroll_to_footer(self, timeout = 30, step = 1400, pause = 0.4):
        """
        Прокручивает страницу до футера и возвращает найденный элемент footer.
        :param timeout: максимальное время ожидания в секундах
        :param step: величина прокрутки за один шаг (в пикселях)
        :param pause: пауза между шагами прокрутки (в секундах)
        :raises TimeoutException: если футер не найден за отведённое время
        :return: элемент футера
        """
        actions = ActionChains(self.driver)
        end = time.time() + timeout
        last_height = 0

        while time.time() < end:
            els = self.driver.find_elements(*L.FOOTER)
            if els:
                actions.scroll_to_element(els[0]).perform()
                return els[0]

            actions.scroll_by_amount(0, step).perform()
            time.sleep(pause)

            new_height = self.driver.execute_script(
                "return document.documentElement.scrollHeight"
            )
            if new_height == last_height:
                break
            last_height = new_height

        raise TimeoutException("Footer не найден или бесконечная лента без футера")

    @allure.step("Ожидать видимость элемента")
    def visibility(self, locator: tuple):
        """Ждёт видимость элемента по локатору и возвращает его, иначе бросает AssertionError."""
        try:
            return wait_for(
                self.driver,
                visible(locator),
                message=f"{locator} не найден"
            )
        except TimeoutException as e:
            raise AssertionError(f"{locator} не найден") from e


    @allure.step("Клик по элементу: {locator}")
    def click(self, locator: tuple):
        """Кликает по элементу, ожидая его кликабельность, и возвращает этот элемент."""
        try:
            el = wait_for(
                self.driver,
                clickable(locator),
                message=f"Элемент {locator} некликабелен"
            )
            el.click()
            return el
        except TimeoutException as e:
            raise AssertionError(f"Элемент {locator} некликабелен") from e

    @allure.step("Ожидать URL содержит: {part}")
    def should_url_contain(self, part: str):
        """Ожидает, что текущий URL будет содержать подстроку `part`."""
        try:
            wait_for(
                self.driver,
                url_contains(part),
                message=f"URL не содержит {part}"
            )
        except TimeoutException:
            raise AssertionError(f"Ожидали, что URL содержит '{part}', но получили: {self.driver.current_url}")
