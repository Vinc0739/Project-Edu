import discord
from discord.ext import commands
from dotenv import dotenv_values

# Keys von der .env Datei bekommen
env = dotenv_values('./src/bot/.env')

class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Neues Mitglied joint Event Listener
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        print('\x1b[7;32;40m' + 'New Member: ' + '\x1b[0m' + '\x1b[7;30;40m' + member.name + '\x1b[0m')
        if channel is not None:
            await channel.send(f'Hallo {member.mention}.')

# cog Setup
async def setup(client):
    await client.add_cog(Welcome(client))
