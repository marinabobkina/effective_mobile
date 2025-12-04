from selenium.webdriver.common.by import By


PAGE_TITLE = (By.XPATH, "//h1/span[text()= 'Ваша карьера в IT']")
FOOTER = (By.TAG_NAME, "footer")

# Блоки в разделе 'Компания'
NAV_ABOUT = (By.LINK_TEXT, "О нас")
NAV_VACANCIES = (By.LINK_TEXT, "Вакансии")
NAV_REVIEWS = (By.LINK_TEXT, "Отзывы")
NAV_CONTACTS = (By.LINK_TEXT, "Контакты")

# Блоки в разделе 'Услуги'
NAV_AUTSTAFF = (By.LINK_TEXT, "Аутстафф")
NAV_EMPLOYMENT = (By.LINK_TEXT, "Трудоустройство")
NAV_CONSULTATION = (By.LINK_TEXT, "Консультация")

# Секции, соответствующие блокам меню
SECTION_ABOUT = (By.ID, "about")
SECTION_VACANCIES = (By.ID, "specializations")
SECTION_REVIEWS = (By.ID, "testimonials")
SECTION_CONTACTS = (By.ID, "contact")

SECTION_AUTSTAFF = (By.ID, "services")
SECTION_EMPLOYMENT = (By.ID, "services")
SECTION_CONSULTATION = (By.ID, "contact")