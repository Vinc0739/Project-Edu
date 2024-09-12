import discord
from discord.ext import commands
from dotenv import dotenv_values
from .. import functions as api

# Keys von der .env Datei bekommen
env = dotenv_values(".env")

class EduCommands(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    # /syncc -> Kann länge dauern
    @commands.hybrid_command()
    async def syncc(self, ctx):
        await self.client.tree.sync()
        print('\x1b[1;33;41m' + 'Synced Commands' + '\x1b[0m')
        await ctx.send('Commands wurden gesynct')
        usedCommand(ctx.author.name, '/syncc')
    # /botping
    @commands.hybrid_command()
    async def botping(self, ctx):
        user_ping = round(self.client.latency * 1000)
        await ctx.send(f'Der Bot hat gerade einen Ping von: {user_ping}ms')
        usedCommand(ctx.author.name, '/botping')
    
    # /schüleranzahl
    @commands.hybrid_command()
    async def schüleranzahl(self, ctx):
        print('test')
        await ctx.send(f'Es sind: {api.getStudentCount()} Schüler in EduPage eingetragen')
        usedCommand(ctx.author.name, '/schüleranzahl')
    
    # /createlogin
    @commands.hybrid_command()
    async def createlogin(self, ctx):
        # Login Embed erstellen
        loginEmbed = discord.Embed(
            colour=discord.Colour.from_str(env['EMBED_COLOUR']),
            title='Project Edu - Control Panel',
            description=''
        )
        loginEmbed.set_footer(text='Project Edu made by Vinc#0739')
        loginEmbed.add_field(name='📑 Login', value='Drücke auf den Login Button und fülle das Formular mit deinen EduPage Kontodaten aus. Solltest du falsche Daten eingeben, kann du sie jederzeit in deinem eigenen Kanal ändern.')
        loginEmbed.add_field(name='📕 Auslogen', value='Um dich aus zu loggen musst du auf den roten Auslogen Button drücken. Jegliche Daten von dir werden gelöscht. Bedenke, dass auch dein Kanal, sowie Nachrichten und Dateien gelöscht werden.')
        # Embed senden
        await ctx.send(embed=loginEmbed)
        print('\x1b[1;33;41m' + 'New Login Created' + '\x1b[0m')
        usedCommand(ctx.author.name, '/createlogin')

# cog Setup
async def setup(client):
    await client.add_cog(EduCommands(client))
    
# Wird ausgefüht bei jedem Benutzen eines Command
def usedCommand(user, command):
    print('\x1b[6;33;40m' + user + '\x1b[0m' + '\x1b[6;30;40m' + f' executed the command ' + '\x1b[0m' + '\x1b[6;33;40m' + command + '\x1b[0m')