import discord
from discord.ext import commands
from .embeds import Embeds
from .prints import Prints

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
        await channel.send(embed=Embeds.getChannelCreatedEmbed(self.username.value, self.password.value))
        
        await interaction.response.send_message(ephemeral=True, embed=Embeds.getLoginEmbed(channel.id))
        Prints.userLogin(interaction.user.name)
        
    # Bei Error
    async def on_error(self, interaction: discord.Interaction):
        await interaction.response.send_message(ephemeral=True, embed=Embeds.getLoginErrorEmbed())