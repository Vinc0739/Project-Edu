import discord
from discord.ext import commands
from .embeds import Embeds
from .prints import Prints
from ..api.api_handler import getUserData

class ControlPanelView(discord.ui.View):
    
    # Login Button
    @discord.ui.button(label='Login', style=discord.ButtonStyle.green)
    async def login(self, interaction: discord.Interaction, button: discord.ui.Button):
        #Edupage Daten bekommen
        api_session_data = getUserData()
        if api_session_data:
            # neuen Kanal erstellen nur für den user
            guild = interaction.guild
            overwrites = {guild.default_role: discord.PermissionOverwrite(read_messages=False), guild.me: discord.PermissionOverwrite(read_messages=True), interaction.user: discord.PermissionOverwrite(read_messages=True)}
            channel = await guild.create_text_channel(name=f"🟣︱{interaction.user.name}", overwrites=overwrites, category=await guild.fetch_channel(1283384196253089883))
        else:
            await interaction.response.send_message(ephemeral=True, embed=Embeds.getLoginErrorEmbed())
        
        await interaction.response.send_message(ephemeral=True, embed=Embeds.getLoginEmbed(channel.id))
        Prints.userLogin(interaction.user.name)
        
    # Logout Button
    @discord.ui.button(label='Logout', style=discord.ButtonStyle.red)
    async def logout(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(ephemeral=True, embed=Embeds.getLogoutEmbed())
        Prints.userLogout(interaction.user.name)
        