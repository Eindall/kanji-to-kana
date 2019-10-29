import globals as G
import discord

async def run(client, message, args):
    if len(args) == 1:
        for command in G.AVAILABLE_COMMANDS:
            if args[0] == command["title"]:
                matching_command = command
                break
        try:
            matching_command
        except NameError:
            G.logger.warn("No command found. Arguments: {}".format(args))
            return await message.channel.send("Sorry <@" + str(message.author.id) + ">, the command " + args[0] + " does not exist !")
        else:
            command_details = discord.Embed(title="**__Command details - " + matching_command["title"] + "__**", description=matching_command["short_desc"], color=G.MAIN_COLOR)
            for usage in matching_command["usages"]:
                command_details.add_field(name="**" + usage["title"] + "**", value="> " + usage["desc"]) 
            await message.channel.send(embed=command_details)
    else:
        command_list = discord.Embed(title="**__Command List__**", description="*Command's prefix : &*", color=G.MAIN_COLOR)
        for command in G.AVAILABLE_COMMANDS:
            command_list.add_field(name="**" + command["title"] + "**", value="> " + command["short_desc"], inline=False) 
        await message.channel.send("<@" + str(message.author.id) + ">, here are the bot's commands : ")
        await message.channel.send(embed=command_list)