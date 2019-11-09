from datetime import datetime
from dateutil import tz
import discord
from discord.ext import commands
import asyncio

botPrefix = "BOT_PREFIX"
botToken = "BOT_TOKEN"

bot=commands.Bot(command_prefix=botPrefix)
t = None #change to your timezone like "America/New_York"
timeZone = tz.gettz(t) if t is not None else tz.tzutc()


@bot.command()
async def start(ctx):
    await ctx.guild.me.edit(nick=datetime.now().astimezone(timeZone).strftime("%a %I:%M %p"))
    await asyncio.sleep(300) #changes time every 5 minutes
    await ctx.guild.me.edit(nick=datetime.now().astimezone(timeZone).strftime("%a %I:%M %p"))

bot.run(botToken)
