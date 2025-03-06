from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Проверка выхода по кнопке «Выйти» в личном кабинете
def test_successful_logout_from_personal_account(authorize_user):
    driver = authorize_user

    driver.find_element(By.XPATH, './/div/header/nav/a/p').click()
    WebDriverWait(driver, 2).until(
        EC.url_to_be(("https://stellarburgers.nomoreparties.site/account/profile"))
    )
    driver.find_element(By.XPATH, './/button[text()="Выход"]').click()
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey"))
    )

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
