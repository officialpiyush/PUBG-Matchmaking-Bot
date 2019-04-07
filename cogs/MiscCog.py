import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def ping(self,ctx):
        latency = self.bot.latency*1000
        await ctx.send('Pong!Response time: '+str(latency)+'ms\U0001f550')

    @commands.command()
    async def invite(self,ctx):
        await ctx.send('https://discordapp.com/api/oauth2/authorize?client_id=562115824475963393&permissions=1074064497&scope=.bot')

    @commands.command()
    async def coolbot(self,ctx):
        await ctx.send('This bot is cool!')



def setup(bot):
    bot.add_cog(Misc(bot))