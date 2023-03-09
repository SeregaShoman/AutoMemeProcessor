import os

folder_path = '..\\..\\images'

files = os.listdir(folder_path)

file_info = []
for file in files:
    file_path = os.path.join(folder_path, file)
    mod_time = os.path.getmtime(file_path)
    file_info.append((file, mod_time))

for file, mod_time in file_info:
    print(f"{file}: {mod_time}")

