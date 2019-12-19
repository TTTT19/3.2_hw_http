#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Это я написал, потому что у меня комментарии на русском языке выбивали ошибку.

import requests
import json

URL_find_lang = "https://cloud-api.yandex.net/v1/disk/resources/upload"
path_file_name = "proba1234.txt" #Путь к файлу
OATHkey = '_________________' # вставить сюда ключ

def find_url_for_download():
    params = {
        'path': path_file_name
    }
    headers = {'Authorization': OATHkey}
    response = requests.get(URL_find_lang, headers=headers, params=params)
    json_ = response.json()
    return json_['href']


with open ('text.txt', encoding='utf-8') as f:
    data = f.read()
    print(requests.put(find_url_for_download(), data=data))
