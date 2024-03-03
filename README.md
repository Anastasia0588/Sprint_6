# Sprint_6
Автотесты для учебного  [сервиса «Яндекс.Самокат»](https://qa-scooter.praktikum-services.ru/)
## Структура
tests - тесты

locators - хранение локаторов

pages - методы для взаимодействия со страницами и описание шагов

links.py - используемые ссылки

testdata.py - тестовые данные

requirements.txt - файл с внешними зависимостями

## Тесты
test_header_page.py - тесты для страницы хедера

test_main_page.py - тесты главной страницы

test_order_page.py - тесты страницы оформления заказа



### Запустить тесты
запустить все тесты:
```bash
pytest -v tests
```
зпустить все тесты с генерацией отчетов
```bash
pytest tests --alluredir=allure_results 
```
