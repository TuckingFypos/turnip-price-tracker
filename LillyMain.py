import os
import RoseSecrets
from discord.ext import commands

bot = commands.Bot(command_prefix = '!', case_insensitive=True)

# Loads all Cogs in cogs folder
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

# Discord Bot Token
bot.run(RoseSecrets.Secrets.client_token)
