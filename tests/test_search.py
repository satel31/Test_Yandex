from src.logs import logs
from src.pages import SearchPage

URL: str = 'https://ya.ru/'
search_word: str = 'Тензор'
search_result: str = 'tensor.ru'

def test_yandex_search(browser):
    """Тестирование Яндекс поиска"""
    logs(info='Тест начат')
    try:
        main_page = SearchPage(browser, URL)
        main_page.open()
        main_page.search_field()
        main_page.enter_word(search_word)
        resulted_link = main_page.results()
        assert search_result in resulted_link, f"Первая ссылка не ведёт на сайт{search_result}"
    except Exception as e:
        logs(error=e)
    finally:
        logs(info='Тест закончен')
