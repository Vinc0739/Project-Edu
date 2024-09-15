from datetime import datetime

class Prints:
    
    """Starting Prints"""
    
    # Bot startet
    def botStarting():
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[1;32;40m' + ' bot starting' + '\x1b[0m')
    
    # Cog laden
    def loadingCog(cog_name):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[0;32;40m' + f' cog loaded: "{cog_name}"' + '\x1b[0m')
        
    # Bot eingelogt in Discord
    def botLoggedIn(bot_name):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[1;32;40m' + f' bot logged in as: "{bot_name}"' + '\x1b[0m')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[1;37;40m' + ' -------------------------------------------' + '\x1b[0m')

    """Commands Prints"""
        
    # User benutzt Command
    def usedCommand(user_name, user_id, command_name):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[0;37;40m' + f' "{user_name}" ({user_id}) used command: {command_name}' + '\x1b[0m')     
        
    # User benutzt Dev Command
    def usedDevCommand(user_name, user_id, command_name):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[0;35;40m' + f' "{user_name}" ({user_id}) used dev command: {command_name}' + '\x1b[0m')    
        
    """Control Panel Prints"""
        
    # User logt sich ein
    def userLogin(user_name, user_id):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[0;32;40m' + f' "{user_name}" ({user_id}) logged in' + '\x1b[0m')     
        
    # User logt sich aus
    def userLogout(user_name, user_id):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[0;31;40m' + f' "{user_name}" ({user_id}) logged out' + '\x1b[0m')       
        
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
        
    """Database Prints"""
        
    # neuer User in DB erstellt 
    def createdUser(user_name, user_id):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[0;34;40m' + f' created new user for "{user_name}" ({user_id})' + '\x1b[0m')       
        
    """Welcome Prints"""
    
    # User tritt Server bei
    def joinedServer(user_name, user_id):
        now = datetime.now()
        formatted_time = now.strftime('[%d/%m/%Y-%H:%M:%S]')
        print('\x1b[0;30;40m' + formatted_time + '\x1b[0m' + '\x1b[0;33;40m' + f' "{user_name}" ({user_id}) joined the Server' + '\x1b[0m')  