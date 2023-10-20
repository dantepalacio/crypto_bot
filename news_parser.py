# import requests
# from bs4 import BeautifulSoup


# url = 'https://coinmarketcap.com/'

# response = requests.get(url)

# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, "html.parser")
#     news_elements = soup.find_all("div", class_="hCrDHc")

#     for news_element in news_elements:
#         news_title = news_element.find("p").text
#         print(news_title)
# else:
#     print("Ошибка при запросе страницы", response.status_code)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time

# # Путь к установленному драйверу
# driver_path = 'C:\\Users\\m4rkness\\Desktop\\news_paper\\chromedriver.exe'

# # Создание экземпляра драйвера браузера
# driver = webdriver.Chrome()

# # URL страницы с новостями на CoinMarketCap
# url = 'https://coinmarketcap.com/currencies/bitcoin/#News'

# # Открываем страницу
# driver.get(url)

# # Ждем, пока страница загрузится и кнопка "Show More" станет доступной
# time.sleep(5)  # Подождем 5 секунд, вы можете увеличить это значение

# # Пока кнопка "Show More" доступна, кликаем на нее, чтобы загрузить больше новостей
# while True:
#     show_more_button = driver.find_element(By.XPATH, "//button[text()='Show More']")
#     if show_more_button.is_displayed():
#         show_more_button.click()
#         time.sleep(2)  # Подождем 2 секунды, чтобы новости загрузились
#     else:
#         break

# # Теперь вы можете извлекать текст новостей
# news_elements = driver.find_elements(By.CLASS_NAME, 'sc-16r8icm-0')

# for news in news_elements:
#     title = news.find_element(By.CLASS_NAME, 'sc-1eb5slv-0')
#     content = news.find_element(By.CLASS_NAME, 'sc-1eb5slv-0')
#     print("Заголовок:", title.text.strip())
#     print("Содержание:", content.text.strip())
#     print("-" * 50)

# # Закрываем браузер после завершения парсинга
# driver.quit()


# import requests
# from bs4 import BeautifulSoup
# from requests.exceptions import RequestException, HTTPError, ConnectionError

# # URL сайта с новостями
# url = 'https://cryptorank.io/news/bitcoin'

# try:
    
#     # Отправка GET-запроса к странице
#     response = requests.get(url)
#     response.raise_for_status()  # Генерировать исключение, если код статуса не 200 OK
    
#     # Инициализация BeautifulSoup для парсинга HTML-кода

#     soup = BeautifulSoup(response.text, 'html.parser')

    
#     # Нахождение всех ссылок на статьи на странице
#     article_links = []
#     article_elements = soup.find_all('div', class_='sc-6cc20a93-3')

#     for article in article_elements:
#         print(article)
    

    # if parent_div:
    #     link = parent_div.find('a')
    #     print(link)
    # Проход по каждой статье и извлечение информации
    # for article_link in article_links:
    #     article_url = 'https://coinmarketcap.com/currencies/bitcoin/#News' + article_link
    #     try:
    #         article_response = requests.get(article_url)
    #         article_response.raise_for_status()

    #         article_soup = BeautifulSoup(article_response.text, 'html.parser')

    #         # Извлекаем заголовок статьи
    #         title = article_soup.find('h1').text

    #         # Извлекаем содержание статьи
    #         content_elements = article_soup.select(".wPcEj")
    #         # find_all('div', class_='article__text')

    #         # Выводим результат
    #         print('\n')

    #         print('Заголовок:', title)

    #         print('\n')

    #         for content in content_elements:
    #             print(content.get_text())


    #     except (RequestException, HTTPError, ConnectionError) as e:
    #         print(f'Не удалось получить доступ к статье: {article_url}')
    #         print(f'Ошибка: {str(e)}')

# except (RequestException, HTTPError, ConnectionError) as e:
#     print('Не удалось получить доступ к главной странице новостей.')
#     print(f'Ошибка: {str(e)}')


# import time
# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# from bs4 import BeautifulSoup

# serv = Service(executable_path="C:\\Users\\m4rkness\\Desktop\\news_paper\\chromedriver.exe")
# driver = webdriver.Chrome(service=serv)

# try:
#     driver.maximize_window()
#     driver.get("https://cryptorank.io/news/bitcoin")
    
#     time.sleep(5)

#     article_links = []

#     while True:

#         article_elements = driver.find_elements(By.CLASS_NAME, "gTvscp")

#         for article in article_elements:
#             links = article.find_elements(By.TAG_NAME, "a")

#             for link in links:
#                 href = link.get_attribute("href")
#                 if href.startswith("https://cryptorank.io/news/feed/"):
#                     article_links.append(href)
 

#         try:
#             driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#             time.sleep(5)

#             WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "gTvscp")))

#         except Exception as ex:
#             print(f"Не удалось выполнить скроллинг: {ex}")
#             break

#     for article_link in article_links:
#         try:
#             article_response = requests.get(article_link)
#             article_response.raise_for_status()

#             article_soup = BeautifulSoup(article_response.text, 'html.parser')
#             # Извлекаем заголовок статьи

#             title = article_soup.find('h1', class_="kwzYET").text
#             print('\n')
#             print('Заголовок:', title)
#             print('\n')

#             content_elements = article_soup.find_all("p")

#             for content in content_elements:
#                 print(content.get_text())

#             time.sleep(5)

#         except Exception as ex:
#             print(f'Не удалось получить доступ к статье: {article_link}')
#             print(f'Ошибка: {str(ex)}') 

# except Exception as ex:
#     print('Не удалось получить доступ к главной странице новостей.')
#     print(f'Ошибка: {str(ex)}')



# import time
# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from bs4 import BeautifulSoup

# serv = Service(executable_path="C:\\Users\\m4rkness\\Desktop\\news_paper\\chromedriver.exe")
# driver = webdriver.Chrome(service=serv)

# try:
#     driver.maximize_window()
#     driver.get("https://cryptorank.io/news/bitcoin")
    
#     time.sleep(5)

#     article_links = []

#     article_elements = driver.find_elements(By.CLASS_NAME, "gTvscp")

#     for article in article_elements:
#         links = article.find_elements(By.TAG_NAME, "a")

#         for link in links:
#             href = link.get_attribute("href")
#             if href.startswith("https://cryptorank.io/news/feed/"):
#                 article_links.append(href)

#     for article_link in article_links:
#         try:
#             article_response = requests.get(article_link)
#             article_response.raise_for_status()

#             article_soup = BeautifulSoup(article_response.text, 'html.parser')
#             # Извлекаем заголовок статьи

#             title = article_soup.find('h1', class_="kwzYET").text
#             print('\n')
#             print('Заголовок:', title)
#             print('\n')

#             content_elements = article_soup.find_all("p")

#             for content in content_elements:
#                 print(content.get_text())

#             time.sleep(5)

#         except Exception as ex:
#             print(f'Не удалось получить доступ к статье: {article_link}')
#             print(f'Ошибка: {str(ex)}') 

# except Exception as ex:
#     print('Не удалось получить доступ к главной странице новостей.')
#     print(f'Ошибка: {str(ex)}')

# finally:
#     driver.quit()


# import time
# import requests
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup

# serv = Service(executable_path="C:\\Users\\m4rkness\\Desktop\\news_paper\\chromedriver.exe")
# driver = webdriver.Chrome(service=serv)

# try:
#     driver.maximize_window()
#     driver.get("https://cryptorank.io/news/bitcoin")
    
#     time.sleep(5)

#     article_links = []

#     while True:
#         article_elements = driver.find_elements(By.CLASS_NAME, "gTvscp")

#         for article in article_elements:
#             links = article.find_elements(By.TAG_NAME, "a")

#             for link in links:
#                 href = link.get_attribute("href")
#                 if href.startswith("https://cryptorank.io/news/feed/"):
#                     article_links.append(href)

#         # Скроллим страницу вниз, чтобы открыть следующую порцию статей
#         driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#         time.sleep(3)  # Подождите, чтобы контент подгрузился

#         # Если не найдено больше статей, завершаем цикл
#         break

#     for article_link in article_links:
#         try:
#             article_response = requests.get(article_link)
#             article_response.raise_for_status()

#             article_soup = BeautifulSoup(article_response.text, 'html.parser')
#             # Извлекаем заголовок статьи

#             title = article_soup.find('h1', class_="kwzYET").text
#             print('\n')
#             print('Заголовок:', title)
#             print('\n')

#             content_elements = article_soup.find_all("p")

#             for content in content_elements:
#                 print(content.get_text())

#             time.sleep(5)

#         except Exception as ex:
#             print(f'Не удалось получить доступ к статье: {article_link}')
#             print(f'Ошибка: {str(ex)}') 

# except Exception as ex:
#     print('Не удалось получить доступ к главной странице новостей.')
#     print(f'Ошибка: {str(ex)}')

# finally:
#     driver.quit()


# import time
# import requests
# import random
# import asyncio
# import aiohttp
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import csv
# from fake_useragent import UserAgent

# serv = Service(executable_path="C:\\Users\\m4rkness\\Docs\\Unik\\2023-2024\\database\\project(crypto)\\bitcoin_news(parser)\\parser\\chromedriver.exe")
# driver = webdriver.Chrome(service=serv)

# ua = UserAgent()
# delay = random.uniform(6, 8)

# proxy_url = "https://37.32.127.106:3128"

# async def parse_and_write_to_csv(article_link, csv_writer):
#     try:
#         headers = {
#             'User-Agent': ua.chrome
#         }

#         connector = aiohttp.TCPConnector(ssl=False)
#         async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
#             async with session.get(article_link, proxy=proxy_url) as response:
#                 response.raise_for_status()
#                 article_html = await response.text()

#         article_soup = BeautifulSoup(article_html, "html.parser")
        
#         title = driver.find_element(By.TAG_NAME, "h1")
        
#         print("Заголовок: ", title)

#         content_elements = article_soup.find_all("p")
#         content = "\n".join([content.text for content in content_elements])

#         print("Содержание: ", content)

        
#         csv_writer.writerow([title, content])

#     except Exception as ex:
#         print(f'Не удалось получить доступ к статье: {article_link}')
#         print(f'Ошибка: {str(ex)}') 

# async def main():
#     try:
#         driver.maximize_window()
#         driver.get("https://cryptorank.io/news/bitcoin")

#         await asyncio.sleep(delay)

#         article_links = []

#         previous_article_count = 0

#         while True:
#             # article_elements = driver.find_elements(By.CLASS_NAME, "cvJHkQ")
#             article_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'sc-9b4c4e3a-3')]")

#             for article in article_elements:
#                 links = article.find_elements(By.TAG_NAME, "a")
#                 print(article)

#                 for link in links:
#                     href = link.get_attribute("href")
#                     if href.startswith("https://cryptorank.io/news/feed/"):
#                         article_links.append(href)
#             # Скроллим страницу вниз, чтобы открыть следующую порцию статей
#             driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)

#             await asyncio.sleep(delay)  # Подождите, чтобы контент подгрузился
#             # # Если не найдено больше статей, завершаем цикл
#             current_article_count = len(article_links)
#             print(current_article_count)

#             if current_article_count == previous_article_count or current_article_count >= 100:
#                 break

#         csv_file_path = "C:\\Users\\m4rkness\\Docs\\Unik\\2023-2024\\database\\project(crypto)\\bitcoin_news(parser)\\parser\\crypto_news.csv"
#         with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
#             csv_writer = csv.writer(csvfile, delimiter=";")
#             csv_writer.writerow(["Title", "Content"])

#             tasks = []

#             for article_link in article_links:
#                 task = asyncio.create_task(parse_and_write_to_csv(article_link, csv_writer))
#                 tasks.append(task)

#             await asyncio.sleep(delay)
            
#             await asyncio.gather(*tasks)


#         print("Парсинг выполнен!")
#         print(f"Количество собранных статей: {len(article_links)}")

#     except Exception as ex:
#         print('Не удалось получить доступ к главной странице новостей.')
#         print(f'Ошибка: {str(ex)}')

#     finally:
#         driver.quit()

# asyncio.run(main())

# import os
# import time
# import requests
# import random
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
# import csv
# from fake_useragent import UserAgent
# from tqdm import tqdm

# serv = Service(executable_path="C:\\Users\\m4rkness\\Docs\\Unik\\2023-2024\\database\\project(crypto)\\bitcoin_news(parser)\\parser\\chromedriver.exe")
# driver = webdriver.Chrome(service=serv)

# ua = UserAgent()
# delay = random.uniform(4, 5)

# def parse_and_write_to_csv(article_link, csv_writer, parsed_titles):
#     print(article_link)
#     try:
#         headers = {
#             'User-Agent': ua.chrome
#         }

#         response = requests.get(article_link, headers=headers)
#         response.raise_for_status()
#         article_html = response.text

#         article_soup = BeautifulSoup(article_html, "html.parser")
        
#         title_element = article_soup.find("h1", class_="huQzNi")
        
#         if title_element:
#             title = title_element.text
#         else:
#             title = "Заголовок не найден"

#         if title in parsed_titles:
#             print(f"Статья {title} уже была спарсена.")
#             return

    
#         # title = driver.find_element(By.XPATH, '//h1[@class="sc-8d6ad85f-0 huQzNi"]')
        
#         # h1_text = title.text

#         print("\n")

#         print("Заголовок: ", title)

#         content_elements = article_soup.find_all("p")
#         content = "\n".join([content.text for content in content_elements])

#         print("Содержание: ", content)

#         print("\n")
        
#         csv_writer.writerow([title, content])

#     except Exception as ex:
#         print(f'Не удалось получить доступ к статье: {article_link}')
#         print(f'Ошибка: {str(ex)}') 

# def main():
#     try:
#         driver.maximize_window()
#         driver.get("https://cryptorank.io/news/bitcoin")

#         time.sleep(delay)



#         article_links = set()
#         parsed_titles = set()

#         previous_article_count = 0

#         while True:
#             article_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'sc-2cd471ac-3')]")

#             for article in article_elements:
#                 links = article.find_elements(By.TAG_NAME, "a")

#                 for link in links:
#                     href = link.get_attribute("href")
#                     if href.startswith("https://cryptorank.io/news/feed/"):
#                         if href not in article_links:
#                             article_links.add(href)
#                             print(f"Спарсено (кол-во ссылок) - {len(article_links)}")  # Добавляем ссылку в множество

            
#             driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#             time.sleep(delay)

#             current_article_count = len(article_links)
#             # print(f"Спарсено (кол-во ссылок) - {current_article_count}")
#             if current_article_count == previous_article_count or current_article_count >= 10:
#                 break
        
#         csv_file_path = "C:\\Users\\m4rkness\\Docs\\Unik\\2023-2024\\database\\project(crypto)\\bitcoin_news(parser)\\parser\\crypto_news.csv"
        

#         with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
#             csv_writer = csv.writer(csvfile, delimiter=";")
#             csv_writer.writerow(["Title", "Content"])

#             for article_link in tqdm(article_links, desc="Пасринг статей"):
#                 title = parse_and_write_to_csv(article_link, csv_writer, parsed_titles)
#                 time.sleep(delay)

#                 if title is not None:
#                     parsed_titles.add(title) 

#         print("Парсинг выполнен!")
#         print(f"Количество собранных статей: {len(article_links)}")

#     except Exception as ex:
#         print('Не удалось получить доступ к главной странице новостей.')
#         print(f'Ошибка: {str(ex)}')

#     finally:
#         driver.quit()


# if __name__ == "__main__":
#     main()

import time
import requests
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import csv
from fake_useragent import UserAgent
from tqdm import tqdm

serv = Service(executable_path="C:\\Users\\m4rkness\\Docs\\Unik\\2023-2024\\database\\project(crypto)\\bitcoin_news(parser)\\parser\\chromedriver.exe")
driver = webdriver.Chrome(service=serv)

ua = UserAgent()
# delay_parsing = random.uniform(3.5)

def parse_and_write_to_csv(article_link, csv_writer):
    print(article_link)
    try:
        headers = {
            'User-Agent': ua.chrome
        }

        response = requests.get(article_link, headers=headers)
        response.raise_for_status()
        article_html = response.text

        article_soup = BeautifulSoup(article_html, "html.parser")
        
        title = article_soup.find("h1", class_="huQzNi")
        # title = driver.find_element(By.XPATH, '//h1[@class="sc-8d6ad85f-0 huQzNi"]')
        
        h1_text = title.text

        print("\n")

        print("Заголовок: ", h1_text)

        content_elements = article_soup.find_all("p")
        content = "\n".join([content.text for content in content_elements])

        print("Содержание: ", content)

        print("\n")
        
        csv_writer.writerow([h1_text, content])

    except Exception as ex:
        print(f'Не удалось получить доступ к статье: {article_link}')
        print(f'Ошибка: {str(ex)}') 

def main():
    try:
        driver.maximize_window()
        driver.get("https://cryptorank.io/news/bitcoin")

        time.sleep(3)

        article_links = set()

        previous_article_count = 0

        scroll_position = 0

        while True:
            # article_elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'sc-2cd471ac-3')]")
            article_elements = driver.find_elements(By.CSS_SELECTOR, "div.sc-2cd471ac-3")
        
            for article in article_elements:
                links = article.find_elements(By.CSS_SELECTOR, "a")

                for link in links:
                    href = link.get_attribute("href")
                    if href.startswith("https://cryptorank.io/news/feed/"):
                        if href not in article_links:
                            article_links.add(href)
                            print(f"Спарсено (кол-во ссылок) - {len(article_links)}")  # Добавляем ссылку в множество
            
            
            driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight - 1500);")
            time.sleep(3)


            # current_height = driver.execute_script("return document.body.scrollHeight")
            # scroll_position += 3000
            
            # driver.execute_script(f"window.scrollTo(0, {scroll_position})")
            # time.sleep(3)

            # new_height = driver.execute_script("return document.body.scrollHeight")

            # if new_height == current_height:
            #     break





            # show_more_button = driver.find_elements(By.XPATH, "//button[contains(text(), 'Show More')]")

            # if show_more_button:
            #     show_more_button[0].click()  # Если кнопка "Show More" найдена, кликаем по ней
            #     time.sleep(2)  # Подождите немного после нажатия кнопки
            # else:
            #     # Если кнопки нет, выполняем скроллинг вниз
            #     driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            #     time.sleep(2)


            current_article_count = len(article_links)
            # print(f"Спарсено (кол-во ссылок) - {current_article_count}")
            if current_article_count == previous_article_count or current_article_count >= 500:
                break
        
        

        csv_file_path = "C:\\Users\\m4rkness\\Docs\\Unik\\2023-2024\\database\\project(crypto)\\bitcoin_news(parser)\\parser\\crypto_news.csv"
        with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=";")
            csv_writer.writerow(["Title", "Content"])

            for article_link in tqdm(article_links, desc="Пасринг статей"):
                parse_and_write_to_csv(article_link, csv_writer)
                time.sleep(random.uniform(4, 5))

        print("Парсинг выполнен!")
        print(f"Количество собранных статей: {len(article_links)}")

    except Exception as ex:
        print('Не удалось получить доступ к главной странице новостей.')
        print(f'Ошибка: {str(ex)}')

    finally:
        driver.quit()


if __name__ == "__main__":
    main()