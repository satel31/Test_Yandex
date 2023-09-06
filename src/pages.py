from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from src.locators import SearchLocators


class BasePage:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def find_element(self, key, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_element_located(key),
                                                      message=f'No key word {key}')

    def find_elements(self, key, time=10):
        return WebDriverWait(self.driver, time).until(ec.presence_of_all_elements_located(key),
                                                      message=f'No key word {key}')

    def is_visible(self, key, time=10):
        return WebDriverWait(self.driver, time).until(ec.visibility_of_element_located(key),
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
