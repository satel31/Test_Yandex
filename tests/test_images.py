from logs import logs
from src.pages import ImagePage

URL = 'https://ya.ru/'


def test_yandex_images(browser):
    logs(info='Тест начат')
    try:
        main_page = ImagePage(browser, URL)
        main_page.open()
        main_page.menu()
        main_page.choose_category()
        main_page.picture()
    except Exception as e:
        logs(error=e)
    finally:
        logs(info='Тест закончен')
