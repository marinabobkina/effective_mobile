import allure
import pytest
from pages.home_page import HomePage
from locators import home_locators as L
from data import urls


@allure.epic("Главная страница")
@allure.feature("Навигация по блокам")
class TestHomeNavigation:
    @allure.title("Проверка наличия в url якорной ссылки, привязанной к выбранному блоку")
    @pytest.mark.parametrize(
        "locator, expected_part",
        [
            pytest.param(L.NAV_ABOUT, urls.ABOUT, id="about us"),
            pytest.param(L.NAV_VACANCIES, urls.VACANCIES, id="vacancies"),
            pytest.param(L.NAV_REVIEWS, urls.REVIEWS, id="reviews"),
            pytest.param(L.NAV_CONTACTS, urls.CONTACTS, id="contacts"),
            pytest.param(L.NAV_AUTSTAFF, urls.AUTSTAFF, id="autstaff"),
            pytest.param(L.NAV_EMPLOYMENT, urls.EMPLOYMENT, id="employment"),
            pytest.param(L.NAV_CONSULTATION, urls.CONSULTATION, id="consultation")
        ]
    )
    def test_navigation_links(self, driver, locator, expected_part):
        page = HomePage(driver).open()
        page.wait_visibility_home_page_title()
        page.scroll_to_footer()
        page.click(locator)
        page.should_url_contain(expected_part)


    @allure.title("Проверка перехода в раздел, соответствующий выбранному блоку")
    @pytest.mark.parametrize(
        "locator, expected_part",
        [
            pytest.param(L.NAV_ABOUT, L.SECTION_ABOUT, id="about us"),
            pytest.param(L.NAV_VACANCIES, L.SECTION_VACANCIES, id="vacancies"),
            pytest.param(L.NAV_REVIEWS, L.SECTION_REVIEWS, id="reviews"),
            pytest.param(L.NAV_CONTACTS, L.SECTION_CONTACTS, id="contacts"),
            pytest.param(L.NAV_AUTSTAFF, L.SECTION_AUTSTAFF, id="autstaff"),
            pytest.param(L.NAV_EMPLOYMENT, L.SECTION_EMPLOYMENT, id="employment"),
            pytest.param(L.NAV_CONSULTATION, L.SECTION_CONSULTATION, id="consultation")
        ]
    )
    def test_navigation_sections(self, driver, locator, expected_part):
        page = HomePage(driver).open()
        page.wait_visibility_home_page_title()
        page.scroll_to_footer()
        page.click(locator)
        page.visibility(expected_part)
