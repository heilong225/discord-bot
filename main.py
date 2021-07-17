import discord
from discord.ext import commands
import json

with open('set.json','r',encoding='utf8') as jfile:
    data =json.load(jfile)

bot = commands.Bot(command_prefix="!")  

@bot.event
async def on_ready():
    print("on ready")


#@bot.command()
#async def ping(ctx):
#    await ctx.send(bot.latency)


bot.run(data['Token'])