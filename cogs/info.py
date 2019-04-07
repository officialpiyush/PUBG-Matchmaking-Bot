import discord
from discord.ext import commands

class InfoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def info(self,ctx):
        user = ctx.message.author
        pfp = user.avatar_url
        embed = discord.Embed(title='MatchMaking Bot',description="**Matchmaking bot** is an exclusive bot made for **PUBG Mobile players**.\nThe main purpose of the bot is to enable PUBG players to match with better players other than randoms.\n\n**You can add me to your server through the following link:**\nhttps://discordapp.com/api/oauth2/authorize?client_id=562115824475963393&permissions=1074064497&scope=bot\n\n**🔗Links🔗**\n<:trello:564042459332739072> [Trello](https://trello.com/b/MkYPR32d/pubg-matchmaking-bot)\n<:twitter:564045070869856257> [Twitter](https://twitter.com/ThEKinG_1234)\n<:discord:564052000308723722> [Support Server](https://discord.gg/ZjMS2Yh)", colour = discord.Colour.green())
        embed.set_author(name = 'Command invoked by- ' + str(user),icon_url = pfp)
        embed.set_footer(text = 'I was made by ThE KinG#2149',icon_url = 'https://cdn.discordapp.com/attachments/548839515259797515/564049864413937684/JPEG_20190406_154323.jpg')
        await ctx.send(embed=embed)
    
    @commands.command()
    async def help(self,ctx):
        user = ctx.message.author
        pfp = user.avatar_url
        if user.bot:
            return
        else:
            embed = discord.Embed(colour = discord.Colour.dark_orange())
            embed.set_author(name='Help',icon_url=pfp)
            embed.add_field(name='Support',value='For more help, join the official bot support server: https://discord.gg/ZjMS2Yh',inline=False)
            embed.add_field(name='m!info',value='Gives the info of the bot!',inline=False)
            embed.add_field(name='m!help',value='Shows this message',inline=False)
            embed.add_field(name='m!ping',value='Replies Pong and shows Bot latency',inline=False)
            embed.add_field(name='m!invite',value='Gives link for adding the bot!',inline=False)
            helpmsg = await ctx.send(embed = embed)
            rxn1 = "\U000025b6"
            rxn2 = '\U000025c0'
            await helpmsg.add_reaction(emoji=rxn2) 
            await helpmsg.add_reaction(emoji=rxn1)



def setup(bot):
    bot.add_cog(InfoCog(bot))