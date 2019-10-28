import discord
import globals
import requests
import sys, os, subprocess
import importlib

TOKEN = open("token", "r").read()

prefix = '&'

commands_dir = "commands"
commands = {}

command_list = discord.Embed(title="**__Command List__**", description="*Command's prefix : &*", color=globals.MAIN_COLOR)
command_list.add_field(name="**help**", value="> Gives a list of every available commands", inline=False)
command_list.add_field(name="**about**", value="> Gives infos about the bot and its creator", inline=False)


class Client(discord.Client):
  async def on_ready(self):
    # List files in directory "/commands"
    files = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/" + commands_dir)

    for module in files:
      if not module == "__init__.py" and module[-3:] == ".py":
        try:
          commands[module[:-3]] = importlib.import_module(commands_dir + "." + module[:-3])
          print("Loaded command %s" % module)
        except ModuleNotFoundError as err:
          print("ModuleNotFoundError: %s" % err, file=sys.stderr)
        except FileNotFoundError as err:
          print("FileNotFoundError: %s" % err, file=sys.stderr)

    print("Logged on as ", self.user)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="some weeb shit"))

  # TODO: 
  # Put all commands in /commands/[command].py
  async def on_message(self, message):
    if message.author == self.user or message.author.bot:
      return

    if message.content[0] == prefix:
      args = message.content.split(' ')
      command = args[0][1:]
      args = args[1:]

      if commands[command]:
        print("Command \"%s\" called by %s" % (command, message.author.name))
        return await commands[command].run(self, message, args)

      print("Command %s not found", command)

      '''# Help command
      if args[0] == prefix + "help":
        await message.channel.send("<@" + str(message.author.id) + ">, here are the bot's commands : ")
        await message.channel.send(embed=command_list)

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
        await message.channel.send("<@" + str(message.author.id) + ">, here is the hiragana table. Feel free to download it !", file=hiragana_table)'''

client = Client()
client.run(TOKEN)