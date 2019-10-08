import discord

TOKEN = open("token", "r").read()

MAIN_COLOR = 0x673e74

prefix = '&'


command_list = discord.Embed(title="**__Command List__**", description="*Command's prefix : &*", color=MAIN_COLOR)
command_list.add_field(name="**help**", value="> Gives a list of every available commands", inline=False)
command_list.add_field(name="**about**", value="> Gives infos about the bot and its creator", inline=False)

about = discord.Embed(color=MAIN_COLOR)
about.add_field(name="**About KanjiToKana Bot**", value="KanjiToKana is a bot created in order to help people that wants to learn Japanese. It has been created by Eindall#2121, feel free to add me if you have any question or would like to submit a feature request")

class Client(discord.Client):
  async def on_ready(self):
    print("Logged on as ", self.user)
    await client.change_presence(status=discord.Status.online, activity=discord.Game(name="some weeb shit"))
  async def on_message(self, message):
    if message.author == self.user:
      return
    if message.content[0] == prefix:
      args = message.content.split(' ')

      if args[0] == prefix + "help":
        await message.channel.send("<@" + str(message.author.id) + ">, here are the bot's commands : ")
        await message.channel.send(embed=command_list)

      if args[0] == prefix + "about":
        await message.channel.send(embed=about)


client = Client()
client.run(TOKEN)