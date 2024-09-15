from  sqlite4  import  SQLite4 as sql
from .prints import Prints

class Database:
    
    __db = None
    
    def __init__(self):
        self.__db = sql('database.db')
        self.__db.connect()
        self.__db.create_table('users', [
            'discordName','discordId', 'username', 'password'
        ])
        
    # neuen User in db erstellen
    def createNewUser(self, discordName, discordId, username, password):
        Prints.createdUser(discordName, discordId)
        
        self.__db.insert('users', {'discordName': discordName, 'discordId': discordId, 'username': username, 'password': password})
        
    # User mit discordId bekommen
    def getUserFromDiscordId(self, discordId):
        users = self.__db.select('users')    
        user = [u for u in users if u[1] == discordId]    
        return user