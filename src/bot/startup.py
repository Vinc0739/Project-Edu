import os
import asyncio
import discord
from dotenv import dotenv_values
from discord.ext import commands

env = dotenv_values(".env")

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

async def load_cogs():
    for filename in os.listdir("./src/bot/cogs"):
        if filename.endswith(".py"):
            print('\x1b[3;30;40m' + 'started cog with name ' + '\x1b[0m' + '\x1b[1;34;40m' + filename + '\x1b[0m')
            await client.load_extension(f"bot.cogs.{filename[:-3]}")

@client.event
async def on_ready():
    print('\x1b[3;30;40m' + 'bot logged in as ' + '\x1b[0m' + '\x1b[1;35;40m' + client.user.name+ '\x1b[0m')
    await client.change_presence(activity=discord.activity.Game(name='Project Edu'))
    await client.tree.sync()

async def main():
    async with client:
        await load_cogs()
        await client.start(env['BOT_TOKEN'])
        
asyncio.run(main())