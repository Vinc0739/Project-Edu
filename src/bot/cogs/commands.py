import discord
from discord.ext import commands
from ...api.api_handler import getUserData
from ...configs.views import ControlPanelView
from ...configs.embeds import Embeds
from ...configs.prints import Prints
from dotenv import dotenv_values

# Keys von der .env Datei bekommen
env = dotenv_values('./src/configs/.env')

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