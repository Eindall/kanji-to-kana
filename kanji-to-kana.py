import discord
import requests
import os
import webm_to_gif

TOKEN = open("token", "r").read()

API_KEY = open("api_key", "r").read()

MAIN_COLOR = 0x673e74

prefix = '&'

api_headers = {
  "x-rapidapi-host": "kanjialive-api.p.rapidapi.com",
  "x-rapidapi-key": API_KEY
}

command_list = discord.Embed(title="**__Command List__**", description="*Command's prefix : &*", color=MAIN_COLOR)
command_list.add_field(name="**help**", value="> Gives a list of every available commands", inline=False)
command_list.add_field(name="**about**", value="> Gives infos about the bot and its creator", inline=False)

about = discord.Embed(title="**__Command List__**", description="[Invite link]({})".format(discord.utils.oauth_url(631039334971342848)), color=MAIN_COLOR)
about.add_field(name="**Created on**", value="October 8th, 2019")
about.add_field(name="**Version**", value="0.1.0")
about.add_field(name="**Created by**", value="Eindall#2121 (Discord ID: 188621082192773120)\nEikinel#4650 (Discord ID: 169884954245857280)")
about.add_field(name="**Library**", value="[discord.py](https://github.com/Rapptz/discord.py) v{}\n[requests](https://github.com/psf/requests) v{}".format(discord.__version__, requests.__version__))
about.set_footer(text="KanjiToKana is a bot created in order to help people that wants to learn Japanese. Feel free to add the creator if you have any question or would like to submit a feature request")

class Client(discord.Client):
  async def on_ready(self):
    print("Logged on as ", self.user)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="some weeb shit"))
  async def on_message(self, message):
    if message.author == self.user or message.author.bot:
      return
    if message.content[0] == prefix:
      args = message.content.split(' ')

      # Help command
      if args[0] == prefix + "help":
        await message.channel.send("<@" + str(message.author.id) + ">, here are the bot's commands : ")
        await message.channel.send(embed=command_list)

      # About command
      if args[0] == prefix + "about":
        about.set_thumbnail(url=self.user.avatar_url)
        about.set_author(name="KanjiToKanaBot (Discord ID: {})".format(self.user.id), icon_url=self.user.avatar_url)
        await message.channel.send(embed=about)

      # Kanji command
      if args[0] == prefix + "kanji":
        if len(args) < 2:
          await message.channel.send("<@" + str(message.author.id) + "> No kanji given as argument.")
        else:
          request = requests.get('https://kanjialive-api.p.rapidapi.com/api/public/kanji/' + args[1], headers=api_headers)
          request = request.json()
          if 'error' in request:
            await message.channel.send("I'm sorry <@" + str(message.author.id) + ">, but I couldn't find this kanji...")
          else:
            webm_to_gif.webm_to_gif(request['kanji']['video']['webm'], request['kanji']['onyomi']['romaji'] + ".gif")
            kanji_gif = discord.File(request['kanji']['onyomi']['romaji'] + ".gif", filename=request['kanji']['onyomi']['romaji'] + ".gif")
            card = discord.Embed(title="Kanji Card - " + request['kanji']['character'], description=request['kanji']['meaning']['english'])
            card.set_image(url='attachment://' + request['kanji']['onyomi']['romaji'] + ".gif")
            card.add_field(name="Pronounciation", value=request['kanji']['kunyomi']['hiragana'] + ' (' + request['kanji']['kunyomi']['romaji'] + ') | ' + request['kanji']['onyomi']['katakana'] + ' (' + request['kanji']['onyomi']['romaji'] + ')', inline=False)
            if 'radical' in request:
              card.add_field(name="Radical", value=request['radical']['character'] + " [" + request['radical']['name']['hiragana'] + " (" + request['radical']['name']['romaji'] + ")]")
            await message.channel.send(file=kanji_gif, embed=card)
            os.remove(request['kanji']['onyomi']['romaji'] + ".gif")

      # Kana commands
      if args[0] == prefix + "katakana":
        katakana_table = discord.File('img/katakana.jpg')
        await message.channel.send("<@" + str(message.author.id) + ">, here is the katakana table. Feel free to download it !", file=katakana_table)
      elif args[0] == prefix + "hiragana":
        hiragana_table = discord.File('img/hiragana.jpg')
        await message.channel.send("<@" + str(message.author.id) + ">, here is the hiragana table. Feel free to download it !", file=hiragana_table)

client = Client()
client.run(TOKEN)