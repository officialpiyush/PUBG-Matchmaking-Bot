import discord
from discord.ext import commands
import asyncio
class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self,ctx):
        message = await ctx.send('Pong!')
        latency = self.bot.latency * 1000
        await asyncio.sleep(3)
        await message.edit(content= 'It took me ' + str(latency)+'ms to respond\U0001f55a')
    @commands.command()
    async def coolbot(self,ctx):
        await ctx.send('This bot is cool!')
    @commands.command()
    async def support(self,ctx):
        await ctx.send('Join our support server!!\nhttps://discord.gg/jgBqpkF')
    @commands.command()
    async def invite(self,ctx):
        await ctx.send('Add me to your server using this link:\nhttps://discordapp.com/api/oauth2/authorize?client_id=562115824475963393&permissions=1074130032&scope=bot')
    @commands.command()
    async def info(self,ctx):
        user = ctx.message.author
        pfp = user.avatar_url
        embed = discord.Embed(title='MatchMaking Bot',description="**Matchmaking bot** is an exclusive bot made for **PUBG Mobile players**.\nThe main purpose of the bot is to enable PUBG players to match with better players other than randoms.\n\n**You can add me to your server through the following link:**\nhttps://discordapp.com/api/oauth2/authorize?client_id=562115824475963393&permissions=1074064497&scope=bot\n\n**🔗Links🔗**\n<:trello:564042459332739072> [Trello](https://trello.com/b/MkYPR32d/pubg-matchmaking-bot)\n<:twitter:564045070869856257> [Twitter](https://twitter.com/ThEKinG_1234)\n<:discord:564052000308723722> [Support Server](https://discord.gg/ZjMS2Yh)", colour = discord.Colour.green())
        embed.set_author(name = 'Command invoked by- ' + str(user),icon_url = pfp)
        embed.set_footer(text = 'I was made by ThE KinG#2149',icon_url = 'https://cdn.discordapp.com/attachments/548839515259797515/564049864413937684/JPEG_20190406_154323.jpg')
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Misc(bot))
 