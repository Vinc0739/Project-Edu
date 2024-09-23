import base64
from sqlite4 import SQLite4 as sql
from ..classes.encryption import EncryptionManager
from ..classes.logs import Logs

class Database:
    def __init__(self):
        self.__db = sql('database.db')
        self.__db.connect()
        self.__db.create_table('users', [
            'discordName', 'discordId', 'username', 'password', 'userChannel', 'salt'
        ])
        self.encryption_manager = EncryptionManager()

    def createNewUser(self, discordName, discordId, username, password, userChannel):
        salt = self.encryption_manager.generate_salt()
        e_username = self.encryption_manager.encrypt(discordId, username, salt)
        e_password = self.encryption_manager.encrypt(discordId, password, salt)

        # Salt encoden
        b64_salt = base64.b64encode(salt).decode('utf-8')
        # Eintragen
        try:
            self.__db.insert('users', {
                'discordName': discordName, 
                'discordId': discordId, 
                'username': e_username, 
                'password': e_password, 
                'userChannel': userChannel, 
                'salt': b64_salt
            })
        except Exception as e:
            print(f"Fehler beim Einfügen in die Datenbank: {e}")
        
        Logs.createdUser(discordName, discordId)

    def deleteUser(self, discordId, discordName):
        try:
            self.__db.delete('users', f'discordId = {discordId}')
            Logs.deletedUser(discordId, discordName)
        except Exception as e:
            print(f"Fehler beim Löschen des Benutzers: {e}")

    def updateUser(self, discordName, discordId, username, password):
        salt = self.encryption_manager.generate_salt()
        e_username = self.encryption_manager.encrypt(discordId, username, salt)
        e_password = self.encryption_manager.encrypt(discordId, password, salt)
        
        b64_salt = base64.b64encode(salt).decode('utf-8')
        
        self.__db.update('users', {
            'username': e_username, 
            'password': e_password, 
            'salt': b64_salt
        }, f'discordId = {discordId}')
        
        Logs.updatedUser(discordId, discordName)

    def getUser(self, discordId):
        users = self.__db.select('users')
        user = [u for u in users if u[1] == discordId]
        if not user:
            return None
        return user[0]

    def decryptUserData(self, discordId, encrypted_username, encrypted_password, salt):
        salt_bytes = base64.b64decode(salt)
        decrypted_username = self.encryption_manager.decrypt(discordId, encrypted_username, salt_bytes)
        decrypted_password = self.encryption_manager.decrypt(discordId, encrypted_password, salt_bytes)
        return decrypted_username, decrypted_password
