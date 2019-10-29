import discord

async def run(client, message, args):
    katakana_table = discord.File('img/katakana.jpg')
    await message.channel.send("<@" + str(message.author.id) + ">, here is the katakana table. Feel free to download it !", file=katakana_table)