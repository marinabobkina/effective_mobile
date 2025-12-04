Проект автотестов UI для сайта effective-mobile.ru (PyTest + Selenium + Allure)

Коротко
- Язык/рантайм: Python 3.10
- Тестовый фреймворк: PyTest
- UI: Selenium 4 (Chrome, headless)
- Отчёты: Allure (плагин allure-pytest, папка результатов allure_results)
- Паттерн: Page Object
- Docker: готовый Dockerfile для локального/удалённого запуска тестов


Структура проекта
```
effective_mobile/
├─ tests/
│  └─ test_home_nav.py           # Тесты навигации главной страницы
├─ pages/
│  ├─ base_page.py               # Базовые методы (клик, ожидания, скролл)
│  └─ home_page.py               # PageObject главной страницы
├─ locators/
│  └─ home_locators.py           # Локаторы меню/секций
├─ utils/
│  └─ wait.py                    # Обёртки WebDriverWait + Expected Conditions
├─ data/
│  └─ urls.py                    # Базовый URL и ожидания частей URL
├─ conftest.py                   # Фикстура driver (Chrome headless)
├─ pytest.ini                    # Конфиг PyTest (allure_results и опции)
├─ requirements.txt              # Зависимости проекта
├─ Dockerfile                    # Образ для запуска тестов
└─ README.md                     # Этот файл
```


Что проверяют тесты сейчас
Файл tests/test_home_nav.py содержит два параметризованных набора:
- test_navigation_links — клик по пунктам/блокам и проверка, что текущий URL содержит ожидаемую якорь/путь (about, contact, services и т.п.).
- test_navigation_sections — клик по пунктам/блокам и проверка, что соответствующая секция появилась/видима на странице (по ID секции).

Вспомогательные возможности
- pages/base_page.py: методы click с явными ожиданиями кликабельности, visibility для ожидания видимости, should_url_contain для проверки URL, scroll_to_footer для прокрутки к футеру (поддержка «бесконечной» подгрузки через ActionChains).
- utils/wait.py: функции-условия для WebDriverWait (clickable, visible, url_contains и т.д.).


Требования к окружению
- Python 3.10
- Google Chrome (локально не обязателен, если используете Docker)
- Allure Commandline для просмотра отчётов (устанавливается на хост-машине):
  - Windows: choco install allure или scoop install allure
  - macOS: brew install allure
  - Linux: через пакетный менеджер или с GitHub Releases


Установка и запуск локально (без Docker)
1) Клонируйте репозиторий и создайте виртуальное окружение
   - Windows PowerShell:
     ```powershell
     python -m venv .venv
     .venv\Scripts\Activate.ps1
     ```
   - Linux/macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

2) Установите зависимости
   ```bash
   pip install -r requirements.txt
   ```

3) Запустите тесты
   ```bash
   pytest
   ```
   По умолчанию результаты Allure будут сохранены в каталоге allure_results (см. pytest.ini).

4) Посмотрите отчёт Allure
   ```bash
   allure serve allure_results
   ```

Примечания по локальному запуску
- В conftest.py Chrome запускается в headless-режиме и добавлены стабильные флаги для контейнеров/CI: --no-sandbox и --disable-dev-shm-usage.
- Драйвер Chrome скачивается автоматически с помощью webdriver-manager.


Запуск в Docker

В проекте уже есть Dockerfile, который устанавливает Python 3.10, Google Chrome и зависимости, а затем запускает pytest в headless-режиме.

1) Сборка образа (в корне проекта):
   - Windows PowerShell:
     ```powershell
     docker build -t effective-mobile-tests:py310 .
     ```
   - Linux/macOS:
     ```bash
     docker build -t effective-mobile-tests:py310 .
     ```

2) Запуск контейнера с монтированием результатов Allure и кеша драйверов:
   - Windows PowerShell:
     ```powershell
     docker run --rm --shm-size=2g \
       -v ${PWD}\allure_results:/app/allure_results \
       -v ${PWD}\.wdm:/wdm \
       effective-mobile-tests:py310
     ```
   - Linux/macOS:
     ```bash
     docker run --rm --shm-size=2g \
       -v "$(pwd)/allure_results:/app/allure_results" \
       -v "$(pwd)/.wdm:/wdm" \
       effective-mobile-tests:py310
     ```

3) Открыть отчёт Allure на хосте:
   ```bash
   allure serve allure_results
   ```

Передача дополнительных аргументов pytest при запуске контейнера
```bash
docker run --rm \
  -v "$(pwd)/allure_results:/app/allure_results" \
  effective-mobile-tests:py310 \
  bash -lc "pytest -k navigation --maxfail=1 --alluredir=allure_results"
```


Лучшие практики, использованные в проекте
- Page Object изолирует работу с DOM от тестов.
- Явные ожидания через utils/wait.py (никаких sleep).
- Параметризация тестов для покрытия однотипных сценариев.
- Отчёты Allure: шаги и автоматические вложения можно расширить при необходимости.

