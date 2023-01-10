import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as ec
from base.base_class import Base


class CataloguePage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators - common

    goods = '//*[@id="list_items"]/div'
    price_lower = '//input[@id="ft_price_min"]'
    price_upper = '//input[@id="ft_price_max"]'
    sort_options = '//*[@class="sort_select"]'
    reserve = '//*[contains(text(),"Оформить доставку или резерв ")]'
    top_name = '//div[@id="list_items"]/*[1]//span[@class="item_name"]'
    top_price = '//div[@id="list_items"]/*[1]//div[@class="product_buy_buttons"]/*[5]//span[@class="price_disk"]'

    # Locators - phone philters

    huawei_checkbox = '//input[@id="f_m_795"]/following-sibling::span'
    smartphone_checkbox = '//input[@id="f_t_3228"]/following-sibling::span'
    screen_checkbox = '//input[@id="f_t_3683462"]/following-sibling::span'
    cores_checkbox = '//input[@id="f_t_21329386"]/following-sibling::span'
    memory_checkbox = '//input[@id="f_t_12566665"]/following-sibling::span'
    drive_checkbox = '//input[@id="f_t_12566679"]/following-sibling::span'
    camera_checkbox = '//input[@id="f_t_21329402"]/following-sibling::span'
    sim_checkbox = '//input[@id="f_t_1368"]/following-sibling::span'
    net_checkbox = '//input[@id="f_t_1213"]/following-sibling::span'
    usb_checkbox = '//input[@id="f_t_7876490"]/following-sibling::span'
    color_checkbox = '//input[@id="f_t_5955"]/following-sibling::span'

    # Locators - processor philters

    intel_checkbox = '//input[@id="f_m_668"]/following-sibling::span'
    lga1200 = '//input[@id="f_t_116813678"]/following-sibling::span'
    buy_button = '//div[@id="list_items"]/*[1]//div[@class="product_buy_buttons"]/*[5]//div[@class="buy_button "]'

    # Getters - common

    def get_lower(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.price_lower)))

    def get_upper(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.price_upper)))

    def get_reserve(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.reserve)))

    def get_top_name(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.top_name)))

    def get_top_price(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.top_price)))

    # Getters - processors

    def get_intel(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.intel_checkbox)))

    def get_lga1200(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.lga1200)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.buy_button)))

    # Getters - phones

    def get_huawei(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.huawei_checkbox)))

    def get_smartphone(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.smartphone_checkbox)))

    def get_screen(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.screen_checkbox)))

    def get_cores(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.cores_checkbox)))

    def get_memory(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.memory_checkbox)))

    def get_drive(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.drive_checkbox)))

    def get_camera(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.camera_checkbox)))

    def get_sim(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.sim_checkbox)))

    def get_network(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.net_checkbox)))

    def get_usb(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.usb_checkbox)))

    def get_color(self):
        return WebDriverWait(self.driver, 5).until(ec.presence_of_element_located((By.XPATH, self.color_checkbox)))

    # Actions

    def price_cut(self):  # Extracts the actual price from the string
        return int(''.join((self.get_top_price().text.split(' руб.')[0]).split()))

    def name_retrieval(self, i):  # Gets the product name
        return self.driver.find_element(By.XPATH, f'//*[@id="list_items"]/*[{i}]/*[2]//span[@class="item_name"]').text

    def price_retrieval(self, i=1):  # Gets the product price
        k = f'//div[@id="list_items"]/*[{i}]//div[@class="product_buy_buttons"]/*[5]//span[@class="price_disk"]'
        tmp = self.driver.find_element(By.XPATH, k)
        return int(''.join((tmp.text.split(' руб.')[0]).split()))

    def press_buy(self, i):  # Presses the checkout button
        tmp = f'//*[@id="list_items"]/*[{i}]/*[2]/*[2]/*[5]//div[@class="buy_button "]'
        element = self.driver.find_element(By.XPATH, tmp)
        self.driver.execute_script("arguments[0].click();", element)

    def buy_algorythm(self, m):  # Add top m products that satisfy the criteria to cart and return {name: price} dict
        keys = []
        values = []
        for i in range(1, m):
            time.sleep(2)
            values.append(self.price_retrieval(i))
            keys.append(self.name_retrieval(i))
            self.press_buy(i)
            time.sleep(2)
            if i == m-1:
                self.get_reserve().click()
            else:
                self.driver.find_element(By.XPATH, '//div[text()="продолжить покупки"]').click()
        return dict(zip(keys, values))

    def selection_processor(self):
        # Puts the newest processor that fits our criteria into the cart,
        # returns its parameters and enters the checkout page
        print('Processor selection started', end=' --- ')
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.execute_script("window.scrollTo(0, 300)")
        print('Moved', end=' --- ')
        select = Select(self.driver.find_element(By.XPATH, self.sort_options))
        select.select_by_visible_text('Сначала новинки')
        print('Sorted', end=' --- ')
        time.sleep(2)
        self.get_lower().send_keys(18000)
        self.get_upper().send_keys(28000)
        print('Keys sent', end=' --- ')
        time.sleep(2)  # Unfortunately, the filters don't want to work with implicit timers.
        self.get_intel().click()
        print('Intel selected', end=' --- ')
        time.sleep(2)
        self.get_lga1200().click()
        print('LGA entered', end=' --- ')
        time.sleep(2)
        entries = self.buy_algorythm(2)
        print('Selection stage complete')
        return entries

    def selection_phone(self):
        # Puts the newest phone that fits our criteria into the cart and returns its parameters
        print('Phone selection started', end=' --- ')
        self.driver.switch_to.window(self.driver.window_handles[1])
        select = Select(self.driver.find_element(By.XPATH, self.sort_options))
        select.select_by_visible_text('Сначала новинки')
        print('Sorted', end=' --- ')
        time.sleep(2)
        self.get_lower().send_keys(7000)
        self.get_upper().send_keys(18000)
        print('Keys sent', end=' --- ')
        time.sleep(2)  # Unfortunately, the filters don't seem to want to work with implicit timers.
        self.get_huawei().click()
        print('Huawei', end=' --- ')
        time.sleep(2)
        self.get_smartphone().click()
        print('Smartphone', end=' --- ')
        time.sleep(2)
        self.get_sim().click()
        print('Double SIM', end=' --- ')
        time.sleep(2)
        self.get_camera().click()
        print('3 cameras', end=' --- ')
        time.sleep(2)
        self.get_drive().click()
        print('128GB memory', end=' --- ')
        time.sleep(2)
        self.get_memory().click()
        print('4GB RAM', end=' --- ')
        time.sleep(2)
        entries = self.buy_algorythm(2)
        print('Selection stage complete')
        return entries

    def selection_phones(self):
        # Puts three most popular phones that fit our criteria into the cart and returns their parameters
        print('Phones selection started', end=' --- ')
        self.driver.switch_to.window(self.driver.window_handles[1])
        select = Select(self.driver.find_element(By.XPATH, self.sort_options))
        select.select_by_visible_text('Сначала популярные')
        print('Sorted', end=' --- ')
        time.sleep(2)
        self.get_lower().send_keys(7000)
        self.get_upper().send_keys(18000)
        print('Keys sent', end=' --- ')
        time.sleep(2)  # Unfortunately, the filters don't seem to want to work with implicit timers.
        self.get_huawei().click()
        print('Huawei', end=' --- ')
        time.sleep(2)
        self.get_smartphone().click()
        print('Smartphone', end=' --- ')
        time.sleep(2)
        self.get_sim().click()
        print('Double SIM', end=' --- ')
        time.sleep(2)
        self.get_camera().click()
        print('3 cameras', end=' --- ')
        time.sleep(2)
        self.get_drive().click()
        print('128GB memory', end=' --- ')
        time.sleep(2)
        self.get_memory().click()
        print('4GB RAM', end=' --- ')
        time.sleep(2)
        tmp = len(self.driver.find_elements(By.XPATH, self.goods))
        if tmp < 2:
            entries = self.buy_algorythm(tmp+1)
        else:
            entries = self.buy_algorythm(3)
        print('Selection stage complete')
        return entries
