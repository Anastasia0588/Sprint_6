import pytest
from selenium import webdriver

import links


@pytest.fixture(scope='function')
def driver():

    firefox_options = webdriver.FirefoxOptions()
    #firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1024, 768)
    driver.get(links.main_page)
    yield driver
    driver.quit()