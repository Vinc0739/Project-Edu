import discord
from discord.ext import commands
from .embeds import Embeds
from .prints import Prints
from .modals import LoginModal

class ControlPanelView(discord.ui.View):
    
    # Login Button
    @discord.ui.button(label='Login', style=discord.ButtonStyle.green)
    async def login(self, interaction: discord.Interaction, button: discord.ui.Button):
        #Modal (Formular) laden
        modal = LoginModal()
        await interaction.response.send_modal(modal)
        
    # Logout Button
    @discord.ui.button(label='Logout', style=discord.ButtonStyle.red)
    async def logout(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(ephemeral=True, embed=Embeds.getLogoutEmbed())
        Prints.userLogout(interaction.user.name, interaction.user.id)
        