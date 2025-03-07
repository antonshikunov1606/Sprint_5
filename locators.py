ACCOUNT_BUTTON = './/div/header/nav/a/p'  # Кнопка "Личный кабинет" в навигации
NAME_INPUT_FIELD = './/fieldset[1]//input[@type="text" and @name="name"]'  # Поле для ввода имени
REGISTRATION_EMAIL_INPUT_FIELD = './/fieldset[2]//input[@type="text" and @name="name"]'  # Поле для ввода Email в окне регистрации
REGISTRATION_PASSWORD_INPUT_FIELD = './/input[@type="password"]'  # Поле для ввода пароля в окне регистрации
REGISTER_BUTTON = '//button[contains(text(), "Зарегистрироваться")]'  # Кнопка "Зарегистрироваться"
INVALID_PASSWORD_MESSAGE = './/p[contains(text(), "Некорректный пароль")]'  # Элемент "Некорректный пароль" в окне регистрации
LOGIN_EMAIL_INPUT_FIELD = './/input[@type="text" and @name="name"]'  # Поле для ввода Email в окне авторизации
LOGIN_PASSWORD_INPUT_FIELD = './/input[@type="password" and @name="Пароль"]'  # Поле для ввода пароля в окне авторизации
LOGIN_BUTTON = './/button[text()="Войти"]'  # Кнопка "Войти" в окне авторизации
LOGOUT_BUTTON = './/button[text()="Выход"]'  # Кнопка "Выйти" в личном кабинете
LOGIN_ACCOUNT_BUTTON = './/button[text()="Войти в аккаунт"]' # Кнопка "Войти в аккаунт"
CONSTRUCTOR_BUTTON = './/p[@class="AppHeader_header__linkText__3q_va ml-2"]'  # Кнопка "Конструктор" в навигации
BUNS_BUTTON = './/div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]' # Кнопка "Булки"
BUNS_SECTION = './/h2[text()="Булки"]'  # Раздел "Булки"
SAUCES_BUTTON = './/div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]'  # Кнопка "Соусы"
SAUCES_SECTION = './/h2[text()="Соусы"]'  # Раздел "Соусы"
FILLINGS_BUTTON = './/div[@class="tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect"]'  # Кнопка "Начинки"
FILLINGS_SECTION = './/h2[text()="Начинки"]'  # Раздел "Начинки"
INGREDIENTS_MENU_CONTAINER_CLASS = './/div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]'  # Класс контейнера меню ингредиентов
AUTH_REG_WINDOW_CLASS = './/div[@class="Auth_login__3hAey"]'  # Класс окна авторизации и регистрации
REGISTER_BUTTON_LOCATOR_IN_LOGIN_MODAL = './/a[@class="Auth_link__1fOlj"]' # Кнопка "Зарегистрироваться" в окне авторизации
RECOVER_PASSWORD_BUTTON = './/a[text()="Восстановить пароль"]' # Кнопка "Восстановить пароль"
LOGIN_BUTTON_LOCATOR_IN_RECOVER_PASSWORD_MODAL = './/a[text()="Войти"]' # Кнопка "Войти" в окне восстановления пароля
ELEMENT_TO_SCROLL_VIEW = 'arguments[0].scrollIntoView()' # Метод для прокрутки веб-страницы до определённого элемента в DOM
