import json
import os
import shutil

CONFIG_PATH = r'C:\ProgramData\RapSync\Config.rsy'
ENCRYPTED_FILES_PATH = r'C:\ProgramData\RapSync\EncryptedFiles'
DEFAULT_CONFIG_PATH = os.path.join(os.path.dirname(__file__), 'configs', 'DefaultConfig.rsy')
UPLOAD_SERVER = "http://localhost:5000/upload"

def create_config():
    if not os.path.exists(ENCRYPTED_FILES_PATH):
        os.makedirs(ENCRYPTED_FILES_PATH)
        print("Папка для хранения файлов создана.")
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
        shutil.copyfile(DEFAULT_CONFIG_PATH, CONFIG_PATH)
        print("Конфигурационный файл создан из шаблона.")
    else:
        print("Конфигурационный файл уже существует.")

def load_config():
    global UPLOAD_SERVER
    with open(CONFIG_PATH, 'r', encoding='utf-8') as config_file:
        data = json.load(config_file)
        UPLOAD_SERVER = data['upload_url']
        return data
