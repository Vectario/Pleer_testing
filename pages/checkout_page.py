from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class CheckoutPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    cart = '//*[@id="cart_postform"]/div[1]/table/tbody'

    # Getters

    def get_cart(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.cart)))

    # Actions

    def cart_volume(self):
        # Gets the total number of products
        tmp = self.driver.find_elements(By.XPATH, f'{self.cart}/tr')
        return len(tmp) - 1

    def name_retrieval(self, i):
        # Gets the product name
        tmp = f'{self.cart}/tr[{i}]/td[2]/h1/a'
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, tmp))).text

    def price_retrieval(self, i):
        # Gets the product price
        tmp = f'{self.cart}/tr[{i}]/td[3]/span/span'
        return int(WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, tmp))).text)

    def verification(self, entries):
        # Verifies that the names-prices pairs are exactly the same as recorded in the previous step
        print(f'Verification started for {self.cart_volume()} product(s)', end=' --- ')
        print(f'{self.cart_volume()} entries in total', end=' --- ')
        assert self.cart_volume() == len(entries)
        price_total = 0
        for i in range(1, self.cart_volume()+1):
            print(f'Row {i}', end=' --- ')
            tmp = self.price_retrieval(i)
            print(f'Price = {tmp}', end=' --- ')
            assert self.name_retrieval(i) in entries.keys()
            assert entries[self.name_retrieval(i)] == tmp
            price_total += tmp
            print(f'Row checks out')
        assert price_total == sum(entries.values())
        print('Test successful')
