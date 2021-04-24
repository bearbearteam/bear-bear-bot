from discord.ext import commands
import discord
import json
import requests
import random
from random import randint
import asynciox`  
bot = commands.Bot(command_prefix='!')

@bot.command()
async def lol(ctx,lol):
  print(lol)
    
@bot.event  
async def on_ready():
        print('Logged in as')
        print(bot.user.name)   
        print(bot.user.id)
        print('------')
        await bot.change_presence(activity=discord.Game('bear bear team and visual studio code'),status=discord.Status.idle)
        channel = bot.get_channel(828506340573184021)
        em = discord.Embed(title="bot is online", description="USE COMMANDS" , color=0x00ff00)
        em.add_field(name="subscribe to bear bear team", value="https://www.youtube.com/channel/UCBnyGCWTYyeI9ebOvQzKdKw")
        channel = bot.get_channel(828649632606715904)
        await channel.send(embed=em)
@bot.command()
async def store(ctx,item):
  storeitem=item
  with open("item.json","r") as file:
    x = json.load(file)
  x["item"]=storeitem
  with open ("item.json","w") as file:
    json.dump(x,file,indent=4)
  await ctx.send('done')
@bot.command()
async def stop(ctx):
  await bot.logout()  
@bot.command()
async def unstore(ctx):
  with open("item.json", "w") as outfile: 
    f = open('item.json',) 
  data = json.loads(f) 
  for i in data['item']: 
    print(i)
    ctx.send(i)
@bot.command()
async def hi(ctx):
  await message.channel.send('hi')
@bot.command()
async def guess(ctx):




bot.run('YOURTOKEN')