from src.files_processor import FilesProcessor
import schedule
import time

def main():
    a = FilesProcessor()
    f = a.get_file_inform()
    a.check_and_delete_files(f)

schedule.every(1).minutes.do(main)

while True:
    schedule.run_pending()
    time.sleep(1)