import discord
import random
import re
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

    # Rolls any ndn sided dice.
    @commands.command()
    async def roll(self, ctx, arg = "1d6"):
        arg.lower()
        # Use a regular expression to split the string, then turn both fields into ints
        player_roll = re.split(r"d", arg)
        player_roll[0] = int(player_roll[0])
        player_roll[1] = int(player_roll[1])
        # Roll the dice and count down the total rolls
        while player_roll[0] > 0:
            roll = random.randrange(1, player_roll[1])
            await ctx.send("Rolling dice {} ... rolled a {}.".format(player_roll[0], roll))
            player_roll[0] -= 1

    #Creates a Quickpoll
    @commands.command()
    async def quickpoll(self, ctx, arg):
        #Use RE to cut the question out of the arg String
        raw_question = re.search(r'^(.+[?])', arg)
        #Assign the capture group to options
        question = raw_question.group()
        #Use RE to cut the options out of the arg String
        raw_solutions = re.search(r'[?]\s(.+)$', arg)
        solution_group = raw_solutions.group(1)
        #Format the options into a List by splitting the String
        options = solution_group.split(',')

        if len(options) <= 1:
            await ctx.send('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await ctx.send('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['✅', '❌']
        else:
            reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(
            title=question,
            description=''.join(description)
        )
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await self.bot.add_reaction(react_message, reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await self.bot.edit_message(react_message, embed=embed)


def setup(bot):
    bot.add_cog(Gaming(bot))
