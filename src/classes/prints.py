class Prints:
    def usedCommand(user, command):
        print('\x1b[6;33;40m' + user + '\x1b[0m' + '\x1b[6;30;40m' + f' executed the command ' + '\x1b[0m' + '\x1b[6;33;40m' + command + '\x1b[0m')
    
    def usedDevCommand(user, command):
        print('\x1b[6;35;40m' + user + '\x1b[0m' + '\x1b[6;30;40m' + f' executed dev command ' + '\x1b[0m' + '\x1b[6;35;40m' + command + '\x1b[0m')
        
    def userLogin(user):
        print('\x1b[7;30;42m' + user + '\x1b[0m' + '\x1b[6;30;40m' + f' logged in ' + '\x1b[0m')
        
    def userLogout(user):
        print('\x1b[7;30;41m' + user + '\x1b[0m' + '\x1b[6;30;40m' + f' logged out ' + '\x1b[0m')