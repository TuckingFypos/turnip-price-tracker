import discord
from discord.ext import commands
import datetime
import random
import time

turnips_list = [0, '', 0, 0, 0]
turnip_id = 0000


class Gaming(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    # Main Turnips Function
    @commands.group(description='Turnips Econonmy', name="turnips", invoke_without_command=True)
    async def turnips(self, ctx, arg=0):
        global turnips_list
        today = datetime.date.today()
        today_day = today.day
        today_month = today.month
        today_hour = time.localtime().tm_hour
        name = str(ctx.message.author)

        if turnips_list[3] < today_day:
            turnips_list[0] = 0
        # AM PM reset, ensures any submission after noon is accepted when compared to a submission made before noon.
        if (turnips_list[4] < 12) & (today_hour >= 12):
            turnips_list[0] = 0
            turnips_list[3] = 0

        # User Turnip price submission
        if arg != 0:
            price = int(arg)

            if price >= turnips_list[0]:
                turnips_list[0] = price
                turnips_list[1] = name
                turnips_list[2] = today_month
                turnips_list[3] = today_day
                turnips_list[4] = today_hour
                await ctx.send(name + " submitted their turnips at " + str(int(arg)) + " bells.")
            else:
                await ctx.send("Your turnips at " + str(price) + " bells are less than the current top-seller.")
                await ctx.send("Type !turnips to view theirs.")

        elif arg == 0:
            if turnips_list[3] is today_day:
                # Embed
                embed = discord.Embed(
                    title='Highest Current Price',
                    colour=discord.Colour.blue()
                )
                embed.set_thumbnail(url='https://vignette.wikia.nocookie.net/animalcrossing/images/8/85/Daisy_Mae.png')
                embed.add_field(name='Price in Bells:', value=str(turnips_list[0]), inline=True)
                embed.add_field(name='From:', value=str(turnips_list[1]), inline=True)
                await ctx.send(embed=embed)
            else:
                await ctx.send("No turnip prices registered for today. ")

    # Sets turnips_list to its initial values
    @turnips.group(hidden=True, invoke_without_command=True)
    @commands.is_owner()
    async def clear(self, ctx):
        self.bot.unload_extension('cogs.turnips')
        self.bot.load_extension('cogs.turnips')
        await ctx.send("The turnip prices have been cleared.")

    # Turnips Help Commands
    @turnips.group(invoke_without_command=True)
    async def help(self, ctx):
        await ctx.send("Can't help you yet.")

        # TODO: Send a 15-min warning message to the Switch channel at 9:45PM EST that the shop is about to close
        # TODO: Create a help command that explains the Turnip economy and why the bot exists


def setup(bot):
    bot.add_cog(Gaming(bot))
