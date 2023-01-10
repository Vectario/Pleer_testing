from datetime import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current URL', get_url)

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Checks out')

    def make_screenshot(self):
        now_date = datetime.utcnow().strftime('%Y.%m.%d.%H.%M.$S')
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(f'C:\\Users\\Aleksander\\PycharmProjects\\SeleniumFinal\\screenshots\\{name_screenshot}')

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result

