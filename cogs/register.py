import discord
from discord.ext import commands

class RegisterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db.users

    @commands.command()
    async def register(self, ctx, userid: int,ingamename):
        if not len(str(userid)) == 9: # It Works
            await ctx.send("Character ID Is Invalid")
            return
        user = ctx.author 

        config = await self.db.find_one({'_id': str(userid)})

        await user.send("\⚠ | The Existing data ( if any ) will get overwrited!")

        await self.db.find_one_and_update(
            {'_id': str(user.id)},
            {'$set': {'IGN': ingamename, 'IGI': str(userid)}},
            upsert=True
        )

        await user.send(f'Your In game ID `{userid}` and In game name `{ingamename}` has been successfully saved in our DataBase.')


    @register.error
    async def register_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Arguments Were Not Given properly!\n`)register <character_id> <in_game_name>`")
def setup(bot):
    bot.add_cog(RegisterCog(bot))