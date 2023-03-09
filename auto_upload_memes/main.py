import schedule
from src.upload_processor import UploadMemesProcessor
import time

def main():
    a = UploadMemesProcessor()
    a.use_uploader()    

schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
