import os
import datetime
import configparser

config = configparser.ConfigParser()
config.read('..\\config.ini', encoding='utf-8')
folder_path = config['CHECKERFILES']["path_to_folder"]

class FilesProcessor():
    files = os.listdir(folder_path)
    last_check_time = datetime.datetime.now()

    def get_file_inform(self):
        file_info = []
        for file in self.files:
            file_path = os.path.join(folder_path, file)
            mod_time = os.path.getmtime(file_path)
            file_info.append({file: datetime.datetime.fromtimestamp(mod_time)})
        print(file_info)
        return file_info
    
    def check_and_delete_files(self, file_info):
        for info in file_info:
            for file, mod_time in info.items():
                if mod_time >= self.last_check_time:
                    continue
                time_diff = (datetime.datetime.now() - mod_time).total_seconds() / 1
                if time_diff > 24:
                    file_path = os.path.join(folder_path, file)
                    os.remove(file_path)
                    print(f"Deleted file {file} modified on {mod_time.strftime('%d %b %Y')}")
