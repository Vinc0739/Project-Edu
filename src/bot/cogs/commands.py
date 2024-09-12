import discord
from discord.ext import commands
from dotenv import dotenv_values


class EduCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    # /syncc -> Kann auch mal lange dauern
    @commands.hybrid_command()
    async def syncc(self, ctx):
        await self.client.tree.sync()
        print('\x1b[1;33;41m' + 'Synced Commands' + '\x1b[0m')
        await ctx.send('Commands wurden gesynct')
        usedCommand(ctx.author.name, '/syncc')

    # /botping
    @commands.hybrid_command()
    async def botping(self, ctx):
        user_ping = round(self.client.latency * 1000)
        await ctx.send(f'Der Bot hat gerade einen Ping von: {user_ping}ms')
        usedCommand(ctx.author.name, '/botping')

async def setup(client):
    await client.add_cog(EduCommands(client))
    
def usedCommand(user, command):
    print('\x1b[6;33;40m' + user + '\x1b[0m' + '\x1b[6;30;40m' + f' executed the command ' + '\x1b[0m' + '\x1b[6;33;40m' + command + '\x1b[0m')