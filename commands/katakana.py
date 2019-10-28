import discord

async def run(client, message, args):
    hiragana_table = discord.File('img/hiragana.jpg')
    await message.channel.send("<@" + str(message.author.id) + ">, here is the hiragana table. Feel free to download it !", file=hiragana_table)