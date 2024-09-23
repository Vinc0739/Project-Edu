import base64
from ..db.database import Database
from ..api.api_handler import getUserData
from ..classes.encryption import EncryptionManager
from .embeds import Embeds
from .views import UserPanelView

class Functions:
    # User Panel senden
    async def sendUserPanelEmbed(channel): 
        try:
            message = await channel.fetch_message(channel.last_message_id)
        except:
            embed = Embeds.getUserPanelEmbed()
            view = UserPanelView()
            await channel.send(embed=embed, view=view)
            return
        await message.delete()
        embed = Embeds.getUserPanelEmbed()
        view = UserPanelView()
        await channel.send(embed=embed, view=view)
        
    # EduPage Object bekommen
    def getUserEdu(user_id):
        db = Database()
        user = db.getUser(user_id)
        # Decodieren
        encryption_manager = EncryptionManager()
        decrypted_username = encryption_manager.decrypt(user_id, user[2], user[5])
        decrypted_password = encryption_manager.decrypt(user_id, user[3], user[5])
        
        user_edu = getUserData(decrypted_username, decrypted_password)
        if user_edu == None:
            return None
        else:
            return user_edu
    
    # User Api Kanal bekommen
    def getUserChannel(user_id):
        db = Database()
        user = db.getUser(user_id)
        channel = user[4]
        return channel