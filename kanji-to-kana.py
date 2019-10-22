import discord
import requests
import os

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
about.add_field(name="**Version**", value="0.0.0")
about.add_field(name="**Created by**", value="Eindall#2121 (Discord ID: 188621082192773120)")
about.add_field(name="**Library**", value="[discord.py](https://github.com/Rapptz/discord.py) v{}".format(discord.__version__))
about.set_footer(text="KanjiToKana is a bot created in order to help people that wants to learn Japanese. Feel free to add the creator if you have any question or would like to submit a feature request")

class Client(discord.Client):
  async def on_ready(self):
    print("Logged on as ", self.user)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="some weeb shit"))
  async def on_message(self, message):
    if message.author == self.user:
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
            card = discord.Embed(title="Kanji Card - " + request['kanji']['character'], description=request['kanji']['meaning']['english'])
            card.set_image(url="http://kanji.nihongo.cz/image.php?text=" + request['kanji']['character'] + "&font=sod.ttf&fontsize=300&color=white")
            card.add_field(name="Pronounciation", value=request['kanji']['kunyomi']['hiragana'] + ' (' + request['kanji']['kunyomi']['romaji'] + ') | ' + request['kanji']['onyomi']['katakana'] + ' (' + request['kanji']['onyomi']['romaji'] + ')', inline=False)
            if 'radical' in request:
              card.add_field(name="Radical", value=request['radical']['character'] + " [" + request['radical']['name']['hiragana'] + " (" + request['radical']['name']['romaji'] + ")]")
            await message.channel.send(embed=card)

      # Test lol eussou
      if args[0] == prefix + "test":
        embed=discord.Embed(title="Kanji Card - 私", url="https://jisho.org/search/%E7%A7%81%20%23kanji", description="private, I, me")
        embed.set_image(url="http://kanji.nihongo.cz/image.php?text=%E7%A7%81&font=sod.ttf&fontsize=300&color=white")
        embed.add_field(name="Pronounciation", value="わたし (watashi) | し (SHI)", inline=False)
        embed.add_field(name="Key(s)", value="厶 (28) | 禾 (115)", inline=False)
        await message.channel.send(embed=embed)


client = Client()
client.run(TOKEN)