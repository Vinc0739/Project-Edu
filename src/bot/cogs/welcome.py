import discord
from discord.ext import commands
from ..config import Config
from ...classes.embeds import Embeds
from ...classes.logs import Logs, DiscordLogs

class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Neues Mitglied joint Server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(Config.welcome_channel)
        if channel is not None:
            # Embed Senden
            await channel.send(embed=Embeds.getJoinedServer(member))
            # Rollen geben    
            roles = [discord.utils.get(member.guild.roles, name=role_name) for role_name in Config.join_roles]
            await member.add_roles(*roles)
            # Logs
            await DiscordLogs.joinedServer(self.client.get_channel(Config.joins_logs_channel), member.id) # Discord
            Logs.joinedServer(member.name, member.id, '/info') # Terminal

# cog Setup
async def setup(client):
    await client.add_cog(Welcome(client))
