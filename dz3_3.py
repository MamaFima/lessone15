import time
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
driver = webdriver.Chrome()

url = "https://www.divan.ru/category/divany"
driver.get(url)
time.sleep(5)

scroll_pause_time = 2
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(scroll_pause_time)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

prices = []
spans = driver.find_elements(By.TAG_NAME, "span")
for span in spans:
    text = span.text
    if 'руб.' in text:
        try:
            price = int(text.replace(' ', '').replace('руб.', ''))
            prices.append(price)
        except ValueError:
            continue

driver.quit()

if not prices:
    print("Не удалось спарсить цены. Проверьте правильность селекторов.")
else:
    # Сохранение данных в CSV файл
    df = pd.DataFrame(prices, columns=['Price'])
    df.to_csv('sofa_prices.csv', index=False)

    # Обработка данных
    mean_price = df['Price'].mean()
    print(f"Средняя цена на диваны: {mean_price} руб.")

    plt.hist(df['Price'], bins=30, edgecolor='black')
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (руб.)')
    plt.ylabel('Частота')
    plt.grid(True)
    plt.show()
