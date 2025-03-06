from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест успешной регистрации
def test_successful_registration(open_registration_page):
    driver = open_registration_page

    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input[@name="name"]').send_keys('Anton')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input[@name="name"]').send_keys('anton_shikunov_19998@yandex.ru')
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input[@type="password"]').send_keys('qwerty')
    driver.find_element(By.XPATH, '//button[contains(text(), "Зарегистрироваться")]').click()
    WebDriverWait(driver, 2).until(
        EC.url_to_be(("https://stellarburgers.nomoreparties.site/login"))
    )

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'


# Проверка невозможности регистрации при несоответствии пароля требованиям
def test_invalid_password_registration_failed(open_registration_page):
    driver = open_registration_page

    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input[@name="name"]').send_keys('Anton')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input[@name="name"]').send_keys('anton_shikunov_19998@yandex.ru')
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input[@type="password"]').send_keys('qwer')
    driver.find_element(By.XPATH, '//button[contains(text(), "Зарегистрироваться")]').click()

    actual_result = driver.find_element(By.XPATH, './/p[contains(text(), "Некорректный пароль")]')
    assert actual_result.text == 'Некорректный пароль'


# Проверка невозможности регистрации если поле Name пустое
def test_no_name_registration_failed(open_registration_page):
    driver = open_registration_page

    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input[@name="name"]').send_keys('anton_shikunov_19998@yandex.ru')
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input[@type="password"]').send_keys('qwerty')
    driver.find_element(By.XPATH, '//button[contains(text(), "Зарегистрироваться")]').click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'


# Проверка невозможности регистрации если указан некорректный Email
def test_incorrect_email_registration_failed(open_registration_page):
    driver = open_registration_page

    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input[@name="name"]').send_keys('Anton')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input[@name="name"]').send_keys('anton_shikunov_')
    driver.find_element(By.XPATH, './/fieldset[3]/div/div/input[@type="password"]').send_keys('qwerty')
    driver.find_element(By.XPATH, '//button[contains(text(), "Зарегистрироваться")]').click()

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/register'
