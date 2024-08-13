from selenium.webdriver.common.by import By


class Login:
    login_email = (By.XPATH, ".//label[text()='Email']/../input")  # Поле с вводом электронной почты при входе в аккаунт
    login_pass = (By.XPATH, ".//label[text()='Пароль']/../input")  # Поле с вводом пароля при входе в аккаунт
    login_button = (By.XPATH, ".//button[text()='Войти']")  # Кнопка "Войти"
    login_text = (By.XPATH, ".//*[text()='Вход']")  # Текст над формой авторизации
    login_button_main_page = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"


class Main:
    main_order_button = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка "Оформить заказ"
    main_personal_account = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка "Личный кабинет"
    main_profile = (By.XPATH, ".//a[text()= 'Профиль']")  # Кнопка "Профиль"
    main_constructor = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка "Конструктор"
    main_burger_text = (By.XPATH, ".//h1[text()='Соберите бургер']")  # Текст "Соберите бургер" на главной странице
    main_logo_button = (By.XPATH, ".//div[@class='AppHeader_header__logo__2D0X2']")  # Логотип
    main_logout_button = (By.XPATH, ".//button[text()='Выход']")  # Кнопка "Выход" в личном кабинете

    main_filling_button = (By.XPATH, ".//span[text()='Начинки']/parent::*")  # Кнопка "Начинки"
    # Текст "Начинки"
    main_filling_text = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")

    main_sauce_button = (By.XPATH, ".//span[text()='Соусы']/parent::*")  # Кнопка "Соусы"
    # Текст "Соусы"
    main_sauce_text = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")

    main_bun_button = (By.XPATH, ".//span[text()='Булки']/parent::*")  # Кнопка "Булки"
    # Текст "Булки"
    main_bun_text = (By.XPATH, ".//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")


class Registration:
    reg_name = (By.XPATH, ".//label[text()='Имя']/../input")  # Поле с вводом имени при регистрации аккаунта
    reg_button = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка "Зарегистрироваться"
    reg_pswd_error = (By.XPATH, ".//p[text()='Некорректный пароль']")  # Надпись "Некорректный пароль"
    reg_login_button = (By.XPATH, ".//a[text()='Войти']")  # Кнопка "Войти" под формой регисрации
