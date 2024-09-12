import discord
from discord.ext import commands
from dotenv import dotenv_values

env = dotenv_values(".env")

class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        print('\x1b[7;32;40m' + 'New Member: ' + '\x1b[0m' + '\x1b[7;30;40m' + member.name + '\x1b[0m')
        if channel is not None:
            await channel.send(f'Hallo {member.mention}.')

async def setup(client):
    await client.add_cog(Welcome(client))
