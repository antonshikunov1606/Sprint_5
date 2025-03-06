from selenium.webdriver.common.by import By


# Проверка перехода в раздел "Булки"
def test_successful_navigation_to_buns_section(authorize_user):
    driver = authorize_user

    element = driver.find_element(By.XPATH, './/section[1]/div[2]/h2[1]')
    driver.execute_script('arguments[0].scrollIntoView()', element)

    assert element.text == 'Булки'


# Проверка перехода в раздел "Соусы"
def test_successful_navigation_to_sauses_section(authorize_user):
    driver = authorize_user

    driver.find_element(By.XPATH, './/section[1]/div[1]/div[2]').click()
    element = driver.find_element(By.XPATH, './/section[1]/div[2]/h2[2]')
    driver.execute_script('arguments[0].scrollIntoView()', element)

    assert element.text == 'Соусы'


# Проверка перехода в раздел "Начинки"
def test_successful_navigation_to_fillings_section(authorize_user):
    driver = authorize_user

    driver.find_element(By.XPATH, './/section[1]/div[1]/div[3]').click()
    element = driver.find_element(By.XPATH, './/section[1]/div[2]/h2[3]')
    driver.execute_script('arguments[0].scrollIntoView()', element)

    assert element.text == 'Начинки'
