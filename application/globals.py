URL = 'https://stormy-refuge-69718.herokuapp.com/'
TOKEN = '920389471:AAHJGFbPHCQ4sGFOY1BmQvQeIGz3hi9ydjw'
YANDEX_TOKEN = 'trnsl.1.1.20200216T090652Z.69ff82988b42b1f4.8757d1dc994b15b668fd4038482eea8fafe69908'
YANDEX_HOST = 'https://translate.yandex.net/api/v1.5/tr.json'
HOST = '0.0.0.0'
PORT = '5001'

supported_languages = {
    "af": "Afrikaans",
    "am": "Amharic",
    "ar": "Arabic",
    "az": "Azerbaijani",
    "ba": "Bashkir",
    "be": "Belarusian",
    "bg": "Bulgarian",
    "bn": "Bengali",
    "bs": "Bosnian",
    "ca": "Catalan",
    "ceb": "Cebuano",
    "cs": "Czech",
    "cv": "Chuvash",
    "cy": "Welsh",
    "da": "Danish",
    "de": "German",
    "el": "Greek",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "eu": "Basque",
    "fa": "Persian",
    "fi": "Finnish",
    "fr": "French",
    "ga": "Irish",
    "gd": "Scottish Gaelic",
    "gl": "Galician",
    "gu": "Gujarati",
    "he": "Hebrew",
    "hi": "Hindi",
    "hr": "Croatian",
    "ht": "Haitian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "id": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "ja": "Japanese",
    "jv": "Javanese",
    "ka": "Georgian",
    "kk": "Kazakh",
    "km": "Khmer",
    "kn": "Kannada",
    "ko": "Korean",
    "ky": "Kyrgyz",
    "la": "Latin",
    "lb": "Luxembourgish",
    "lo": "Lao",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "mg": "Malagasy",
    "mhr": "Mari",
    "mi": "Maori",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mn": "Mongolian",
    "mr": "Marathi",
    "mrj": "Hill Mari",
    "ms": "Malay",
    "mt": "Maltese",
    "my": "Burmese",
    "ne": "Nepali",
    "nl": "Dutch",
    "no": "Norwegian",
    "pa": "Punjabi",
    "pap": "Papiamento",
    "pl": "Polish",
    "pt": "Portuguese",
    "ro": "Romanian",
    "ru": "Russian",
    "si": "Sinhalese",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sq": "Albanian",
    "sr": "Serbian",
    "su": "Sundanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Telugu",
    "tg": "Tajik",
    "th": "Thai",
    "tl": "Tagalog",
    "tr": "Turkish",
    "tt": "Tatar",
    "udm": "Udmurt",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "vi": "Vietnamese",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "zh": "Chinese"
}

commands = {
    "uzen": "O'zbek tilidan ingliz tiliga tarjima qilish.",
    "enuz": "Ingliz tilidan o'zbek tiliga tarjima qilish.",
    "uzru": "O'zbek tilidan rus tiliga tarjima qilish.",
    "ruuz": "Rus tilidan o'zbek tiliga tarjima qilish.",
    "enru": "Ingliz tilidan rus tiliga tarjima qilish.",
    "ruen": "Rus tilidan ingliz tiliga tarjima qilish."
}

def start_info():
    message = "Ushbu tarjimon Yandex tarjimonga asoslangan.\nMumkin bo'lgan tillar ro'yxati:\n"
    for command in commands.keys():
        message += f"/{command} - {commands[command]}\n"

    return message