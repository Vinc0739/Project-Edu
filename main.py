#imports
from dotenv import dotenv_values
from utils import getColours
import discord
from discord.ext import commands

#load env
env = dotenv_values(".env")

#create the bot
bot = commands.Bot(command_prefix='.', intents=discord.Intents.all())

#EVENTS
@bot.event
async def on_ready():
    print('logging in as ' + '\x1b[1;32;40m' + bot.user.name + '\x1b[0m')
    await bot.change_presence(activity=discord.activity.Game(name='EduPage Studenplan'))


#run the bot
bot.run(env['BOT_TOKEN'])