import requests
 # документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL_find_lang = 'https://translate.yandex.net/api/v1.5/tr.json/detect'
URL_tanslate = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

#Словарь с языками из справочника яндекса
all_lang = {'az': 'Азербайджанский',	'ml': 'малаялам',
    'sq': 'албанский',	'mt': 'мальтийский',
    'am': 'амхарский',	'mk': 'македонский',
    'en': 'английский',	'mi': 'маори',
    'ar': 'арабский',	'mr': 'маратхи',
    'hy': 'армянский',	'mhr': 'марийский',
    'af': 'африкаанс',	'mn': 'монгольский',
    'eu': 'баскский',	'de': 'немецкий',
    'ba': 'башкирский',	'ne': 'непальский',
    'be': 'белорусский',	'no': 'норвежский',
    'bn': 'бенгальский',	'pa': 'панджаби',
    'my': 'бирманский',	'pap': 'папьяменто',
    'bg': 'болгарский',	'fa': 'персидский',
    'bs': 'боснийский',	'pl': 'польский',
    'cy': 'валлийский',	'pt': 'португальский',
    'hu': 'венгерский',	'ro': 'румынский',
    'vi': 'вьетнамский',	'ru': 'русский',
    'ht': 'гаитянский (креольский)',	'ceb': 'себуанский',
    'gl': 'галисийский',	'sr': 'сербский',
    'nl': 'голландский',	'si': 'сингальский',
    'mrj': 'горномарийский',	'sk': 'словацкий',
    'el': 'греческий',	'sl': 'словенский',
    'ka': 'грузинский',	'sw': 'суахили',
    'gu': 'гуджарати',	'su': 'сунданский',
    'da': 'датский',	'tg': 'таджикский',
    'he': 'иврит',	'th': 'тайский',
    'yi': 'идиш',	'tl': 'тагальский',
    'id': 'индонезийский',	'ta': 'тамильский',
    'ga': 'ирландский',	'tt': 'татарский',
    'it': 'итальянский',	'te': 'телугу',
    'is': 'исландский',	'tr': 'турецкий',
    'es': 'испанский',	'udm': 'удмуртский',
    'kk': 'казахский',	'uz': 'узбекский',
    'kn': 'каннада',	'uk': 'украинский',
    'ca': 'каталанский',	'ur': 'урду',
    'ky': 'киргизский',	'fi': 'финский',
    'zh': 'китайский',	'fr': 'французский',
    'ko': 'корейский',	'hi': 'хинди',
    'xh': 'коса',	'hr': 'хорватский',
    'km': 'кхмерский',	'cs': 'чешский',
    'lo': 'лаосский',	'sv': 'шведский',
    'la': 'латынь',	'gd': 'шотландский',
    'lv': 'латышский',	'et': 'эстонский',
    'lt': 'литовский',	'eo': 'эсперанто',
    'lb': 'люксембургский',	'jv': 'яванский',
    'mg': 'малагасийский',	'ja': 'японский',
    'ms': 'малайский'}

#Функция для определения языка
def translate_find_language(text):
    """
    https://translate.yandex.net/api/v1.5/tr.json/detect ?
    key=<API-ключ>
     & text=<переводимый текст>
     & [hint=<список вероятных языков текста>]
     & [callback=<имя callback-функции>]
    :param hint:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text
        #'hint': 'en,de'
    }

    response = requests.get(URL_find_lang, params=params)
    json_ = response.json()
    return ''.join(json_['lang'])

#Функция для перевода с языка, который передается в параметр lang_text на язык указанный в need_lang_text
def translate_it(text, lang_text, need_lang_text):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param lang_text:
    :return:
    """

    params = {
        'key': API_KEY,
        'text': text,
        'lang': '{}-{}'.format(lang_text, need_lang_text),
    }

    response = requests.get(URL_tanslate, params=params)
    json_ = response.json()
    return ''.join(json_['text'])

#Функция перевод файла на указанный язык (язык с которого нужно переводить находит с помощью функции translate_find_language
def read_translate_and_write_file(file_path, need_lang_text = 'ru'):
    with open('text.txt', 'a', encoding='utf-8') as d:
        d.write(f'Перевод текста из файла: {file_path}\n')
        with open(file_path, encoding='utf-8') as f:
            while True:
                text = f.readline().strip()
                f.readline().strip()
                if not text:
                    print("Текст из файла переведен и записан в файл 'text.txt")
                    break
                else:
                    lang_text = translate_find_language(f'{text}')
                    translated_text = translate_it(text, lang_text,need_lang_text)
                    d.write(f'{translated_text}\n')

#Функция выводит словарь с языками
def help_pick_lang():
    for dict in all_lang:
        print(f'Для того чтобы выбрать язык "{all_lang[dict]}" наберите "{dict}"')

#Функция для выбора файла
def pick_file():
    while True:
        pick_file_input = input('Какой файл хотите открыть? (ES, DE, FR)\n')
        if pick_file_input.upper() == 'ES':
            file_path = 'ES.txt'
            return file_path
        elif pick_file_input.upper() == 'DE':
            file_path = 'DE.txt'
            return file_path
        elif pick_file_input.upper() == 'FR':
            file_path = 'FR.txt'
            return file_path
        else:
            print('Не правильно ввели код')

#Функция для выбора языка, на который будем переводить
def pick_language():
    while True:
        pick_language_input = input('На какой язык хотите перевести файл? (для подсказки введите h)\n')
        if pick_language_input.lower() in all_lang:
            print(f'Вы выбрали {all_lang[pick_language_input.lower()]} язык')
            return pick_language_input.lower()
        elif pick_language_input == 'h':
            help_pick_lang()
        else:
            print('Не правильно ввели код')


#Запускаем функцию, выбираем путь к файлу и выбираем язык, на который будем переводить (изначальный язык находится сам)
read_translate_and_write_file(pick_file(), pick_language())

