from .embeds import Embeds
from .views import ControlPanelView
from ..bot.config import Config
from .logs import Logs, DiscordLogs

class Functions:
    async def sendControlPanelEmbed(channel): 
        try:
            message = await channel.fetch_message(channel.last_message_id)
        except:
            embed = Embeds.getControlPanelEmbed()
            view = ControlPanelView()
            await channel.send(embed=embed, view=view)
            return
        await message.delete()
        embed = Embeds.getControlPanelEmbed()
        view = ControlPanelView()
        await channel.send(embed=embed, view=view)