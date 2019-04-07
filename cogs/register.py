import discord
from discord.ext import commands

class RegisterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.db["users"]

    @commands.command()
    async def register(self, ctx, userid: int,ingamename):
        if not len(str(userid)) == 9: # It Works
            await ctx.send("Character ID Is Invalid")
            return
        user = ctx.author          
        
        # conf = self.db.find({"user_id": str(user.id)})
        # if conf:# i believe in you  lmao :3 shouldnt next line be awaited? thats why i said, I believe in you lmao. lol
        #     await ctx.send("We had you information in our database,Now This Will Overwrite existing data.")
        self.db.delete_one({"user_id": str(userid)})

        userInfo = {"user_id": str(ctx.author.id),
            "hasData": True,
            "ignID": str(userid),
            "IGN": str(ingamename) 
            }

        dbID = self.db.insert_one(userInfo)

        await user.send(f'Your In game ID `{userid}` and In game name `{ingamename}` has been successfully saved in our Data Base With Database ID - `{dbID.inserted_id}`')


    @register.error
    async def register_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Arguments Were Not Given properly!\n`)register <character_id> <in_game_name>`")
def setup(bot):
    bot.add_cog(RegisterCog(bot))