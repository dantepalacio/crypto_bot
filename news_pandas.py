import pandas as pd

# Замените 'crypto_articles.csv' на путь к вашему CSV-файлу
csv_file_path = 'crypto_news.csv'

# Чтение CSV-файла с использованием Pandas
try:
    df = pd.read_csv(csv_file_path, delimiter=';')  # Указываем разделитель, если он отличается от запятой
    # Вывод первых нескольких строк для проверки
    print(df.head(100))

except Exception as ex:
    print(f'Ошибка при чтении CSV-файла: {str(ex)}')
