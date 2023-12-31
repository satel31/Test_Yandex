# Тестирование ЯндексПоиска и ЯндексКартинок

## Краткое описание

Тестирование сервисов ЯндексПоиск и ЯндексКартинки через браузер GoogleChrome.
Создан с использованием python, pytest и SeleniumWebDriver. Для логирования используется logging, логи записываются в
файл 'logfile.log'. Для формирования отчётов используется pytest-html.

## Инструкция по запуску

1. Установите зависимости проекта, указанные в файле pyproject.toml.
2. Запустите тесты
   ```bash
   # Для запуска всех тестов
   pytest -v tests -s
   ```
   ```bash
   # Для запуска тестов по отдельности
   pytest -v tests/test_search.py -s   
   pytest -v tests/test_images.py -s
   ```
   ```bash
   # Для запуска тестов с формированием отчёта в файле pytest_report.html
   pytest -v tests --html=pytest_report.html
   ```

## Технологии в проекте (стек)

* Python 3.11
* Selenium WebDriver
* Pytest
* Logging
* Pytest-html
