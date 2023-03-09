import schedule
from src.upload_processor import UploadMemesProcessor
import time

def main():
    print("govno")
    a = UploadMemesProcessor()
    a.use_uploader()    

main()
#schedule.every(1).minutes.do(main)

#while True:
    #schedule.run_pending()
    #time.sleep(1)
