import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix='m!')
bot.remove_command('help')
extensions = ['cogs.help','cogs.misc','cogs.register','cogs.error']
for extension in extensions:
    bot.load_extension(extension)
    print('Loaded '+ extension)



bot.run('Token')