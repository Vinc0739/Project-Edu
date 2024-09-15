import discord
from discord.ext import commands
from dotenv import dotenv_values
from ...classes.embeds import Embeds
from ...classes.prints import Prints

# Keys von der .env Datei bekommen
env = dotenv_values('./src/bot/.env')

# Variablen
welcome_channel = 1281634156778094602
join_roles = ['↣ | Mitglied', '-- Team Roles --', '-- Custom Roles --', '-- User Roles--', '-- Permission Roles --']


class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Neues Mitglied joint Server
    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(welcome_channel)
        if channel is not None:
            # Embed Senden
            await channel.send(embed=Embeds.getJoinedServer(member))
            
            # Rollen geben    
            roles = [discord.utils.get(member.guild.roles, name=role_name) for role_name in join_roles]
            await member.add_roles(*roles)
            
            Prints.joinedServer(member.name, member.id)

# cog Setup
async def setup(client):
    await client.add_cog(Welcome(client))
