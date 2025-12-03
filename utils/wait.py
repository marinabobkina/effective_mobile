from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait_for(driver, condition, timeout=10):
    return WebDriverWait(driver, timeout).until(condition)


def clickable(locator):
    return EC.element_to_be_clickable(locator)


def visible(locator):
    return EC.visibility_of_element_located(locator)


def url_contains(part):
    return EC.url_contains(part)
