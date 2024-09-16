import discord
from discord.ext import commands

# Embed Farben
default_embed_colour = "0x7b5bff"
success_embed_colour = "0x18a76c"
error_embed_colour = "0xa71818"

class Embeds:
    # Control Panel Embed
    def getControlPanelEmbed():
        embed = discord.Embed()
        embed.title='Project Edu - Control Panel'
        embed.color=discord.Colour.from_str(default_embed_colour)
        embed.set_footer(text='Project Edu made by Vinc#0739')
        embed.add_field(name='📑 Login', value='Drücke auf den Login Button und fülle das Formular mit deinen EduPage Kontodaten aus. Solltest du falsche Daten eingeben, kann du sie jederzeit in deinem eigenen Kanal ändern.')
        embed.add_field(name='📕 Auslogen', value='Um dich aus zu loggen musst du auf den roten Auslogen Button drücken. Jegliche Daten von dir werden gelöscht. Bedenke, dass auch dein Kanal, sowie Nachrichten und Dateien gelöscht werden.')
        return embed
    
    # Login Embed
    def getLoginEmbed(channel_id):
        embed = discord.Embed()
        embed.title='Project Edu - Login'
        embed.description=f'Du hast dich erfolgreich eingelogt. Du findest deinen persönlichen Kanal unter <#{channel_id}>.'
        embed.color=discord.Colour.from_str(success_embed_colour)
        embed.set_footer(text='Project Edu made by Vinc#0739')
        return embed
    
    # Login Error Embed
    def getLoginErrorEmbed(error):
        embed = discord.Embed()
        embed.title='Project Edu - Login Fehler'
        embed.description=f'Login fehlgeschlagen. Versuche es bitte später erneut. ERROR: {error}'
        embed.color=discord.Colour.from_str(error_embed_colour)
        embed.set_footer(text='Project Edu made by Vinc#0739')
        return embed
    
    # schon eingelogt Embed
    def getAlreadyLogedInEmbed():
        embed = discord.Embed()
        embed.title='Project Edu - Login Fehler'
        embed.description=f'Du bereits eingelogt bist.'
        embed.color=discord.Colour.from_str(error_embed_colour)
        embed.set_footer(text='Project Edu made by Vinc#0739')
        return embed
    
    # Channel Crated
    def getChannelCreatedEmbed(username, password):
        embed = discord.Embed()
        embed.title='Project Edu - Kanal erstellt'
        embed.description='Dein Kanal wurde erfolgreich erstellt. Du kann hier nun alle Funktionen des Bots benutzen.'
        embed.color=discord.Colour.from_str(success_embed_colour)
        embed.set_footer(text='Project Edu made by Vinc#0739')
        embed.add_field(name='Benutzername', value=f'||{username}||')
        embed.add_field(name='Passwort', value=f'||{password}||')
        return embed
    
    # Logout Embed
    def getLogoutEmbed():
        embed = discord.Embed()
        embed.title='Project Edu - Logout'
        embed.description='Du hast dich erfolgreich ausgelogt.'
        embed.color=discord.Colour.from_str(success_embed_colour)
        embed.set_footer(text='Project Edu made by Vinc#0739')
        return embed
    
    # Neuer User joint dem Server
    def getJoinedServer(member):
        embed = discord.Embed()
        embed.title='Project Edu - Willkommen'
        embed.description=f'**Hey {member.mention}, willkommen bei Project Edu!**'
        embed.color=discord.Colour.from_str(default_embed_colour)
        embed.set_footer(text='Project Edu made by Vinc#0739')
        embed.add_field(name='📌 Anleitung', value='Schaue dir den Kanal <#1281634184367968389> an. Dort findest du eine detaillierte Anleitung, wie du dich beim Bot einloggen kannst, um alle Funktionen nutzen zu können. Befolge alle Schritte genau so wie beschrieben, um Fehler zu vermeiden.')
        embed.add_field(name='🔨 Fortschritt', value='Besuche den Kanal <#1283381827528032327>, um den aktuellen Fortschritt des Projektes zu verfolgen. Hier erhältst du die neuesten Updates und Informationen über Bugfixes und neue Features.')
        return embed
    
    # schon eingelogt Embed
    def getNotLogedIdEmbed():
        embed = discord.Embed()
        embed.title='Project Edu - Logout Fehler'
        embed.description=f'Du bist nicht eingelogt.'
        embed.color=discord.Colour.from_str(error_embed_colour)
        embed.set_footer(text='Project Edu made by Vinc#0739')
        return embed