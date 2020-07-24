import discord
from discord.ext import commands
import json
import requests

class Destiny(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Xur(self, ctx):
        # Gets Xur info from the wtfix.gg API
        r = requests.get('https://wtfix.gg/api/xur')
        xur_info = json.loads(r.text)
        if xur_info['found']:
            await ctx.send("Xur is creepin in {} on {}".format(xur_info['zone'], xur_info['planet']))
        else:
            await ctx.send("Doesn't look like Xur is around today (at least, we haven't found him!)")


def setup(bot):
    bot.add_cog(Destiny(bot))