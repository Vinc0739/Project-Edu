import base64
import discord
from ..bot.bot_config import Config
from ..db.database import Database
from .embeds import Embeds
from .logs import Logs, DiscordLogs

class LoginModal(discord.ui.Modal, title='Gib bitte deine EduPage Benutzerdaten ein'):
    username = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label='Benutzername',
        required=True,
        placeholder='dein Benutzername'
    )
    
    password = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label='Passwort',
        required=True,
        placeholder='dein Passwort'
    )
    
    # Bei Absenden
    async def on_submit(self, interaction: discord.Interaction):
        # neuen Kanal erstellen nur für den user
        guild = interaction.guild
        overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False), guild.me: discord.PermissionOverwrite(read_messages=True), interaction.user: discord.PermissionOverwrite(read_messages=True)}
        channel = await guild.create_text_channel(name=f"🟣︱{interaction.user.name}", overwrites=overwrites, category=await guild.fetch_channel(1283384196253089883))
        await channel.send(embed=Embeds.getChannelCreatedEmbed())
        # Codieren von Passwort und Username
        byte_username = self.username.value.encode('utf-8')
        byte_password = self.password.value.encode('utf-8')
        encoded_username = base64.b64encode(byte_username)
        encoded_password = base64.b64encode(byte_password)
        # neuen User in Db anlegen
        db = Database()
        db.createNewUser(interaction.user.name, interaction.user.id, encoded_username, encoded_password, channel.id)
        # Benutzer Rolle geben
        member = guild.get_member(interaction.user.id)
        roles = [discord.utils.get(guild.roles, name=Config.user_role)]
        await member.add_roles(*roles)
        # Embed Antwort
        await interaction.response.send_message(ephemeral=True, embed=Embeds.getLoginEmbed(channel.id))
        # Logs
        await DiscordLogs.userLogin(interaction.guild.get_channel(Config.user_panel_logs_channel), interaction.user.id) # Discord
        Logs.userLogin(interaction.user.name, interaction.user.id) # Terminal
        
    # Bei Error
    async def on_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message(ephemeral=True, embed=Embeds.getLoginErrorEmbed())
        # Logs
        await DiscordLogs.loginError(interaction.guild.get_channel(Config.user_panel_logs_channel), interaction.user.id, error) # Discord
        Logs.loginError(interaction.user.name, interaction.user.id, error) # Terminal


class UpdateDataModal(discord.ui.Modal, title='Gib bitte deine EduPage Benutzerdaten ein'):
    username = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label='Benutzername',
        required=True,
        placeholder='dein Benutzername'
    )
    
    password = discord.ui.TextInput(
        style=discord.TextStyle.short,
        label='Passwort',
        required=True,
        placeholder='dein Passwort'
    )
    
    # Bei Absenden
    async def on_submit(self, interaction: discord.Interaction):
        # Codieren von Passwort und Username
        byte_username = self.username.value.encode('utf-8')
        byte_password = self.password.value.encode('utf-8')
        encoded_username = base64.b64encode(byte_username)
        encoded_password = base64.b64encode(byte_password)
        # neuen User in Db anlegen
        db = Database()
        db.updateUser(interaction.user.name, interaction.user.id, encoded_username, encoded_password)
        # Embed Antwort
        await interaction.response.send_message(ephemeral=True, embed=Embeds.getUpdatedDataEmbed())
        # Logs
        await DiscordLogs.dataUpdate(interaction.guild.get_channel(Config.user_panel_logs_channel), interaction.user.id) # Discord
        Logs.dataUpdate(interaction.user.name, interaction.user.id) # Terminal
        
    # Bei Error
    async def on_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message(ephemeral=True, embed=Embeds.getLoginErrorEmbed())
        # Logs
        await DiscordLogs.dataUpdateError(interaction.guild.get_channel(Config.user_panel_logs_channel), interaction.user.id, error) # Discord
        Logs.dataUpdateError(interaction.user.name, interaction.user.id, error) # Terminal