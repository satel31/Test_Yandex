from src.pages import SearchPage

URL = 'https://ya.ru/'
search_word = 'Тензор'
search_result = 'tensor.ru'

def test_yandex_search(browser):
    main_page = SearchPage(browser, URL)
    main_page.open()
    main_page.search_field()
    main_page.enter_word(search_word)
    resulted_link = main_page.results()
    assert search_result in resulted_link, f"Первая ссылка не ведёт на сайт{search_result}"
