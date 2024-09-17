from  sqlite4  import  SQLite4 as sql
from ..classes.logs import Logs

class Database:
    
    __db = None
    
    def __init__(self):
        self.__db = sql('database.db')
        self.__db.connect()
        self.__db.create_table('users', [
            'discordName','discordId', 'username', 'password', 'userChannel'
        ])
        
    # neuen User in db erstellen
    def createNewUser(self, discordName, discordId, username, password, userChannel):
        self.__db.insert('users', {'discordName': discordName, 'discordId': discordId, 'username': username, 'password': password, 'userChannel': userChannel})
        # Logs nur Terminal
        Logs.createdUser(discordName, discordId)
    
    # User aus Db löschen
    def deleteUser(self, discordId, discordName):
        self.__db.delete("users", f"discordId = {discordId}")
        # Logs nur Terminal
        Logs.deletedUser(discordId, discordName)
        
    # User mit discordId bekommen
    def getUser(self, discordId):
        users = self.__db.select('users')    
        user = [u for u in users if u[1] == discordId]  
        if user == []:
            return None 
        else:
            return user[0]