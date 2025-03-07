from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_unique_email
import locators as loc
from data import REGISTRATION_DATA
from data import URLCollection


class TestRegistrationPage:
    # Тест успешной регистрации
    def test_successful_registration(self, driver, open_registration_page):
        driver.find_element(By.XPATH, loc.NAME_INPUT_FIELD).send_keys(REGISTRATION_DATA['name'])
        driver.find_element(By.XPATH, loc.REGISTRATION_EMAIL_INPUT_FIELD).send_keys(generate_unique_email())
        driver.find_element(By.XPATH, loc.REGISTRATION_PASSWORD_INPUT_FIELD).send_keys(REGISTRATION_DATA['password'])
        driver.find_element(By.XPATH, loc.REGISTER_BUTTON).click()
        WebDriverWait(driver, 2).until(
            EC.url_to_be(URLCollection.LOGIN_PAGE)
        )

        assert driver.current_url == URLCollection.LOGIN_PAGE

    # Проверка невозможности регистрации при несоответствии пароля требованиям
    def test_invalid_password_registration_failed(self, driver, open_registration_page):
        driver.find_element(By.XPATH, loc.NAME_INPUT_FIELD).send_keys(REGISTRATION_DATA['name'])
        driver.find_element(By.XPATH, loc.REGISTRATION_EMAIL_INPUT_FIELD).send_keys(REGISTRATION_DATA['email'])
        driver.find_element(By.XPATH, loc.REGISTRATION_PASSWORD_INPUT_FIELD).send_keys('qwer')
        driver.find_element(By.XPATH, loc.REGISTER_BUTTON).click()

        actual_result = driver.find_element(By.XPATH, loc.INVALID_PASSWORD_MESSAGE)
        assert actual_result.text == 'Некорректный пароль'

    # Проверка невозможности регистрации если поле Name пустое
    def test_no_name_registration_failed(self, driver, open_registration_page):
        driver.find_element(By.XPATH, loc.REGISTRATION_EMAIL_INPUT_FIELD).send_keys(REGISTRATION_DATA['email'])
        driver.find_element(By.XPATH, loc.REGISTRATION_PASSWORD_INPUT_FIELD).send_keys(REGISTRATION_DATA['password'])
        driver.find_element(By.XPATH, loc.REGISTER_BUTTON).click()

        assert driver.current_url == URLCollection.REGISTRATION_PAGE

    # Проверка невозможности регистрации если указан некорректный Email
    def test_incorrect_email_registration_failed(self, driver, open_registration_page):
        driver.find_element(By.XPATH, loc.NAME_INPUT_FIELD).send_keys(REGISTRATION_DATA['name'])
        driver.find_element(By.XPATH, loc.REGISTRATION_EMAIL_INPUT_FIELD).send_keys('anton_shikunov_')
        driver.find_element(By.XPATH, loc.REGISTRATION_PASSWORD_INPUT_FIELD).send_keys(REGISTRATION_DATA['password'])
        driver.find_element(By.XPATH, loc.REGISTER_BUTTON).click()

        assert driver.current_url == URLCollection.REGISTRATION_PAGE
