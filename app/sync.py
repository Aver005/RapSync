import os
import time
import json
from .config import load_config
from .encryption import encrypt_file
from .uploader import upload_file

def save_file_list(file_list):
    config_path = r'C:\ProgramData\RapSync\Config.rsy'
    with open(config_path, 'r+') as config_file:
        config = json.load(config_file)
        config['file_list'] = file_list
        config_file.seek(0)  # Сбросить указатель в начало файла
        json.dump(config, config_file, indent=4)
        config_file.truncate()  # Удалить старые данные после новой записи

def get_file_list(sync_folder):
    file_list = []
    for root, dirs, files in os.walk(sync_folder):
        for name in files:
            file_list.append(os.path.join(root, name))
        for name in dirs:
            file_list.append(os.path.join(root, name))
    return file_list

def sync_files():
    config = load_config()
    sync_folder = config['sync_folder']
    sync_interval = config['sync_interval']
    previous_file_list = []
    previous_access_time = os.path.getatime(sync_folder)

    while True:
        print(f"Проверка синхронизации в папке: {sync_folder}")
        last_access_time = os.path.getatime(sync_folder)
        current_file_list = get_file_list(sync_folder)
        
        if previous_access_time == last_access_time:
            print("Папка не изменена, пересохранение не требуется.")
            time.sleep(sync_interval)
            continue

        if len(current_file_list) == len(previous_file_list):
            print("Количество файлов не изменилось, пересохранение не требуется.")
            time.sleep(sync_interval)
            continue
        
        for file_path in current_file_list:
            if file_path not in previous_file_list:
                encrypted_file_path = encrypt_file(file_path)
                response = upload_file(encrypted_file_path)
                print(f"Файл {file_path} загружен на сервер: {response.text}")

        # save_file_list(current_file_list)
        print("Список файлов сохранен в конфигурации.")
        previous_file_list = current_file_list 
        previous_access_time = last_access_time 
        time.sleep(sync_interval)
