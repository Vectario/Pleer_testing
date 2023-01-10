import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.main_page import MainPage
from pages.catalogue_page import CataloguePage
from pages.checkout_page import CheckoutPage


@pytest.mark.run(order=3)
def test_buy_processor(set_up):  # Buys a single processor
    s = Service('C:\\Users\\Aleksander\\PycharmProjects\\Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    mm = MainPage(driver)
    print('Test started: trying to buy processors', end=' --- ')
    mm.start_test_processors()
    cp = CataloguePage(driver)
    entries = cp.selection_processor()
    bp = CheckoutPage(driver)
    bp.verification(entries)
    driver.close()


@pytest.mark.run(order=2)
def test_buy_phone(set_up):  # Buys a single phone
    s = Service('C:\\Users\\Aleksander\\PycharmProjects\\Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    mm = MainPage(driver)
    mm.start_test_phones()
    cp = CataloguePage(driver)
    entries = cp.selection_phone()
    bp = CheckoutPage(driver)
    bp.verification(entries)
    driver.close()


@pytest.mark.run(order=1)
def test_buy_several_phones(set_up):  # Buys several phones
    s = Service('C:\\Users\\Aleksander\\PycharmProjects\\Selenium\\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    mm = MainPage(driver)
    mm.start_test_phones()
    cp = CataloguePage(driver)
    entries = cp.selection_phones()
    bp = CheckoutPage(driver)
    bp.verification(entries)
    driver.close()
