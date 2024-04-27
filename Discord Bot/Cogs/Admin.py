import discord
from discord.ext import commands
from discord import Member, Role, TextChannel
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

@commands.command
async def on_message(message):
    if message.content == # add information from forbidden list
        await message.delete()
        await message.channel.send('Comment or Link not authorized in this channel')

@commands.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f' User {member} has been removed from the channel')
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You cannot kick people')

@commands.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def addRole(self, ctx, user: discord.member, *, role: discord.Role):
    if role in user.roles:
        await ctx.send(f"{user.mention} already has {role}")
    else:
        await user.add_roles(role)
        await ctx.send(f"Added {role} to {user.mention}")


@addRole.error
async def role_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cannot use this command!")


@commands.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def removeRole(self, ctx, user: discord.member, *, role: discord.Role):
    if role in user.roles:
        await user.remove_roles(role)
        await ctx.send(f"Removed {role} from {user.mention}")
    else:

        await ctx.send(f"{user.mention} does not have {role}")


@removeRole.error
async def role_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You cannot use this command!")

