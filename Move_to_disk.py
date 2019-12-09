#! /usr/bin/env python
# -*- coding: utf-8 -*-
#Это я написал, потому что у меня комментарии на русском языке выбивали ошибку.

import requests
import json

URL_find_lang = "https://cloud-api.yandex.net/v1/disk/resources/upload"
path_file_name = "new-file4.txt" #Путь к файлу
OATHkey = '______________________' # вставить сюда ключ

def find_url_for_download():
    params = {
        'path': path_file_name
    }
    headers = {'Authorization': OATHkey}
    response = requests.get(URL_find_lang, headers=headers, params=params)
    json_ = response.json()
    return json_['href']

myString = '\n' #создаем строку для передачи в файл
with open('text.txt', encoding='utf-8') as f:
    while True:
        text = f.readline().strip()
        myString = myString + '\n' + text
        if not text:
            break


data_to_send = json.dumps(myString).encode('utf-8') #передаем строчку в файл
#почему то русский язык передается в файл странными символами хотя я сделал энкоуд, английский передается нормально.

print(requests.put(find_url_for_download(), data_to_send))
