# from secrets import YANDEX_TRNSL_KEY, YANDEX_DICT_KEY

YANDEX_TRNSL_KEY = 'trnsl.1.1.20170324T011406Z.c567f3cf5967f5a9.58ef012e20163c0ff45d69c27bea361c9a8e3934'

YANDEX_DICT_KEY = 'dict.1.1.20180329T043155Z.59a6d54d0b930186.2a7117cd310b296f965c3b630d171d4831fa947e'

LANG_CODES = {'az': 'Azerbaijan',
             'sq': 'Albanian',
             'am': 'Amharic',
             'en': 'English',
             'ar': 'Arabic',
             'hy': 'Armenian',
             'af': 'Afrikaans',
             'eu': 'Basque',
             'ba': 'Bashkir',
             'be': 'Belarusian',
             'bn': 'Bengali',
             'my': 'Burmese',
             'bg': 'Bulgarian',
             'bs': 'Bosnian',
             'cy': 'Welsh',
             'hu': 'Hungarian',
             'vi': 'Vietnamese',
             'ht': 'Haitian (Creole)',
             'gl': 'Galician',
             'nl': 'Dutch',
             'mrj': 'Hill Mari',
             'el': 'Greek',
             'ka': 'Georgian',
             'gu': 'Gujarati',
             'da': 'Danish',
             'he': 'Hebrew',
             'yi': 'Yiddish',
             'id': 'Indonesian',
             'ga': 'Irish',
             'it': 'Italian',
             'is': 'Icelandic',
             'es': 'Spanish',
             'kk': 'Kazakh',
             'kn': 'Kannada',
             'ca': 'Catalan',
             'ky': 'Kyrgyz',
             'zh': 'Chinese',
             'ko': 'Korean',
             'xh': 'Xhosa',
             'km': 'Khmer',
             'lo': 'Laotian',
             'la': 'Latin',
             'lv': 'Latvian',
             'lt': 'Lithuanian',
             'lb': 'Luxembourgish',
             'mg': 'Malagasy',
             'ms': 'Malay',
             'ml': 'Malayalam',
             'mt': 'Maltese',
             'mk': 'Macedonian',
             'mi': 'Maori',
             'mr': 'Marathi',
             'mhr': 'Mari',
             'mn': 'Mongolian',
             'de': 'German',
             'ne': 'Nepali',
             'no': 'Norwegian',
             'pa': 'Punjabi',
             'pap': 'Papiamento',
             'fa': 'Persian',
             'pl': 'Polish',
             'pt': 'Portuguese',
             'ro': 'Romanian',
             'ru': 'Russian',
             'ceb': 'Cebuano',
             'sr': 'Serbian',
             'si': 'Sinhala',
             'sk': 'Slovakian',
             'sl': 'Slovenian',
             'sw': 'Swahili',
             'su': 'Sundanese',
             'tg': 'Tajik',
             'th': 'Thai',
             'tl': 'Tagalog',
             'ta': 'Tamil',
             'tt': 'Tatar',
             'te': 'Telugu',
             'tr': 'Turkish',
             'udm': 'Udmurt',
             'uz': 'Uzbek',
             'uk': 'Ukrainian',
             'ur': 'Urdu',
             'fi': 'Finnish',
             'fr': 'French',
             'hi': 'Hindi',
             'hr': 'Croatian',
             'cs': 'Czech',
             'sv': 'Swedish',
             'gd': 'Scottish',
             'et': 'Estonian',
             'eo': 'Esperanto',
             'jv': 'Javanese',
             'ja': 'Japanese'}


# API URL BASES

TRNSL_BASE = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=' + YANDEX_TRNSL_KEY
DICT_BASE = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key=' + YANDEX_DICT_KEY