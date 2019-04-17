import discord
import asyncio
import motor.motor_asyncio as amotor
from discord.ext import commands
class Register(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.client=amotor.AsyncIOMotorClient("mongodb+srv://akhil:<password>@pubg-3d4bw.mongodb.net/test?retryWrites=true")
        self.db=self.client['pubg']
        self.collection=self.db['ids']
    @commands.command()
    async def register(self,ctx,character_id:int,*,ingamename):
        user = ctx.message.author
        channel = self.bot.get_channel(568004553069428747)
        if len(str(character_id)) == 9:
            try:
                await self.collection.insert_one({'_id':str(user.id),"character_id":str(character_id),"ingamename":ingamename})
                await ctx.send('Successfully registered!!')
                embed = discord.Embed(colour = discord.Colour.green())
                embed.add_field(name ='Character id',value=str(character_id))
                embed.add_field(name='In game name',value=ingamename)
                pfp = user.avatar_url
                embed.set_author(name='Details',icon_url=pfp)
                await ctx.send(embed = embed)
                await channel.send('New Registration!')
                await channel.send(embed = embed)
            except Exception as error:
                await self.collection.find_one_and_update({'_id':str(user.id)},{'$set':{'character_id':str(character_id),"ingamename":ingamename}})    
                await ctx.send('Found existing data and successfully updated!!')
                embed = discord.Embed(colour = discord.Colour.green())
                embed.add_field(name ='Character id',value=str(character_id))
                embed.add_field(name='In game name',value=ingamename)
                pfp = user.avatar_url
                embed.set_author(name='Details',icon_url=pfp)
                await ctx.send(embed = embed)
                await channel.send('Registration Update')
                await channel.send(embed = embed)
        else:
            await ctx.send('Invalid character id')
    @commands.command()
    async def details(self,ctx):
        user = ctx.message.author
        try:
            data = await self.collection.find_one({'_id':str(user.id)})
            char_id = data['character_id']
            ign = data['ingamename']
            embed = discord.Embed(colour = discord.Colour.green())
            embed.add_field(name ='Character id',value=char_id)
            embed.add_field(name='In game name',value=ign)
            pfp = user.avatar_url
            embed.set_author(name='Details',icon_url=pfp)
            await ctx.send(embed = embed)
        except:
            await ctx.send('Could not find any registered data.Register using `m!register <character_id> <in game name>` command.')
def setup(bot):
    bot.add_cog(Register(bot))
    