import discord
from ..bot.bot_config import Config
from ..db.database import Database
from .embeds import Embeds
from .logs import Logs, DiscordLogs
from .modals import LoginModal

class UserPanelView(discord.ui.View):
    
    # Login Button
    @discord.ui.button(label='Login', style=discord.ButtonStyle.green)
    async def login(self, interaction: discord.Interaction, button: discord.ui.Button):
        #Modal (Formular) laden
        modal = LoginModal()
        await interaction.response.send_modal(modal)
        
    # Logout Button
    @discord.ui.button(label='Logout', style=discord.ButtonStyle.red)
    async def logout(self, interaction: discord.Interaction, button: discord.ui.Button):
        # User von Db bekommen
        db = Database()
        user = db.getUser(interaction.user.id)
        if user == [] or user == None:
            await interaction.response.send_message(ephemeral=True, embed=Embeds.getNotLogedIdEmbed())
            # Logs
            await DiscordLogs.userNotLogedIn(interaction.guild.get_channel(Config.user_panel_logs_channel), interaction.user.id) # Discord
            Logs.userNotLogedIn(interaction.user.name, interaction.user.id) # Terminal
        else:
            user_channel_id = user[4]
            # user von db löschen
            db.deleteUser(interaction.user.id, interaction.user.name)
            # Channel des Users löschen
            user_channel = interaction.guild.get_channel(user_channel_id)
            await user_channel.delete()
            # Antworten
            await interaction.response.send_message(ephemeral=True, embed=Embeds.getLogoutEmbed())
            # Logs
            await DiscordLogs.userLogout(interaction.guild.get_channel(Config.user_panel_logs_channel), interaction.user.id) # Discord
            Logs.userLogout(interaction.user.name, interaction.user.id) # Terminal
        