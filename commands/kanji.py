import globals as G
import discord
import requests
import os
from utils import webm_to_gif
from utils.log import Level

async def run(client, message, args):
    if not args:
        G.logger.warn("No kanji given as argument. Arguments : {}".format(args))
        return await message.channel.send("<@" + str(message.author.id) + "> No kanji given as argument.")

    kanji = args[0]
    request = requests.get(G.api["url"] + kanji, headers=G.api["headers"])
    request = request.json()
        
    if 'error' in request:
        G.logger.warn("API could not found kanji \"{}\"".format(args[0]))
        return await message.channel.send("I'm sorry <@" + str(message.author.id) + ">, but I couldn't find this kanji...")

    # Request simplified
    kunyomi_romaji = request['kanji']['kunyomi']['romaji']
    hiragana = request['kanji']['kunyomi']['hiragana']
    katakana = request['kanji']['onyomi']['katakana']
    onyomi_romaji = request['kanji']['onyomi']['romaji']
    gif_filename = onyomi_romaji + '.gif'

    # GIF creation
    webm_to_gif.webm_to_gif(request['kanji']['video']['webm'], gif_filename)
    kanji_gif = discord.File(gif_filename, filename=gif_filename)
    
    # Embed creation
    card = discord.Embed(title="Kanji Card - " + request['kanji']['character'], description=request['kanji']['meaning']['english'])
    card.set_image(url='attachment://' + gif_filename)
    card.add_field(name="Pronounciation", value=hiragana + ' (' + kunyomi_romaji + ') | ' + katakana + ' (' + onyomi_romaji + ')', inline=False)
        
    if 'radical' in request:
        card.add_field(name="Radical", value=request['radical']['character'] + " [" + hiragana + " (" + request['radical']['name']['romaji'] + ")]")
    
    await message.channel.send(file=kanji_gif, embed=card)
    
    try:
        os.remove(gif_filename)
    except OSError as err:
        G.logger.warn("OSError: %s" % err)