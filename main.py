from asyncore import loop
import random
import time
import discord
from discord.ext import commands
import os
from pystyle import *
blue = Col.blue
cyan = Col.cyan



#------------CONFIG------------
TOKEN = ""
prefix = "."
allowed = 1137704471154143354
title = "Cloud Pfps"
desc = ""
footer = "github.com/Bobbbyyyyy"
color = 0x92cace
banner = """
┏  ┏┓┓     ┓  ┓
┃  ┃ ┃┏┓┓┏┏┫  ┃
┛  ┗┛┗┗┛┗┻┗┻  ┗

"""
#------------------------------


os.system("cls")
os.system(f'title Cloud Pfps / Made by Bobbyyy')
System.Size(70, 20)
Cursor.HideCursor()
tostop = 0
intents = discord.Intents.all()
pfpbot = commands.Bot(command_prefix=prefix,intents=intents)

def randnum(fname):
    lines=open(fname).read().splitlines()
    return random.choice(lines)

@pfpbot.event
async def on_ready():
    os.system('cls')
    print(Colorate.Horizontal(Colors.blue_to_cyan, Center.XCenter(banner), 1))
    print(cyan, Center.XCenter(f"Connected to {pfpbot.user}"))

@pfpbot.command()
async def stop(ctx):
  global tostop
  if ctx.author.id == allowed:
    tostop += 1
    await ctx.reply("`✅` | **Stopped AutoPfP**")
    print(cyan, Center.XCenter(f"Stopped AutoPfP"))
  else:
    await ctx.reply("`⛔` | **You are not allowed to do that**")

@pfpbot.command()
async def start(ctx):
    global tostop
    if ctx.author.id == allowed:
        tostop = 0
        await ctx.reply("`✅` | **Started AutoPfP**")
        print(cyan, Center.XCenter(f"Started AutoPfP"))
        while tostop == 0:
            
            embed = discord.Embed(title = title,description = desc,color = color)
            embed.set_image(url = randnum('pfps.txt'))
            embed.set_footer(text = footer)
            await ctx.send(embed=embed)
            time.sleep(3)
    else:
        await ctx.send("`⛔` | **You are not allowed to do that**")

pfpbot.run(TOKEN)
