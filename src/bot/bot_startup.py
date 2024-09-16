import os
import asyncio
import discord
from discord.ext import commands
from dotenv import dotenv_values
from .config import Config
from ..classes.logs import Logs, DiscordLogs

# Keys von der .env Datei bekommen
env = dotenv_values('./src/bot/.env')

# Bot erstellen
client = commands.Bot(command_prefix='.', intents=Config.bot_intents)

# alle cog Extensions laden
async def load_cogs():
    # await Logs.botStarting()
    for cog_name in os.listdir("./src/bot/cogs"):
        if cog_name.endswith(".py"):
            Logs.loadingCog(cog_name)
            await client.load_extension(f"src.bot.cogs.{cog_name[:-3]}")

# On Ready Event zum Commands syncen und Aktivität setzten
@client.event
async def on_ready():
    # Bot Status ändern
    await client.change_presence(activity=discord.activity.Game(name='Project Edu'))
    
    # Logs
    await DiscordLogs.botStarting(client.get_channel(Config.logs_channel)) # Discord
    Logs.botLoggedIn(client.user.name) # Terminal
    
    # Command Tree syncen
    await client.tree.sync()
    
# Bot Start
async def main():
    async with client:
        await load_cogs()
        await client.start(env['BOT_TOKEN'])
asyncio.run(main())