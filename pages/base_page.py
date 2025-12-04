import time
import allure
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from utils.wait import wait_for, clickable, url_contains, visible
from locators import home_locators as L


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открыть URL: {url}")
    def open(self, url: str):
        self.driver.get(url)
        return self

    @allure.step("Прокрутка страницы к footer")
    def scroll_to_footer(self, timeout = 30, step = 1400, pause = 0.4):
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
        try:
            wait_for(
                self.driver,
                url_contains(part),
                message=f"URL не содержит {part}"
            )
        except TimeoutException:
            raise AssertionError(f"Ожидали, что URL содержит '{part}', но получили: {self.driver.current_url}")
