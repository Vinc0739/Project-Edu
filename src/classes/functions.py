import base64
from ..db.database import Database
from ..api.api_handler import getUserData
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
        byte_username = base64.b64decode(user[2])
        byte_password = base64.b64decode(user[3])
        decoded_username = byte_username.decode('utf-8')
        decoded_password = byte_password.decode('utf-8')
        
        user_edu = getUserData(decoded_username, decoded_password)
        return user_edu
    
    # User Api Kanal bekommen
    def getUserChannel(user_id):
        db = Database()
        user = db.getUser(user_id)
        channel = user[4]
        return channel