from src.upload_memes import UploaderMemes as _UM
import datetime
import configparser
import time

config = configparser.ConfigParser()
config.read('..\\config.ini', encoding='utf-8')

class UploadMemesProcessor(_UM):
    search_url = config["MEMEUPLOADERURL"]["url"]
    now = datetime.datetime.now()
    
    def _get_requests_from_config(self):
        requests = []
        for key, value in config.items('MEMEUPLOADERREQUEST'):
            requests.append(value)
        return requests
    
    def use_uploader(self):
        print("Начинается загрузка мемов")
        for request in self._get_requests_from_config():
            self.parse_html(self.search_url+request+" "+self.now.strftime('%Y-%m-%d'))
            self.get_image_and_save()
            time.sleep(5)
        print("Загрузка мемов окончена")

