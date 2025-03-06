import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
    driver.get("https://stellarburgers.nomoreparties.site/")

    WebDriverWait(driver, 1).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo"))
    )

    yield driver


# Фикстура которая открывает страницу регистрации
# Так же фикстура содержит явное ожидание загрузки окна логина
@pytest.fixture
def open_registration_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey"))
    )

    yield driver


# Фикстура которая открывает страницу логина и авторизует пользователя
@pytest.fixture
def authorize_user(driver):
    driver.get("https://stellarburgers.nomoreparties.site/login")

    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey"))
    )

    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(
        'anton_shikunov_19998@yandex.ru')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input[@name="Пароль"]').send_keys('qwerty')
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo"))
    )

    yield driver
