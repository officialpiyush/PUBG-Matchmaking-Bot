import discord
from discord.ext import commands
class Error(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            await ctx.send("That command doesn't exist.")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send('This command cannot be used in private messages.')
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send('Sorry. This command is disabled and cannot be used.')
        elif isinstance(error, commands.errors.MissingRequiredArgument):
            await ctx.send(f"Not enough arguments supplied.")
            await ctx.send_help(ctx.command)
        elif isinstance(error, commands.errors.BadArgument):
            await ctx.send(f"Bad arguments supplied.")
            await ctx.send_help(ctx.command)
        elif isinstance(error, commands.errors.NotOwner):
            await ctx.send("This command is only for my master, AXVin!!!!")
        elif isinstance(error, discord.errors.Forbidden):
            await ctx.send("I don't have enough permsissions to do that!")
        elif isinstance(error, commands.errors.MissingPermissions):
            await ctx.author.send("You don't have enough permissions to use this command!")
        else:
            raise
def setup(bot):
    bot.add_cog(Error(bot))