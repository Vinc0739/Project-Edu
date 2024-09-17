import discord
from ..bot.config import Config
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
        # in db speichern
        db = Database()
        user = db.getUser(interaction.user.id)
        if user == [] or user == None:
            # neuen Kanal erstellen nur für den user
            guild = interaction.guild
            overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False), guild.me: discord.PermissionOverwrite(read_messages=True), interaction.user: discord.PermissionOverwrite(read_messages=True)}
            channel = await guild.create_text_channel(name=f"🟣︱{interaction.user.name}", overwrites=overwrites, category=await guild.fetch_channel(1283384196253089883))
            await channel.send(embed=Embeds.getChannelCreatedEmbed(self.username.value, self.password.value))
            # neuen User in Db anlegen
            db.createNewUser(interaction.user.name, interaction.user.id, self.username.value, self.password.value, channel.id)
            # Embed Antwort
            await interaction.response.send_message(ephemeral=True, embed=Embeds.getLoginEmbed(channel.id))
            # Logs
            await DiscordLogs.userLogin(interaction.guild.get_channel(Config.user_panel_logs_channel), interaction.user.id) # Discord
            Logs.userLogin(interaction.user.name, interaction.user.id) # Terminal
        else:
            await interaction.response.send_message(ephemeral=True, embed=Embeds.getAlreadyLogedInEmbed())
            # Logs
            await DiscordLogs.alreadyLogedIn(interaction.guild.get_channel(Config.user_panel_logs_channel), interaction.user.id) # Discord
            Logs.alreadyLogedIn(interaction.user.name, interaction.user.id) # Terminal
        
    # Bei Error
    async def on_error(self, interaction: discord.Interaction, error):
        await interaction.response.send_message(ephemeral=True, embed=Embeds.getLoginErrorEmbed())
        Logs.loginError(interaction.user.name, interaction.user.id, error)
        # Logs
        await DiscordLogs.loginError(interaction.guild.get_channel(Config.user_panel_logs_channel), interaction.user.id, error) # Discord
        Logs.loginError(interaction.user.name, interaction.user.id, error) # Terminal