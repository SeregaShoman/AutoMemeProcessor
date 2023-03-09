import requests
from bs4 import BeautifulSoup

# URL сайта с таблицей прокси-серверов


# Запрос страницы

# Создание объекта BeautifulSoup из HTML-кода страницы


# Нахождение таблицы с прокси-серверами


# Нахождение всех строк таблицы


# Извлечение IP-адресов и портов из строк таблицы


class GetProxyList:
    url = "https://free-proxy-list.net/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', {'class': 'table table-striped table-bordered'})
    

    def get_proxy_list(self, count=10):
        ip_port = []
        rows = self.table.find_all('tr')[1:count+1]  # ограничение количества строк
        for row in rows:
            cols = row.find_all('td')
            ip = cols[0].text.strip()
            port = cols[1].text.strip()
            ip_port.append(f"{ip}:{port}")
        return ip_port
    