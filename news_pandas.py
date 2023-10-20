import pandas as pd

# Замените 'crypto_articles.csv' на путь к вашему CSV-файлу
csv_file_path = 'C:\\Users\\m4rkness\\Docs\\Unik\\2023-2024\\database\\project(crypto)\\bitcoin_news(parser)\\parser\\crypto_news.csv'

# Чтение CSV-файла с использованием Pandas
try:
    df = pd.read_csv(csv_file_path, delimiter=';')  # Указываем разделитель, если он отличается от запятой
    # Вывод первых нескольких строк для проверки
    print(len(df["Title"].value_counts()))

except Exception as ex:
    print(f'Ошибка при чтении CSV-файла: {str(ex)}')
