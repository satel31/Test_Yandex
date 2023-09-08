from src.pages import ImagePage

URL = 'https://ya.ru/'

def test_yandex_images(browser):
    main_page = ImagePage(browser, URL)
    main_page.open()
    main_page.menu()
    main_page.choose_category()
    main_page.picture()

