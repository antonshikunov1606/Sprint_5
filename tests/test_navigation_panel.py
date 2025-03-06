from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Проверка перехода по клику на «Личный кабинет»
def test_successful_navigate_to_personal_account(authorize_user):
    driver = authorize_user

    driver.find_element(By.XPATH, './/div/header/nav/a/p').click()
    WebDriverWait(driver, 2).until(
        EC.url_to_be(("https://stellarburgers.nomoreparties.site/account/profile"))
    )

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'


# Проверка перехода по клику на «Личный кабинет»
def test_successful_navigate_from_personal_account_to_constructor(authorize_user):
    driver = authorize_user

    driver.find_element(By.XPATH, './/nav/a/p').click()
    driver.find_element(By.XPATH, './/nav/ul/li[1]/a/p').click()
    WebDriverWait(driver, 2).until(
        EC.url_to_be(("https://stellarburgers.nomoreparties.site/"))
    )

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
