from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators as loc
from data import URLCollection


class TestNavigationPanel:
    # Проверка перехода по клику на «Личный кабинет»
    def test_successful_navigate_to_personal_account(self, driver, open_main_page):
        driver.find_element(By.XPATH, loc.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 2).until(
            EC.url_to_be(URLCollection.LOGIN_PAGE)
        )

        assert driver.current_url == URLCollection.LOGIN_PAGE

    # Проверка перехода по клику на «Личный кабинет»
    def test_successful_navigate_from_personal_account_to_constructor(self, driver, open_main_page):
        driver.find_element(By.XPATH, loc.ACCOUNT_BUTTON).click()
        driver.find_element(By.XPATH, loc.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 2).until(
            EC.url_to_be(URLCollection.HOME_PAGE)
        )

        assert driver.current_url == URLCollection.HOME_PAGE
