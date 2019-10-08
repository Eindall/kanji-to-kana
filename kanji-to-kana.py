import discord

TOKEN = 'NjMxMDM5MzM0OTcxMzQyODQ4.XZxLEA.oTKm6lqn45WcPVcartWMnZ55Lmk'

prefix = 'k!'

class Client(discord.Client):
  async def on_ready(self):
    print("Logged on as ", self.user)

client = Client()
client.run(TOKEN)