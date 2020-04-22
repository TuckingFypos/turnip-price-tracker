from discord.ext import commands

class Status(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is online.')

    # Prints Successful Commands in Console
    @commands.Cog.listener()
    async def on_command_completion(self, ctx):
        print(ctx.command.name + " was executed successfully!")

def setup(bot):
    bot.add_cog(Status(bot))
