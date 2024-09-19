from datetime import datetime
from .embeds import LogEmbeds
from ..bot.config import Config

class Logs:
    
    """Starting Prints"""
    
    # Bot startet
    async def botStarting():
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[1;32;40m' + 'bot starting' + '\x1b[0m')
        
    # Bot gestopt
    async def botStopped():
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[1;31;40m' + 'bot stopped' + '\x1b[0m')
    
    # Cog laden
    def loadingCog(cog_name):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[0;32;40m' + f'cog loaded: "{cog_name}"' + '\x1b[0m')
        
    # Bot eingelogt in Discord
    def botLoggedIn(bot_name):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[1;32;40m' + 'bot logged in as: "{bot_name}"' + '\x1b[0m')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[1;37;40m' + '-------------------------------------------' + '\x1b[0m')
        
    # Bot eingelogt in Discord
    def syncedCommands():
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[5;32;40m' + 'synced command tree' + '\x1b[0m')

    """Commands Prints"""
        
    # User benutzt Command
    def usedCommand(user_name, user_id, command_name):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[0;37;40m' + f'"{user_name}" ({user_id}) used command: {command_name}' + '\x1b[0m')     
        
    # User benutzt Dev Command
    def usedDevCommand(user_name, user_id, command_name):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[0;35;40m' + f'"{user_name}" ({user_id}) used dev command: {command_name}' + '\x1b[0m')    
        
    """User Panel Prints"""
        
    # Neues User Panel erstellt
    def newUserPanel():
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[7;33;40m' + 'new User panel created' + '\x1b[0m')  
        
    # User logt sich ein
    def userLogin(user_name, user_id):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[0;32;40m' + f'"{user_name}" ({user_id}) logged in' + '\x1b[0m')     
        
    # User logt sich aus
    def userLogout(user_name, user_id):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[0;31;40m' + f'"{user_name}" ({user_id}) logged out' + '\x1b[0m')       
        
    # Login Error
    def loginError(user_name, user_id, error):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[0;33;41m' + f'login error for "{user_name}" ({user_id}):{error}' + '\x1b[0m')      
        
    # Logout Error    
    def logoutError(user_name, user_id, error):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[0;33;41m' + f'logout error for "{user_name}" ({user_id}):{error}' + '\x1b[0m')     
        
    # User schon Eingelogt  
    def alreadyLogedIn(user_name, user_id):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[0;37;41m' + f'already logged in: "{user_name}" ({user_id})' + '\x1b[0m')  
        
    # User nicht Eingelogt  
    def userNotLogedIn(user_name, user_id):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + f'{formatted_time} ' + '\x1b[0m' + '\x1b[0;37;41m' + f'user not logged in: "{user_name}" ({user_id})' + '\x1b[0m')      
        
    """Database Prints"""
        
    # neuer User in DB erstellt 
    def createdUser(user_name, user_id):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[0;34;40m' + f' created new user for "{user_name}" ({user_id})' + '\x1b[0m')  
        
    # User von DB gelöscht 
    def deletedUser(user_id, user_name):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[0;34;40m' + f' deleted user for "{user_name}" ({user_id})' + '\x1b[0m')       
        
    """Welcome Prints"""
    
    # User tritt Server bei
    def joinedServer(user_name, user_id):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[0;33;40m' + f' "{user_name}" ({user_id}) joined the Server' + '\x1b[0m') 

# -------------------------- Discord Logs -----------------------------------------------------------------------------------------------------------------------      
# 
class DiscordLogs:
    
    """Starting Logs"""
    
    # Bot Startet
    async def botStarting(channel):
        await channel.send(embed=LogEmbeds.getLogsEmbed('Der Bot wurde gestartet.', Config.bot_start_log_colour))
        
    """Commands Logs"""    
        
    # User benutzt Command
    async def usedCommand(channel, user_id, command_name):
        await channel.send(embed=LogEmbeds.getLogsEmbed(f'Der User **<@{user_id}>** hat den Command "**{command_name}**" verwendet.', Config.command_log_colour))
        
    # User benutzt Dev Command
    async def usedDevCommand(channel, user_id, command_name):
        await channel.send(embed=LogEmbeds.getLogsEmbed(f'Der User **<@{user_id}>** hat den Dev Command "**{command_name}**" verwendet.', Config.dev_command_log_colour))
        
    """User Panel"""    
        
    # User Login
    async def userLogin(channel, user_id):
        await channel.send(embed=LogEmbeds.getLogsEmbed(f'Der User **<@{user_id}>** hat sich eingelogt', Config.login_log_colour))
        
    # User Logout
    async def userLogout(channel, user_id):
        await channel.send(embed=LogEmbeds.getLogsEmbed(f'Der User **<@{user_id}>** hat sich ausgelogt', Config.logout_log_colour))
        
    # Login Error
    async def loginError(channel, user_id, error):
        await channel.send(embed=LogEmbeds.getLogsEmbed(f'Fehler beim Login von **<@{user_id}>**. Error: {error}', Config.error_log_colour))
        
    # Logout Error
    async def logoutError(channel, user_id, error):
        await channel.send(embed=LogEmbeds.getLogsEmbed(f'Fehler beim Logout von **<@{user_id}>**. Error: {error}', Config.error_log_colour))
        
    # User schon Eingelogt  
    async def alreadyLogedIn(channel, user_id):
        await channel.send(embed=LogEmbeds.getLogsEmbed(f'Der User **<@{user_id}>** hat versucht sich einzuloggen, er ist jedoch schon eingelogt', Config.error_light_log_colour))
        
    # User nicht Eingelogt  
    async def userNotLogedIn(channel, user_id,):
        await channel.send(embed=LogEmbeds.getLogsEmbed(f'Der User **<@{user_id}>** hat versucht sich auszuloggen, er ist jedoch nicht eingelogt', Config.error_light_log_colour))
        
    # Neues User Panel erstellt   
    async def newUserPanel(channel):
        await channel.send(embed=LogEmbeds.getLogsEmbed(f'Neues User Panel erstellt', Config.user_panel_log_colour))

    # Neuer User joint Server
    async def joinedServer(channel, user_id):
        await channel.send(embed=LogEmbeds.getLogsEmbed(f'Der User <@{user_id}> ist dem Server beigetreten', Config.default_log_colour))
        
    # Command Tree gesynced
    async def syncedCommands(channel):
        await channel.send(embed=LogEmbeds.getLogsEmbed('Der Command Tree wurde gesynced', Config.commands_synced_log_colour))
        
    # Command Tree gesynced
    async def botStopped(channel, user_id):
        await channel.send(embed=LogEmbeds.getLogsEmbed(f'Der User <@{user_id}> hat den Bot gestopt', Config.error_log_colour))