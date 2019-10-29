import discord
from utils import log

api = {}
api["key"] = open("api_key", "r").read()
api["url"] = 'https://kanjialive-api.p.rapidapi.com/api/public/kanji/'
api["headers"] = {
    "x-rapidapi-host": "kanjialive-api.p.rapidapi.com",
    "x-rapidapi-key": api["key"]
}

logger = log.Log()

MAIN_COLOR = 0x673e74

AVAILABLE_COMMANDS = [
    {
        "title": "about",
        "short_desc": "Gives infos about the bot and its creator",
        "usages": [
            {
                "title": "&about",
                "desc": "Gives infos about the bot and its creator"
            }
        ]
    }, 
    {
        "title": "help",
        "short_desc": "Gives infos about commands",
        "usages": [
            {
                "title": "&help",
                "desc": "Gives a list of every available commands"
            },
            {
                "title": "&help [command]",
                "desc": "Gives details about the command given as argument"
            }
        ]
    },
    {
        "title": "hiragana",
        "short_desc": "Displays the hiragana table",
        "usages": [
            {
                "title": "&hiragana",
                "desc": "Displays the hiragana table"
            }
        ]
    },
    {
        "title": "kanji",
        "short_desc": "Gives details about given kanji",
        "usages": [
            {
                "title": "&kanji [kanji]",
                "desc": "Gives infos about the kanji given as argument"
            }
        ]
    },
    {
        "title": "katakana",
        "short_desc": "Displays the katakana table",
        "usages": [
            {
                "title": "&katakana",
                "desc": "Displays the katakana table"
            }
        ]
    }
]
