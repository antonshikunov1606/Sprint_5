from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Тест входа по кнопке "Личный кабинет"
def test_successful_login_with_navigate_to_personal_account(open_main_page):
    driver = open_main_page

    driver.find_element(By.XPATH, './/div/header/nav/a/p').click()
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input').send_keys(
        'anton_shikunov_19998@yandex.ru')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input[@name="Пароль"]').send_keys('qwerty')
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo"))
    )

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


# Тест входа по кнопке «Войти в аккаунт»
def test_successful_login_clicking_the_button_to_login_to_your_account(open_main_page):
    driver = open_main_page

    driver.find_element(By.XPATH, './/button[text()="Войти в аккаунт"]').click()
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input[@name="name"]').send_keys(
        'anton_shikunov_19998@yandex.ru')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input[@name="Пароль"]').send_keys('qwerty')
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo"))
    )

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'


# Тест входа через кнопку "Войти" в форме регистрации
def test_successful_login_from_registration_page(open_registration_page):
    driver = open_registration_page

    driver.find_element(By.CLASS_NAME, 'Auth_link__1fOlj').click()
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "Auth_login__3hAey"))
    )
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input[@name="name"]').send_keys(
        'anton_shikunov_19998@yandex.ru')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input[@name="Пароль"]').send_keys('qwerty')
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo"))
    )

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

# Тест входа через кнопку "Восстановить пароль"
def test_successful_login_clicking_the_button_recover_password(open_main_page):
    driver = open_main_page

    driver.find_element(By.XPATH, './/button[text()="Войти в аккаунт"]').click()
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey"))
    )
    driver.find_element(By.XPATH, './/a[text()="Восстановить пароль"]').click()
    driver.find_element(By.XPATH, './/a[text()="Войти"]').click()
    driver.find_element(By.XPATH, './/fieldset[1]/div/div/input[@name="name"]').send_keys(
        'anton_shikunov_19998@yandex.ru')
    driver.find_element(By.XPATH, './/fieldset[2]/div/div/input[@name="Пароль"]').send_keys('qwerty')
    driver.find_element(By.XPATH, './/button[text()="Войти"]').click()
    WebDriverWait(driver, 2).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "BurgerIngredients_ingredients__menuContainer__Xu3Mo"))
    )

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
