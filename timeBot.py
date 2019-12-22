from datetime import datetime
from dateutil import tz
import discord
from discord.ext import commands
import asyncio

botPrefix = "time!"
botToken = "NjU3NjgyMzQ2MzE2NjYwNzQ2.Xf0wbw.Lt3tC7_KspsV8lDWB3hh4DPtRTI"

bot=commands.Bot(command_prefix=botPrefix)
t = "Asia/Dubai"
timeZone = tz.gettz(t) if t is not None else tz.tzutc()


@bot.command()
async def start(ctx):
    while True:
      await ctx.guild.me.edit(nick=datetime.now().astimezone(timeZone).strftime("%a %I:%M %p"))
      await asyncio.sleep(300) #changes time every 5 minutes
      await ctx.guild.me.edit(nick=datetime.now().astimezone(timeZone).strftime("%a %I:%M %p"))

bot.run(botToken)
