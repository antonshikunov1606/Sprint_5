import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as loc
import data
from data import URLCollection


#  Фикстура для инициализации веб-драйвера Chrome, которая создает
#  экземпляр веб-драйвера Chrome, а после завершения тестов
#  драйвер корректно закрывается вызовом `driver.quit()`
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


# Фикстура которая открывает главную страницу сайта
# Так же фикстура содержит явное ожидание загрузки контейнера меню
@pytest.fixture
def open_main_page(driver):
    driver.get(URLCollection.HOME_PAGE)

    WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.XPATH, loc.INGREDIENTS_MENU_CONTAINER_CLASS))
    )


# Фикстура которая открывает страницу регистрации
# Так же фикстура содержит явное ожидание загрузки окна логина
@pytest.fixture
def open_registration_page(driver):
    driver.get(URLCollection.REGISTRATION_PAGE)

    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, loc.AUTH_REG_WINDOW_CLASS))
    )


# Фикстура которая открывает страницу логина и авторизует пользователя
@pytest.fixture
def authorize_user(driver):
    driver.get(URLCollection.LOGIN_PAGE)

    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.XPATH, loc.AUTH_REG_WINDOW_CLASS))
    )

    driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(
        data.REGISTRATION_DATA['email'])
    driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(data.REGISTRATION_DATA['password'])
    driver.find_element(By.XPATH, loc.LOGIN_BUTTON).click()
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located(
            (By.XPATH, loc.INGREDIENTS_MENU_CONTAINER_CLASS))
    )
