from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class MainPage(Base):
    url = 'https://www.pleer.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    menu = '//a[@class="navbar__button button button-gradient js-navbar-btn"]'
    menu_co = '//div[@class="catalog-list"]//span[text()="Компьютерное, сетевое и офисное оборудование"]'
    menu_phone = '//div[@class="catalog-list"]//span[text()="Телефоны, планшеты, ноутбуки, фотоаппараты и портативная техника"] '
    processors = '//div[@class="catalog__box js-nav-tabs-container"]//span[text()="Процессоры"]'
    phones = '//div[@class="catalog__box js-nav-tabs-container"]//span[text()="Сотовые / мобильные телефоны, ' \
             'смартфоны"] '

    # Getters

    def get_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu)))

    def get_menu_co(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_co)))

    def get_menu_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_phone)))

    def get_processors(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.processors)))

    def get_phones(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phones)))

    # Actions

    def open_menu(self):
        self.get_menu().click()

    def open_menu_co(self):
        self.get_menu_co().click()

    def open_menu_phone(self):
        self.get_menu_phone().click()

    def start_test_processors(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.open_menu()
        self.open_menu_co()
        self.get_processors().click()

    def start_test_phones(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.open_menu()
        self.open_menu_phone()
        self.get_phones().click()
