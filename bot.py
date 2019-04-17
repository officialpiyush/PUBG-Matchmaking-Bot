import discord
from discord.ext import commands
from jishaku import Jishaku
from motor.motor_asyncio import AsyncIOMotorClient
# from pymongo import MongoClient
import logging

mongoURI = "mongodb://localhost:27017/"
# dbClient = MongoClient(mongoURI)

def get_prefix(bot, msg):
    prefixes = [")", "p."]

    return commands.when_mentioned_or(*prefixes)(bot, msg)

bot = commands.Bot(command_prefix=get_prefix, description="A Discord Bot To Make Teams")
bot.remove_command('help')

bot.db = AsyncIOMotorClient(mongoURI).pubg_bot

bot.load_extension("jishaku")


extensions = ['cogs.register','cogs.info','cogs.MiscCog']

if __name__ == "__main__":
    for extension in extensions:
        bot.load_extension(extension)
        print(f"Loaded Cog {extension}")

@bot.event
async def on_ready():
    print(f"[BOT] Ready!") 
    await bot.change_presence(activity = discord.Game(name='PUBG Mobile')) 


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# bot.run(os.getenv('Token'))
bot.run("NDk5MTI2MzY4NDk2NTE3MTI1.XKsrGw.Nchqu6_YKJLGX9BX0B6YrCaLtHs")