import discord
from discord.ext import commands
from ..config import Config
from ...classes.views import ControlPanelView
from ...classes.embeds import Embeds
from ...classes.logs import Logs, DiscordLogs

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
        await DiscordLogs.usedCommand(self.client.get_channel(Config.logs_channel), ctx.author.id, '/botping' ) # Discord
        Logs.usedCommand(ctx.author.name, ctx.author.id, '/botping') # Terminal
        
    # /info
    @commands.hybrid_command()
    async def info(self, ctx):
        await ctx.send(f'Informatik ist cool!')
        # Logs
        await DiscordLogs.usedCommand(self.client.get_channel(Config.logs_channel), ctx.author.id, '/info' ) # Discord
        Logs.usedCommand(ctx.author.name, ctx.author.id, '/info') # Terminal
        
    '''Dev Commands'''
    # /createlogin
    @commands.hybrid_command()
    async def createlogin(self, ctx):
        embed = Embeds.getControlPanelEmbed()
        view = ControlPanelView()
        await ctx.send(embed=embed, view=view)
        # Logs
        await DiscordLogs.usedDevCommand(self.client.get_channel(Config.logs_channel), ctx.author.id, '/createlogin' ) # Discord
        Logs.usedDevCommand(ctx.author.name, ctx.author.id, '/createlogin') # Terminal
        
    # /reaload -> Kann länge dauern
    @commands.hybrid_command()
    async def reaload(self, ctx):
        await self.client.tree.sync()
        # Logs
        await DiscordLogs.usedDevCommand(self.client.get_channel(Config.logs_channel), ctx.author.id, '/reaload' ) # Discord
        Logs.usedDevCommand(ctx.author.name, ctx.author.id, '/reaload') # Terminal

# cog Setup
async def setup(client):
    await client.add_cog(EduCommands(client))