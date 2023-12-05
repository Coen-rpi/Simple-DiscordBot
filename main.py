import discord
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions
import requests
import json
import os


intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='c!', intents=intents)


@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('c!help'))
  print("Trash is coming for you")
  print("------------------------")

@client.command()
async def running(ctx):
    await ctx.send('this bot will be running on a RPI Zero 2W')


@client.command()
async def downtime(ctx):
  await ctx.send('The bot will be down at 30-10-2023 - 10:00-13:00 paris time due my internet provider doing maintanence.')



@client.command()
@has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'User {member} has been kicked')

@kick.error
async def kick_error(ctx, error):
  if isinstance(error, commands.Missing.Permissions):
    await ctx.send("You don't have the permissions to kick dummie!")

@client.command()
@has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
  await member.ban(reason=reason)
  await ctx.send(f'User {member} has been banned')

@ban.error
async def ban_error(ctx, error):
  if isinstance(error, commands.Missing.Permissions):
    await ctx.send("You don't have the permissions to ban dummie!")


@client.command()
async def pi(ctx):
  embed = discord.Embed(title="Raspberry Pi Zero 2W", url="https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/", description="This is the device this bot will be running on")
  embed.set_author(name="Coen", icon_url="https://pbs.twimg.com/media/FnbPrikXoA4RrKy.jpg:large")
  embed.set_thumbnail(url="https://assets.raspberrypi.com/static/51035ec4c2f8f630b3d26c32e90c93f1/2b8d7/zero2-hero.webp")
  embed.add_field(name="Main specifications", value="4xA53 cores, those are based on a ARM architecture, 64-Bit. and it has 512MB SDRAM", inline=True)

  await ctx.send(embed=embed)


@client.command()
async def music(ctx):
  embed = discord.Embed(title="Some random great music", url="https://open.spotify.com/playlist/5uiptNSaM8oh5Izj4vPKoM?si=b69c7d56f80f470a", description="This is my cool vibe playlist fir when I am gaming")
  embed.set_author(name="Coen", icon_url="https://pbs.twimg.com/media/FnbPrikXoA4RrKy.jpg:large")
  
  await ctx.send(embed=embed)




token = os.environ.get("your token")
client.run(TOKEN)
