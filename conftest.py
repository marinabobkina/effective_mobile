"""Pytest-фикстуры для запуска браузерных тестов.

Содержит фикстуру `driver`, которая настраивает и предоставляет экземпляр
Selenium Chrome WebDriver для тестов. Драйвер запускается в headless-режиме,
с фиксированным размером окна и безопасными флагами для CI. Установка и
управление исполняемым драйвером хрома выполняются через `webdriver_manager`.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver(request):
    """Возвращает настроенный экземпляр Chrome WebDriver для тестов.

        Настройки:
        - `--window-size=1920,1080` — фиксированный размер окна;
        - `--headless` — безголовый режим (удобно для CI и контейнеров);
        - `--no-sandbox`, `--disable-dev-shm-usage` — флаги стабильности в ограниченных окружениях (добавлены для для CI).

        Порядок работы:
        1. Создаёт объект опций Chrome и применяет флаги запуска.
        2. Инициализирует драйвер с помощью `webdriver_manager` (скачивает подходящий ChromeDriver при необходимости).
        3. Передаёт драйвер в тест (через `yield`).
        4. После завершения теста корректно завершает сессию браузера (`driver.quit()`).

        :param request: объект `pytest.FixtureRequest` (необязательный, на будущее для параметризации/хуков).
        :yield: экземпляр `selenium.webdriver.Chrome`.
        """
    options = Options()
    options.add_argument(f"--window-size=1920,1080")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    yield driver
    driver.quit()
