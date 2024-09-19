import discord
from datetime import datetime
from ..bot.bot_config import Config

class Embeds:
    # User Panel Embed
    def getUserPanelEmbed():
        embed = discord.Embed()
        embed.title='Project Edu - User Panel'
        embed.color=discord.Colour.from_str('0x' + f'{Config.default_embed_colour}')
        embed.set_footer(text='Project Edu made by Vinc#0739', icon_url=Config.logo_url)
        embed.add_field(name='📑 Login', value='Drücke auf den Login Button und fülle das Formular mit deinen EduPage Kontodaten aus. Solltest du falsche Daten eingeben, kann du sie jederzeit in deinem eigenen Kanal ändern.')
        embed.add_field(name='📕 Auslogen', value='Um dich aus zu loggen musst du auf den roten Auslogen Button drücken. Jegliche Daten von dir werden gelöscht. Bedenke, dass auch dein Kanal, sowie Nachrichten und Dateien gelöscht werden.')
        return embed
    
    # Login Embed
    def getLoginEmbed(channel_id):
        embed = discord.Embed()
        embed.title='Project Edu - Login'
        embed.description=f'Du hast dich erfolgreich eingelogt. Du findest deinen persönlichen Kanal unter <#{channel_id}>.'
        embed.color=discord.Colour.from_str('0x' + f'{Config.success_embed_colour}')
        embed.set_footer(text='Project Edu made by Vinc#0739', icon_url=Config.logo_url)
        return embed
    
    # Login Error Embed
    def getLoginErrorEmbed():
        embed = discord.Embed()
        embed.title='Project Edu - Login Fehler'
        embed.description=f'Login fehlgeschlagen. Versuche es bitte später erneut.'
        embed.color=discord.Colour.from_str('0x' + f'{Config.error_embed_colour}')
        embed.set_footer(text='Project Edu made by Vinc#0739', icon_url=Config.logo_url)
        return embed
    
    # schon eingelogt Embed
    def getAlreadyLogedInEmbed():
        embed = discord.Embed()
        embed.title='Project Edu - Login Fehler'
        embed.description=f'Du bereits eingelogt bist.'
        embed.color=discord.Colour.from_str('0x' + f'{Config.error_light_embed_colour}')
        embed.set_footer(text='Project Edu made by Vinc#0739', icon_url=Config.logo_url)
        return embed
    
    # Channel Crated
    def getChannelCreatedEmbed(username, password):
        embed = discord.Embed()
        embed.title='Project Edu - Kanal erstellt'
        embed.description='Dein Kanal wurde erfolgreich erstellt. Du kann hier nun alle Funktionen des Bots benutzen.'
        embed.color=discord.Colour.from_str('0x' + f'{Config.success_embed_colour}')
        embed.set_footer(text='Project Edu made by Vinc#0739', icon_url=Config.logo_url)
        embed.add_field(name='Benutzername', value=f'||{username}||')
        embed.add_field(name='Passwort', value=f'||{password}||')
        return embed
    
    # Logout Embed
    def getLogoutEmbed():
        embed = discord.Embed()
        embed.title='Project Edu - Logout'
        embed.description='Du hast dich erfolgreich ausgelogt.'
        embed.color=discord.Colour.from_str('0x' + f'{Config.success_embed_colour}')
        embed.set_footer(text='Project Edu made by Vinc#0739', icon_url=Config.logo_url)
        return embed
    
    # Neuer User joint dem Server
    def getJoinedServer(member):
        embed = discord.Embed()
        embed.title='Project Edu - Willkommen'
        embed.description=f'**Hey {member.mention}, willkommen bei Project Edu!**'
        embed.color=discord.Colour.from_str('0x' + f'{Config.default_embed_colour}')
        embed.set_footer(text='Project Edu made by Vinc#0739', icon_url=Config.logo_url)
        embed.add_field(name='📌 Anleitung', value='Schaue dir den Kanal <#1281634184367968389> an. Dort findest du eine detaillierte Anleitung, wie du dich beim Bot einloggen kannst, um alle Funktionen nutzen zu können. Befolge alle Schritte genau so wie beschrieben, um Fehler zu vermeiden.')
        embed.add_field(name='🔨 Fortschritt', value='Besuche den Kanal <#1283381827528032327>, um den aktuellen Fortschritt des Projektes zu verfolgen. Hier erhältst du die neuesten Updates und Informationen über Bugfixes und neue Features.')
        return embed
    
    # schon eingelogt Embed
    def getNotLogedIdEmbed():
        embed = discord.Embed()
        embed.title='Project Edu - Logout Fehler'
        embed.description=f'Du bist nicht eingelogt.'
        embed.color=discord.Colour.from_str('0x' + f'{Config.error_light_embed_colour}')
        embed.set_footer(text='Project Edu made by Vinc#0739', icon_url=Config.logo_url)
        return embed
    
    # User Panel erstellt
    def getUserPanelCreated():
        embed = discord.Embed()
        embed.title='Project Edu - User Panel'
        embed.description=f'Das User Panel wurde neu gesendet.'
        embed.color=discord.Colour.from_str('0x' + f'{Config.success_embed_colour}')
        embed.set_footer(text='Project Edu made by Vinc#0739', icon_url=Config.logo_url)
        return embed
    
class LogEmbeds:
    def getLogsEmbed(description, color):
        
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        
        embed = discord.Embed()
        embed.title=f'{formatted_time}'
        embed.description=f'{description}'
        embed.color=discord.Colour.from_str('0x' + f'{color}')
        embed.set_footer(text='Project Edu made by Vinc#0739', icon_url=Config.logo_url)
        return embed