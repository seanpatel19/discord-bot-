import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from apikey import *
import os

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

initial_extensions = []
for filename in os.listdir('./cogs/'):
    if filename.endswith('.py'):
        initial_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
    for extension in initial_extensions:
        client.load_extension(f'cogs.{extension}')





client.run(key)