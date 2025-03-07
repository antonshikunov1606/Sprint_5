from selenium.webdriver.common.by import By
import locators as loc


class TestConstructorPage:
    # Проверка перехода в раздел "Булки"
    def test_successful_navigation_to_buns_section(self, driver, open_main_page):
        driver.find_element(By.XPATH, loc.SAUCES_BUTTON).click()
        driver.find_element(By.XPATH, loc.BUNS_BUTTON).click()
        element = driver.find_element(By.XPATH, loc.BUNS_SECTION)
        driver.execute_script(loc.ELEMENT_TO_SCROLL_VIEW, element)

        assert element.text == 'Булки'

    # Проверка перехода в раздел "Соусы"
    def test_successful_navigation_to_sauses_section(self, driver, open_main_page):
        driver.find_element(By.XPATH, loc.SAUCES_BUTTON).click()
        element = driver.find_element(By.XPATH, loc.SAUCES_SECTION)
        driver.execute_script(loc.ELEMENT_TO_SCROLL_VIEW, element)

        assert element.text == 'Соусы'

    # Проверка перехода в раздел "Начинки"
    def test_successful_navigation_to_fillings_section(self, driver, open_main_page):
        driver.find_element(By.XPATH, loc.FILLINGS_BUTTON).click()
        element = driver.find_element(By.XPATH, loc.FILLINGS_SECTION)
        driver.execute_script(loc.ELEMENT_TO_SCROLL_VIEW, element)

        assert element.text == 'Начинки'
