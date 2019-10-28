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
