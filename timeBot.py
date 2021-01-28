from datetime import datetime
from dateutil import tz
import discord
from discord.ext import commands
import asyncio

botPrefix = "" #Your Prefix Here
botToken = "" #Your Bot Token Here
GUILD_ID = ""

bot = commands.Bot(command_prefix=botPrefix)
t = "Asia/Dubai"
timeZone = tz.gettz(t) if t else tz.tzutc()


@bot.event
async def on_ready():
    print("Logged in as "+bot.user.name)
    while True:
      await bot.get_guild(GUILD_ID).me.edit(nick=datetime.now().astimezone(timeZone).strftime("%a %I:%M %p"))
      await asyncio.sleep(300) #changes time every 5 minutes
      await bot.get_guild(GUILD_ID).me.edit(nick=datetime.now().astimezone(timeZone).strftime("%a %I:%M %p"))


bot.run(botToken)
