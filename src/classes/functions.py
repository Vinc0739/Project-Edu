from .embeds import Embeds
from .views import UserPanelView

class Functions:
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