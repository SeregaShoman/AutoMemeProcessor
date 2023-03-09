import schedule
from src.upload_processor import UploadMemesProcessor
from src.logger import Logger
import time

@Logger.log
def main():
    a = UploadMemesProcessor()
    a.use_uploader()    

schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
