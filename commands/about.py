import globals
import discord
import requests

async def run(client, message, args):
    about = discord.Embed(title="**__Command List__**", description="[Invite link]({})".format(discord.utils.oauth_url(631039334971342848)), color=globals.MAIN_COLOR)
    about.add_field(name="**Created on**", value="October 8th, 2019")
    about.add_field(name="**Version**", value="0.1.0")
    about.add_field(name="**Created by**", value="Eindall#2121 (Discord ID: 188621082192773120)\nEikinel#4650 (Discord ID: 169884954245857280)")
    about.add_field(name="**Library**", value="[discord.py](https://github.com/Rapptz/discord.py) v{}\n[requests](https://github.com/psf/requests) v{}".format(discord.__version__, requests.__version__))
    about.set_footer(text="KanjiToKana is a bot created in order to help people that wants to learn Japanese. Feel free to add the creator if you have any question or would like to submit a feature request")
    about.set_thumbnail(url=client.user.avatar_url)
    about.set_author(name="KanjiToKanaBot (Discord ID: {})".format(client.user.id), icon_url=client.user.avatar_url)

    return await message.channel.send(embed=about)