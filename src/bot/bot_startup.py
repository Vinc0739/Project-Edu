import os
import asyncio
import discord
from dotenv import dotenv_values
from discord.ext import commands
from ..classes.prints import Prints

# Keys von der .env Datei bekommen
env = dotenv_values('./src/bot/.env')

# Bot erstellen
client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

# alle cog Extensions laden
async def load_cogs():
    Prints.botStarting()
    for cog_name in os.listdir("./src/bot/cogs"):
        if cog_name.endswith(".py"):
            Prints.loadingCog(cog_name)
            await client.load_extension(f"src.bot.cogs.{cog_name[:-3]}")

# On Ready Event zum Commands syncen und Aktivität setzten
@client.event
async def on_ready():
    Prints.botLoggedIn(client.user.name)
    await client.change_presence(activity=discord.activity.Game(name='Project Edu'))
    await client.tree.sync()
    
# Bot Start
async def main():
    async with client:
        await load_cogs()
        await client.start(env['BOT_TOKEN'])
asyncio.run(main())