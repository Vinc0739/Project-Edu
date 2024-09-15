import discord
from discord.ext import commands
from ...classes.views import ControlPanelView
from ...classes.embeds import Embeds
from ...classes.prints import Prints

class EduCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    '''Commands'''
    # /botping
    @commands.hybrid_command()
    async def botping(self, ctx):
        user_ping = round(self.client.latency * 1000)
        await ctx.send(f'Der Bot hat gerade einen Ping von: **{user_ping}ms**')
        Prints.usedCommand(ctx.author.name, ctx.author.id, '/botping')
        
    # /info
    @commands.hybrid_command()
    async def info(self, ctx):
        await ctx.send(f'Informatik ist cool!')
        Prints.usedCommand(ctx.author.name, ctx.author.id, '/info')
        
    '''Dev Commands'''
    # /createlogin
    @commands.hybrid_command()
    async def createlogin(self, ctx):
        embed = Embeds.getControlPanelEmbed()
        view = ControlPanelView()
        await ctx.send(embed=embed, view=view)
        Prints.usedDevCommand(ctx.author.name, ctx.author.id, '/createlogin')
        
    # /reaload -> Kann länge dauern
    @commands.hybrid_command()
    async def reaload(self, ctx):
        await self.client.tree.sync()
        Prints.usedDevCommand(ctx.author.name, ctx.author.id, '/reaload')

# cog Setup
async def setup(client):
    await client.add_cog(EduCommands(client))