import discord
from discord.ext import commands
class MyHelp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def help(self,ctx):
        user = ctx.message.author
        if user.bot:
            return
        else:
            embed = discord.Embed(colour = discord.Colour.dark_orange())
            embed.set_author(name='Help (5 commands)')
            embed.add_field(name='Support',value='For more help, join the official bot support server: https://discord.gg/ZjMS2Yh',inline=False)
            embed.add_field(name='m!info',value='Gives the info of the bot!',inline=False)
            embed.add_field(name='m!help',value='Shows this message',inline=False)
            embed.add_field(name='m!ping',value='Replies Pong and shows Bot latency',inline=False)
            embed.add_field(name='m!invite',value='Gives link for adding the bot!',inline=False)
            embed.add_field(name='m!coolbot',value='Is this bot cool?',inline=False)
            helpmsg = await ctx.send(embed = embed)
def setup(bot):
    bot.add_cog(MyHelp(bot))