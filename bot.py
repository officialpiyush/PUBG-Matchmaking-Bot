import discord
from discord.ext import commands
import motor.motor_asyncio as amotor
import asyncio

dbClient = amotor.AsyncIOMotorClient("mongodb+srv://akhil:<password>@pubg-3d4bw.mongodb.net/test?retryWrites=true")

bot = commands.Bot(command_prefix='m!')
bot.db=self.client['pubg']
bot.remove_command('help')
extensions = ['cogs.help','cogs.misc','cogs.register','cogs.error']
for extension in extensions:
    bot.load_extension(extension)
    print('Loaded '+ extension)



bot.run('Token')