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

    def search_field(self):
        assert self.is_present(SearchLocators.SEARCH_FIELD), "Нет поля для поиска на странице"

    def enter_word(self, word):
        search_field = self.find_element(SearchLocators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        assert self.is_visible(SearchLocators.SUGGEST), "Нет таблицы с подсказками"
        search_field.send_keys(Keys.ENTER)

    def results(self):
        links = self.find_elements(SearchLocators.LINKS)
        link = links[0].get_attribute('href')
        return link


class ImagePage(BasePage):
    def menu(self):
        self.find_element(SearchLocators.SEARCH_FIELD).click()
        assert self.is_present(ImagesLocators.ALL_SERVICES), "Нет меню с сервисами на главной странице"
        services = self.find_element(ImagesLocators.ALL_SERVICES)
        services.click()
        links = self.find_elements(ImagesLocators.IMAGES)
        images_link = list(filter(lambda x: x.get_attribute('href') == 'https://ya.ru/images/', links))
        images_link[0].click()
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        assert 'https://ya.ru/images/' in self.driver.current_url, "Не перешли на url https://ya.ru/images/"

    def choose_category(self):
        category = self.find_elements(ImagesLocators.CATEGORY)
        category_link = list(
            filter(lambda x: x.get_attribute('href') and 'https://ya.ru/images/search' in x.get_attribute('href'),
                   category))
        category_name = category_link[0].text
        category_link[0].click()
        category_text = self.find_element(ImagesLocators.CATEGORY_TEXT)
        assert category_text.get_attribute('value') == category_name, "В поле поиска отсутствует название категории или название категории не верное"


    def picture(self):
        pictures = self.find_elements(ImagesLocators.PICTURE)
        pictures[0].click()
        assert self.is_present(ImagesLocators.PICTURE_WINDOW), "Картинка не открылась"
        picture_1 = self.find_element(ImagesLocators.OPENED_PICTURE).get_attribute('src')
        self.find_element(ImagesLocators.FORWARD_BUTTON).click()
        picture_2 = self.find_element(ImagesLocators.OPENED_PICTURE).get_attribute('src')
        assert picture_1 != picture_2, "Картинка не сменилась"
        self.find_element(ImagesLocators.BACK_BUTTON).click()
        picture_3 = self.find_element(ImagesLocators.OPENED_PICTURE).get_attribute('src')
        assert picture_1 == picture_3, "Первая картинка не осталась прежней"
