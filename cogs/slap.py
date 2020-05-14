import discord
import json
import random
from discord.ext import commands

jsonpath =  "playbook.txt"

class Slap(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def initialize(self, ctx):
		print("")

	@commands.command()
	async def slap(self, ctx, member: discord.Member):
		#initialize both players
		player1 = ctx.author.name
		player2 = member.name
		#load the game database
		# with open (jsonpath) as player_database:
		arsenal_roll = random.randrange(0, 3)
		counter_roll = random.randrange(0, 3)

		small_weapons = ["a rusty spoon", "a smelly fish", "a wet noodle", "a broken bottle", "a paper fan"]
		medium_weapons = ["a baseball bat", "consecutive normal punches", "a stone axe", "a hidden blade", "a mean backhand"]
		large_weapons = ["the mastersword", "a hammer of sol", "Thunderfury, blessed blade of The Windseeker", "a lightsaber" ]

		if arsenal_roll is 1:
			p1weapon = random.choice(small_weapons)
		elif arsenal_roll is 2:
			p1weapon = random.choice(medium_weapons)
		if arsenal_roll is 3:
			p1weapon = random.choice(large_weapons)

		if counter_roll is 1:
			p2weapon = random.choice(small_weapons)
		if counter_roll is 2:
			p2weapon = random.choice(medium_weapons)
		if counter_roll is 3:
			p2weapon = random.choice(large_weapons)

		if arsenal_roll > 0:
			if arsenal_roll < counter_roll:
				await ctx.send("{} attempts to slap {} with {}...").format()

			elif arsenal_roll > counter_roll:
				await ctx.send("{} slaps {} with {}.".format(player1, player2, weapon))

			elif arsenal_roll == counter_roll:
				await ctx.send("")
		else:
			await ctx.send("{} attempted to slap {}, but they missed.".format(player1, player2))
			
def setup(bot):
	bot.add_cog(Slap(bot))
