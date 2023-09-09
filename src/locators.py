from selenium.webdriver.common.by import By


class SearchLocators:
    SEARCH_FIELD = (By.ID, 'text')
    SUGGEST = (By.CSS_SELECTOR, '[class="mini-suggest__overlay mini-suggest__overlay_theme-color_dark mini-suggest__overlay_visible"]')
    LINKS = (By.CSS_SELECTOR, '[class="Link Link_theme_normal OrganicTitle-Link organic__url link"]')

class ImagesLocators:
    ALL_SERVICES = (By.CLASS_NAME, 'services-suggest__list-item-more')
    IMAGES = (By.CSS_SELECTOR, 'div div span a')
    CATEGORY = (By.CSS_SELECTOR, 'div div div div a')
    CATEGORY_TEXT = (By.CSS_SELECTOR, '[class="input__control mini-suggest__input"]')
    PICTURE = (By.CSS_SELECTOR, '[class="serp-item__link"]')
    PICTURE_WINDOW = (By.CSS_SELECTOR, '[class="MMImageContainer"]')
    OPENED_PICTURE = (By.CSS_SELECTOR, '[class="MMImage-Preview"]')
    FORWARD_BUTTON = (By.CSS_SELECTOR, '.MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext > i')
    BACK_BUTTON = (By.CSS_SELECTOR, '.MediaViewer-ButtonPrev.MediaViewer_theme_fiji-ButtonPrev > i')
