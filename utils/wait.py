"""Утилиты ожиданий поверх Selenium `WebDriverWait` и `expected_conditions`.

Содержит короткие обёртки для часто используемых условий: кликабельность,
видимость, наличие в DOM и проверка части URL.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for(driver, condition, timeout=10, message=None):
    """Дождаться выполнения условия через 'WebDriverWait' и вернуть его результат.

        :param driver: экземпляр Selenium 'WebDriver'
        :param condition: функция/условие из 'expected_conditions', принимающая драйвер
        :param timeout: максимальное время ожидания (секунды)
        :param message: сообщение об ошибке при таймауте
        :return: значение, возвращённое условием ('WebElement' или 'True'/'False')
        """
    return WebDriverWait(driver, timeout).until(condition, message=message)


def clickable(locator):
    """Условие кликабельности элемента по локатору."""
    return EC.element_to_be_clickable(locator)


def visible(locator):
    """Условие видимости элемента по локатору."""
    return EC.visibility_of_element_located(locator)


def url_contains(part):
    """Условие: текущий URL содержит подстроку 'part'."""
    return EC.url_contains(part)

def presence(locator):
    """Условие присутствия элемента в DOM (не обязательно видим)."""
    return EC.presence_of_element_located(locator)
