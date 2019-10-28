import globals as G
import discord

async def run(client, message, args):
    command_list = discord.Embed(title="**__Command List__**", description="*Command's prefix : &*", color=G.MAIN_COLOR)
    command_list.add_field(name="**help**", value="> Gives a list of every available commands", inline=False)
    command_list.add_field(name="**about**", value="> Gives infos about the bot and its creator", inline=False)

    await message.channel.send("<@" + str(message.author.id) + ">, here are the bot's commands : ")
    await message.channel.send(embed=command_list)