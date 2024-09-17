import discord
from discord.ext import commands
from ..config import Config
from ...classes.logs import Logs, DiscordLogs
from ...classes.functions import Functions
from ...classes.embeds import Embeds

class EduCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    '''Commands'''
    # /botping
    @commands.hybrid_command()
    async def botping(self, ctx):
        user_ping = round(self.client.latency * 1000)
        await ctx.send(f'Der Bot hat gerade einen Ping von: **{user_ping}ms**')
        # Logs
        await DiscordLogs.usedCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/botping' ) # Discord
        Logs.usedCommand(ctx.author.name, ctx.author.id, '/botping') # Terminal
        
    # /info
    @commands.hybrid_command()
    async def info(self, ctx):
        await ctx.send(f'Informatik ist cool!')
        # Logs
        await DiscordLogs.usedCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/info' ) # Discord
        Logs.usedCommand(ctx.author.name, ctx.author.id, '/info') # Terminal
        
    # /projectedu
    @commands.hybrid_command()
    async def projectedu(self, ctx):
        await ctx.send(f'...')
        # Logs
        await DiscordLogs.usedCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/projectedu' ) # Discord
        Logs.usedCommand(ctx.author.name, ctx.author.id, '/projectedu') # Terminal
        
    '''Dev Commands'''
    # /createuserpanel
    @commands.hybrid_command()
    async def createuserpanel(self, ctx):
        await Functions.sendUserPanelEmbed(self.client.get_channel(Config.user_panel_channel))
        # Commands Logs
        await DiscordLogs.usedDevCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/createuserpanel' ) # Discord
        Logs.usedDevCommand(ctx.author.name, ctx.author.id, '/createuserpanel') # Terminal
        # User Panel Logs
        await DiscordLogs.newUserPanel(self.client.get_channel(Config.user_panel_logs_channel)) # Discord
        Logs.newUserPanel() # Terminal
        
    # /reaload -> Kann länge dauern
    @commands.hybrid_command()
    async def reaload(self, ctx):
        await self.client.tree.sync()
        # Logs
        await DiscordLogs.usedDevCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/reaload' ) # Discord
        Logs.usedDevCommand(ctx.author.name, ctx.author.id, '/reaload') # Terminal
        
    # /stopbot -> Stop den Bot
    @commands.hybrid_command()
    async def stopbot(self, ctx):
        await ctx.send('Der Bot wurde erfolgreich gestopt.')
        # Commands Logs
        await DiscordLogs.usedDevCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/stopbot' ) # Discord
        Logs.usedDevCommand(ctx.author.name, ctx.author.id, '/stopbot') # Terminal
        # Bot Stop Logs
        await DiscordLogs.botStopped(self.client.get_channel(Config.system_logs_channel), ctx.author.id) # Discord
        Logs.botStopped() # Terminal
        # Stop Bot
        exit()

# cog Setup
async def setup(client):
    await client.add_cog(EduCommands(client))