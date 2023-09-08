import time

from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from src.locators import SearchLocators, ImagesLocators


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_element(self, key, time=120):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(key),
                                                      message=f'No key word {key}')

    def find_elements(self, key, time=120):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(key),
                                                      message=f'No key word {key}')

    def is_visible(self, key, time=120):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(key),
                                                      message=f'No key word {key}')

    def is_present(self, key, time=120):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(key),
                                                      message=f'No key word {key}')

    def open(self):
        return self.driver.get(self.url)


class SearchPage(BasePage):

    def enter_word(self, word):
        search_field = self.find_element(SearchLocators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        self.is_visible(SearchLocators.SUGGEST)
        search_field.send_keys(Keys.ENTER)

    def results(self):
        links = self.driver.find_elements(*SearchLocators.LINKS)
        link = links[0].get_attribute('href')
        return link


class ImagePage(BasePage):
    def menu(self):
        self.find_element(SearchLocators.SEARCH_FIELD).click()
        services = self.find_element(ImagesLocators.ALL_SERVICES)
        services.click()
        links = self.driver.find_elements(*ImagesLocators.IMAGES)
        images_link = list(filter(lambda x: x.get_attribute('href') == 'https://ya.ru/images/', links))
        images_link[0].click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert 'https://ya.ru/images/' in self.driver.current_url
        time.sleep(2)

    def choose_category(self):
        category = self.driver.find_elements(*ImagesLocators.CATEGORY)
        category_link = list(
            filter(lambda x: x.get_attribute('href') and 'https://ya.ru/images/search' in x.get_attribute('href'),
                   category))
        category_name = category_link[0].text
        category_link[0].click()
        category_text = self.driver.find_element(*ImagesLocators.CATEGORY_TEXT)
        assert category_text.get_attribute('value') == category_name

    def picture(self):
        time.sleep(2)
        pictures = self.driver.find_elements(*ImagesLocators.PICTURE)
        time.sleep(2)
        pictures[0].click()
        assert self.is_present(ImagesLocators.PICTURE_WINDOW)
        time.sleep(2)
