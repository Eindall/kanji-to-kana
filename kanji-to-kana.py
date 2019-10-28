import globals as G
import discord
import requests
import sys, os, subprocess
import importlib
from utils.log import Level

TOKEN = open("token", "r").read()
prefix = '&'
commands_dir = "commands"
commands = {}

class Client(discord.Client):
  async def on_ready(self):
    G.logger.setLevel(Level.INFO)

    # List files in directory "/commands"
    files = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/" + commands_dir)

    for module in files:
      if not module == "__init__.py" and module[-3:] == ".py":
        try:
          commands[module[:-3]] = importlib.import_module(commands_dir + "." + module[:-3])
          G.logger.info("Loaded command %s" % module)
        except ModuleNotFoundError as err:
          G.logger.warn("ModuleNotFoundError: %s" % err)
        except FileNotFoundError as err:
          G.logger.warn("FileNotFoundError: %s" % err)

    G.logger.info("Logged on as %s" % self.user)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="some weeb shit"))

  async def on_message(self, message):
    if message.author == self.user or message.author.bot:
      return

    if message.content[0] == prefix:
      args = message.content.split(' ')
      command = args[0][1:]
      args = args[1:]

      G.logger.info("Command \"%s\" called by %s" % (command, message.author.name))
      
      if command in commands:
        return await commands[command].run(self, message, args)

      G.logger.warn("Command %s not found" % command)

client = Client()
client.run(TOKEN)