from selenium.webdriver.common.by import By
import locators as loc
from data import REGISTRATION_DATA
from data import URLCollection
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLoginPage:
    # Тест входа по кнопке "Личный кабинет"
    def test_successful_login_with_navigate_to_personal_account(self, driver, open_main_page):
        driver.find_element(By.XPATH, loc.ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(
            REGISTRATION_DATA['email'])
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(REGISTRATION_DATA['password'])
        driver.find_element(By.XPATH, loc.LOGIN_BUTTON).click()
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, loc.INGREDIENTS_MENU_CONTAINER_CLASS))
        )

        assert driver.current_url == URLCollection.HOME_PAGE

    # Тест входа по кнопке «Войти в аккаунт»
    def test_successful_login_clicking_the_button_to_login_to_your_account(self, driver, open_main_page):
        driver.find_element(By.XPATH, loc.LOGIN_ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(
            REGISTRATION_DATA['email'])
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(REGISTRATION_DATA['password'])
        driver.find_element(By.XPATH, loc.LOGIN_BUTTON).click()
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(
                (By.XPATH, loc.INGREDIENTS_MENU_CONTAINER_CLASS))
        )

        assert driver.current_url == URLCollection.HOME_PAGE

    # Тест входа через кнопку "Войти" в форме регистрации
    def test_successful_login_from_registration_page(self, driver, open_registration_page):
        driver.find_element(By.XPATH, loc.REGISTER_BUTTON_LOCATOR_IN_LOGIN_MODAL).click()
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(
                (By.XPATH, loc.AUTH_REG_WINDOW_CLASS))
        )
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(
            REGISTRATION_DATA['email'])
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(REGISTRATION_DATA['password'])
        driver.find_element(By.XPATH, loc.LOGIN_BUTTON).click()
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(
                (By.XPATH, loc.INGREDIENTS_MENU_CONTAINER_CLASS))
        )

        assert driver.current_url == URLCollection.HOME_PAGE

    # Тест входа через кнопку "Восстановить пароль"
    def test_successful_login_clicking_the_button_recover_password(self, driver, open_main_page):
        driver.find_element(By.XPATH, loc.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, loc.AUTH_REG_WINDOW_CLASS))
        )
        driver.find_element(By.XPATH, loc.RECOVER_PASSWORD_BUTTON).click()
        driver.find_element(By.XPATH, loc.LOGIN_BUTTON_LOCATOR_IN_RECOVER_PASSWORD_MODAL).click()
        driver.find_element(By.XPATH, loc.LOGIN_EMAIL_INPUT_FIELD).send_keys(
            REGISTRATION_DATA['email'])
        driver.find_element(By.XPATH, loc.LOGIN_PASSWORD_INPUT_FIELD).send_keys(REGISTRATION_DATA['password'])
        driver.find_element(By.XPATH, loc.LOGIN_BUTTON).click()
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located(
                (By.XPATH, loc.INGREDIENTS_MENU_CONTAINER_CLASS))
        )

        assert driver.current_url == URLCollection.HOME_PAGE
