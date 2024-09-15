import discord
from discord.ext import commands
from ...api.api_handler import getUserData
from ...classes.views import ControlPanelView
from ...classes.embeds import Embeds
from ...classes.prints import Prints
from dotenv import dotenv_values

# Keys von der .env Datei bekommen
env = dotenv_values('./src/bot/.env')

user_sessions = {}

class EduCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    '''Commands'''
    # /botping
    @commands.hybrid_command()
    async def botping(self, ctx):
        user_ping = round(self.client.latency * 1000)
        await ctx.send(f'Der Bot hat gerade einen Ping von: **{user_ping}ms**')
        Prints.usedCommand(ctx.author.name, '/botping')
        
    # /info
    @commands.hybrid_command()
    async def info(self, ctx):
        await ctx.send(f'Informatik ist cool!')
        Prints.usedCommand(ctx.author.name, '/info')
        
    '''Dev Commands'''
    # /createlogin
    @commands.hybrid_command()
    async def createlogin(self, ctx):
        embed = Embeds.getControlPanelEmbed()
        view = ControlPanelView()
        await ctx.send(embed=embed, view=view)
        Prints.usedDevCommand(ctx.author.name, '/createlogin')
        
    # /reaload -> Kann länge dauern
    @commands.hybrid_command()
    async def reaload(self, ctx):
        await self.client.tree.sync()
        Prints.usedDevCommand(ctx.author.name, '/reaload')

# cog Setup
async def setup(client):
    await client.add_cog(EduCommands(client))