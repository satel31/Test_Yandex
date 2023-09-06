from selenium.webdriver.common.by import By


class SearchLocators:
    SEARCH_FIELD = (By.ID, 'text')
    SUGGEST = (By.CSS_SELECTOR, 'div.mini-suggest__popup')
    LINKS = (By.CSS_SELECTOR, 'li div div a')

class ImagesLocators:
    ALL_SERVICES = (By.CLASS_NAME, 'services-suggest__list-item-more')
    IMAGES = (By.CSS_SELECTOR, 'div div span a')
