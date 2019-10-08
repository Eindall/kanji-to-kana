import discord

TOKEN = open("token", "r").read()

prefix = 'k!'

class Client(discord.Client):
  async def on_ready(self):
    print("Logged on as ", self.user)

client = Client()
client.run(TOKEN)