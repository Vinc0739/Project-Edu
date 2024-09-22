import discord
from discord.ext import commands
from ...api.api_handler import getUserData
from ...db.database import Database
from ...classes.functions import Functions
from ...classes.logs import Logs, DiscordLogs
from ..bot_config import Config


class ApiConnection(commands.Cog):
    def __init__(self, client):
        self.client = client


    """API Commands"""
    
    # /schüleranzahl
    @commands.hybrid_command(description='Gibt die Anzahl an Schülern aus, die zurzeit in Edupage eingetragen sind')
    async def schüleranzahl(self, ctx):
        # Überprüfen ob der jetztige Kanal auch der Kanal des Users ist
        current_channel = ctx.interaction.channel_id
        user_channel = Functions.getUserChannel(ctx.author.id)
        if user_channel == current_channel:
            # User Daten bekommen
            user_edu = Functions.getUserEdu(ctx.author.id)
            # Schüleranzhal bekommen
            student_count = len(user_edu.get_all_students())
            # Antwort
            await ctx.send(f'Es sind zurzeit **{student_count}** Schüler in EduPage eingetragen')
            # Logs
            await DiscordLogs.usedApiCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/schüleranzahl' ) # Discord
            Logs.usedApiCommand(ctx.author.name, ctx.author.id, '/schüleranzahl') # Terminal
        else:
            await ctx.interaction.response.send_message(ephemeral=True, content='Bitte benutze deinen eigenen Kanal dafür')


async def setup(client):
    await client.add_cog(ApiConnection(client))
