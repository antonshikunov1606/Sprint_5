from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as loc
from data import URLCollection


class TestLogout:
    # Проверка выхода по кнопке «Выйти» в личном кабинете
    def test_successful_logout_from_personal_account(self, driver, authorize_user):
        driver.find_element(By.XPATH, loc.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 2).until(
            EC.url_to_be(URLCollection.PROFILE_PAGE)
        )
        driver.find_element(By.XPATH, loc.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, loc.AUTH_REG_WINDOW_CLASS))
        )

        assert driver.current_url == URLCollection.LOGIN_PAGE
