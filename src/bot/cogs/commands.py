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
    # /createcontrolpanel
    @commands.hybrid_command()
    async def createcontrolpanel(self, ctx):
        await Functions.sendControlPanelEmbed(self.client.get_channel(Config.control_panel_channel))
        # Commands Logs
        await DiscordLogs.usedDevCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/createcontrolpanel' ) # Discord
        Logs.usedDevCommand(ctx.author.name, ctx.author.id, '/createcontrolpanel') # Terminal
        # Control Panel Logs
        await DiscordLogs.newControlPanel(self.client.get_channel(Config.control_panel_logs_channel)) # Discord
        Logs.newControlPanel() # Terminal
        
    # /reaload -> Kann länge dauern
    @commands.hybrid_command()
    async def reaload(self, ctx):
        await self.client.tree.sync()
        # Logs
        await DiscordLogs.usedDevCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/reaload' ) # Discord
        Logs.usedDevCommand(ctx.author.name, ctx.author.id, '/reaload') # Terminal

# cog Setup
async def setup(client):
    await client.add_cog(EduCommands(client))