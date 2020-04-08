import datetime
import discord
from discord.ext import commands
import random
import RoseSecrets

bot = commands.Bot(command_prefix='!')
turnips_list = [0,'',0,0]
turnip_id = 0000


@bot.command()
async def commands(ctx):
    await ctx.send("Type !turnips <price> to add your turnips to the price list.")
    await ctx.send("     (without the <> ) ")
    await ctx.send("Type !turnips with no additional parameters to view the top Turnip seller today.")

@bot.command()
async def yesno(ctx):
    decision = random.choice['yes', 'no']
    await ctx.send("Your answer is " + str(decision))

@bot.command()
async def choose(ctx, *args):
    decision = random.choice(args)
    await ctx.send("I have chosen " + decision)

@bot.command()
async def turnips(ctx, arg = 0):
    global turnips_list
    today = datetime.date.today()
    today_day = today.day
    today_month = today.month
    name = str(ctx.message.author)

    if turnips_list[3] < today_day:
        turnips_list[0] = 0

    if arg == "clear":
        turnips_list.clear()
        await ctx.send("Turnip price list cleared.")
    elif arg != 0:
        price = int(arg)
        if price >= turnips_list[0]:
            turnips_list[0] = price
            turnips_list[1] = name
            turnips_list[2] = today_month
            turnips_list[3] = today_day
            await ctx.send(name + " submitted their turnips at " + str(int(arg)) + " bells.")
        else:
            await ctx.send("Your turnips at " + str(price) + " bells are less than the current top-seller.")
            await ctx.send("Type !turnips to view theirs.")

    elif arg == 0:
        if turnips_list[3] is today_day:
            #TODO: Format this announcement as a code-block in Discord.
            await ctx.send("Highest current price is: " + str(turnips_list[0]) + " bells. From: " + str(turnips_list[1]))
        else:
            await ctx.send("No turnip prices registered for today. ")

    #TODO: Reset turnip_list to original state at 5AM; announce the reset in the Switch channel
    #TODO: Send a 15-min warning message to the Switch channel at 9:45PM EST that the shop is about to close
    #TODO: Create a help command that explains the Turnip economy and why the bot exists




bot.run(RoseSecrets.Secrets.client_token)
