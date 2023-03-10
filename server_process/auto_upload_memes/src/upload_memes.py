import requests
import shortuuid
from bs4 import BeautifulSoup
from src.logger import Logger

class UploaderMemes():
    
    @Logger.log
    def parse_html(self, response_url) -> None:
        self.url = response_url
        response = requests.get(response_url)
        self.soup = BeautifulSoup(response.content, 'html.parser')

    def _get_unique_name_and_uuid(self):
        query = self.url.split("=")[-1]
        query = query.replace(" ", "_")
        new_name = f"{query}_{shortuuid.uuid()}"
        return new_name

    @Logger.log
    def get_image_and_save(self, file_path):
        for img in self.soup.find_all('img', {'class': 'serp-item__thumb justifier__thumb'}):
            image_url = img['src']
            with open(f'{file_path}\\{self._get_unique_name_and_uuid()}.jpg', 'wb') as f:
                response = requests.get("https:"+image_url)
                f.write(response.content)
