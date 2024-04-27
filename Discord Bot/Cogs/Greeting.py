import discord
from discord.ext import commands

class Greetings(commands.Cog):
    def __init__(self, client):
        self.client = client

@commands.command()
async def on_ready():
    print('Jail Bot is ready.')

@commands.command()
async def on_member_remove(member):
    # add channel information
    channel = client.get_channel()
    await channel.send(f'{user.mention} has left the server')

@commands.command(pass_context=True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send('You are not in a voice channel')

@commands.command(pass_context=True)
async def leave(ctx):
    if ctx.author.voice:
        await ctx.guild.voice.channel.disconnect()
        await ctx.send('I have left the voice channel')
    else:
        await ctx.send('I am not in a voice channel')