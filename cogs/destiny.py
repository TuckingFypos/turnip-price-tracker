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
        # Loads the returned JSON to a python dict
        xur_info = json.loads(r.text)
        # Checks if Xur is found
        if xur_info['found']:
            # If found, prints Xur's location to a Discord Embed
            embed = discord.Embed(
                title='Xur Located',
                colour=discord.Colour.green()
            )
            embed.add_field(name='Planet:', value=str(xur_info['planet']), inline=True)
            embed.add_field(name='Zone:', value=str(xur_info['zone']), inline=True)
            await ctx.send(embed=embed)
        else:
            # No Xur? No problem
            embed = discord.Embed(
                title='Xur not found',
                colour=discord.Color.dark_green()
            )
            embed.add_field(name='Planet:', value="unknown", inline=True)
            embed.add_field(name='Zone:', value="unknown", inline=True)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Destiny(bot))