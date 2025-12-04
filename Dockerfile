FROM python:3.10

# Базовые ENV и кеш для webdriver-manager (чтобы не скачивать ChromeDriver каждый раз)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    WDM_LOCAL=1 \
    WDM_CACHE_DIR=/wdm

# Системные зависимости и либы для Chrome
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget gnupg ca-certificates unzip \
    fonts-liberation libasound2 libatk-bridge2.0-0 libatk1.0-0 \
    libgtk-3-0 libnss3 libx11-6 libxcomposite1 libxdamage1 libxext6 \
    libxfixes3 libxrandr2 libgbm1 libxshmfence1 libdrm2 libxkbcommon0 libxi6 \
    libgdk-pixbuf2.0-0 libu2f-udev \
    && rm -rf /var/lib/apt/lists/*

# Установка Google Chrome (stable)
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google-linux.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/google-linux.gpg] http://dl.google.com/linux/chrome/deb/ stable main" \
       > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /app

# Сначала зависимости (лучший кеш Docker-слоёв)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Затем код
COPY . .

# Каталоги для артефактов (результаты Allure и кеш драйверов)
RUN mkdir -p /app/allure_results /wdm

# Запуск тестов в headless (Xvfb для не headless-режима)
CMD ["pytest", "-v", "--tb=short", "--alluredir=allure_results"]
