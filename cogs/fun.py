import random
from discord.ext import commands

class Gaming(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Returns a simple Yes or No
    @commands.command()
    async def yesno(self, ctx):
        decision = random.choice(['yes', 'no'])
        await ctx.send("Your answer is " + str(decision))

    # Returns a choice from a given list
    @commands.command()
    async def choose(self, ctx, *args):
        decision = random.choice(args)
        await ctx.send("I have chosen " + decision)

def setup(bot):
    bot.add_cog(Gaming(bot))
