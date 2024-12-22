import requests
from bs4 import BeautifulSoup

url = 'https://stavka.tv/matches'  # Замените на URL, который вы хотите парсить
response = requests.get(url)

# Проверьте, что запрос прошел успешно
if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')


    # Ищем заголовки. Измените 'h2' на нужный тег, если нужно
    title = soup.find_all('section', class_='MatchesTable MatchesTable--football')  

    # Открываем файл для записи
    with open('results.txt', 'w', encoding='utf-8') as file:
        # Записываем найденные заголовки в файл
        for title in titles:
            file.write(title.text + text.text + '\n')  # добавляем перевод строки

    print('Заголовки успешно записаны в файл results.txt')  # Подтверждение успешной записи
else:
    print(f'Ошибка при запросе страницы: {response.status_code}')
