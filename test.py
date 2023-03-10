from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import logging
from logging import FileHandler


logger = logging.getLogger('logger')
logger.setLevel(logging.INFO)
handler = FileHandler('logger')
logger.addHandler(handler)
logger.info('info URL connect')

# Создаем переменные с URL адресами сайта
url1 = 'https://ru.wikipedia.org/wiki/Samsung_Galaxy_S22'
url2 = 'https://ru.wikipedia.org/wiki/Pixel_6/6_Pro'

# Будем работать с браузером 'Chrome', подключаем его драйвер
driver = webdriver.Chrome(executable_path=r'C:\Users\Rail\PycharmProjects\test\chromedriver\chromedriver.exe')

try:
    # Заходим на сайт и увеличиваем окно браузера
    driver.get(url=url1)
    logger.info(url1)
    driver.maximize_window()
    time.sleep(2)

    # Ищем элементы, если их не нашли в течении 10 секунд, то произойдет исключение
    try:
        driver.maximize_window()
        search_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='mw-parser-output']/p"))).text
        search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Android']")))
        href = search.get_attribute('href')
        print(search_text)
        print(href)
        search.click()
        logger.info(href)
        time.sleep(2)
    except TimeoutException:
        print('Android не найден')

    try:
        search_text1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='mw-parser-output']/p[32]"))).text
        search1 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "//a[@title='Android 13']")))
        href1 = search1.get_attribute('href')
        print(search_text1)
        print(href1)
        search1.click()
        logger.info(href1)
        time.sleep(2)
    except TimeoutException:
        print('Android 13 не найден')

    try:
        search_text2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='mw-parser-output']/p[2]"))).text
        search2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@title='Pixel 6']")))
        href2 = search2.get_attribute('href')
        print(search_text2)
        print(href2)
        search2.click()
        logger.info(href2)
        time.sleep(2)
    except TimeoutException:
        print('Pixel 6 не найден')

# Показывает ошибки
except Exception as ex:
    print(ex)
    print('Ошибка')

# Выходим из подключения чтобы ни случилось
finally:
    driver.quit()
