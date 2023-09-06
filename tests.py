from src.pages import SearchPage

URL = 'https://ya.ru/'

def test_yandex_search(browser):
    main_page = SearchPage(browser, URL)
    main_page.open()
    main_page.enter_word('Тензор')
    resulted_link = main_page.results()
    assert 'tensor.ru' in resulted_link
