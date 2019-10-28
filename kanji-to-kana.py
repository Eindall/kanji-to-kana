import globals
import discord
import requests
import sys, os, subprocess
import importlib

TOKEN = open("token", "r").read()

prefix = '&'

commands_dir = "commands"
commands = {}

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

client = Client()
client.run(TOKEN)