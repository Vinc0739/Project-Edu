class Prints:
    def usedCommand(user, command):
        print('\x1b[6;33;40m' + user + '\x1b[0m' + '\x1b[6;30;40m' + ' executed the command ' + '\x1b[0m' + '\x1b[6;33;40m' + command + '\x1b[0m')
    
    def usedDevCommand(user, command):
        print('\x1b[6;35;40m' + user + '\x1b[0m' + '\x1b[6;30;40m' + ' executed dev command ' + '\x1b[0m' + '\x1b[6;35;40m' + command + '\x1b[0m')
        
    def userLogin(user):
        print('\x1b[7;30;42m' + user + '\x1b[0m' + '\x1b[6;30;40m' + ' logged in ' + '\x1b[0m')
        
    def userLogout(user):
        print('\x1b[7;30;41m' + user + '\x1b[0m' + '\x1b[6;30;40m' + ' logged out ' + '\x1b[0m')
    
    def insertedInDB(discordName, discordId):
        print('\x1b[6;30;40m' + 'created new user in db for - ' + '\x1b[0m' + '\x1b[7;30;46m' + f'{discordName}: {discordId}' + '\x1b[0m')