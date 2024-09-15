import discord
from discord.ext import commands

# Embed Farben
default_embed_colour = "0x7b5bff"
success_embed_colour = "0x18a76c"
error_embed_colour = "0xa71818"

class Embeds:
    # Control Panel Embed
    def getControlPanelEmbed():
        control_panel_embed = discord.Embed()
        control_panel_embed.title='Project Edu - Control Panel'
        control_panel_embed.color=discord.Colour.from_str(default_embed_colour)
        control_panel_embed.set_footer(text='Project Edu made by Vinc#0739')
        control_panel_embed.add_field(name='📑 Login', value='Drücke auf den Login Button und fülle das Formular mit deinen EduPage Kontodaten aus. Solltest du falsche Daten eingeben, kann du sie jederzeit in deinem eigenen Kanal ändern.')
        control_panel_embed.add_field(name='📕 Auslogen', value='Um dich aus zu loggen musst du auf den roten Auslogen Button drücken. Jegliche Daten von dir werden gelöscht. Bedenke, dass auch dein Kanal, sowie Nachrichten und Dateien gelöscht werden.')
        return control_panel_embed
    
    # Login Embed
    def getLoginEmbed(channel_id):
        login_embed = discord.Embed()
        login_embed.title='Project Edu - Login'
        login_embed.description=f'Du hast dich erfolgreich eingelogt. Du findest deinen persönlichen Kanal unter <#{channel_id}>.'
        login_embed.color=discord.Colour.from_str(success_embed_colour)
        login_embed.set_footer(text='Project Edu made by Vinc#0739')
        return login_embed
    # Login Error Embed
    def getLoginErrorEmbed(channel_id):
        login_error_embed = discord.Embed()
        login_error_embed.title='Project Edu - Login'
        login_error_embed.description='Login fehlgeschlagen. Versuche es bitte später erneut.'
        login_error_embed.color=discord.Colour.from_str(error_embed_colour)
        login_error_embed.set_footer(text='Project Edu made by Vinc#0739')
        return login_error_embed
    
    # Channel Crated
    def getChannelCreatedEmbed(username, password):
        channel_created_embed = discord.Embed()
        channel_created_embed.title='Project Edu - Kanal erstellt'
        channel_created_embed.description='Dein Kanal wurde erfolgreich erstellt. Du kann hier nun alle Funktionen des Bots benutzen.'
        channel_created_embed.color=discord.Colour.from_str(default_embed_colour)
        channel_created_embed.set_footer(text='Project Edu made by Vinc#0739')
        channel_created_embed.add_field(name='Benutzername', value=f'||{username}||')
        channel_created_embed.add_field(name='Passwort', value=f'||{password}||')
        return channel_created_embed
    
    # Logout Embed
    def getLogoutEmbed():
        logout_embed = discord.Embed()
        logout_embed.title='Project Edu - Logout'
        logout_embed.description='Du hast dich erfolgreich ausgelogt.'
        logout_embed.color=discord.Colour.from_str(default_embed_colour)
        logout_embed.set_footer(text='Project Edu made by Vinc#0739')
        return logout_embed