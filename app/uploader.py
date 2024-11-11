import requests
import os
from .config import UPLOAD_SERVER

def upload_file(file_path):
    url = UPLOAD_SERVER
    with open(file_path, 'rb') as file:
        response = requests.post(url, files={'file': (os.path.basename(file_path), file)})
    return response
