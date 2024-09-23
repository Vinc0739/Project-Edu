import io
import locale
from PIL import Image
import discord
from discord import app_commands
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from matplotlib.table import Table
from discord.ext import commands
from ...classes.functions import Functions
from ...classes.logs import Logs, DiscordLogs
from ...classes.embeds import Embeds
from ...classes.modals import UpdateDataModal
from ..bot_config import Config

# Setze die Locale auf Deutsch (de_DE)
locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

def get_available_days():
    days = []
    today = datetime.today()

    # Füge "heute", "morgen" und "übermorgen" hinzu
    days.append("heute")
    days.append("morgen")
    days.append("übermorgen")

    # Füge Wochentage der nächsten zwei Wochen hinzu
    for i in range(2, 15):  # Von morgen (1) bis 14 Tage in die Zukunft (15)
        future_date = today + timedelta(days=i)
        # Nur Wochentage hinzufügen (Montag bis Freitag)
        if future_date.weekday() < 5:  # 0 = Montag, 1 = Dienstag, ..., 6 = Sonntag
            days.append(future_date.strftime('%Y-%m-%d'))
    return days

class ApiConnection(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    """Update Nutzerdatan"""

    # /nutzerdaten
    @commands.hybrid_command(description='Hier kannst du deine Nutzerdaten von EduPage ändern')
    async def nutzerdaten(self, ctx):
        # Überprüfen ob der jetztige Kanal auch der Kanal des Users ist
        current_channel = ctx.interaction.channel_id
        user_channel = Functions.getUserChannel(ctx.author.id)
        if user_channel == current_channel:
            # Modal schicken
            modal = UpdateDataModal()
            await ctx.interaction.response.send_modal(modal)
            # Logs
            await DiscordLogs.usedApiCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/nutzerdaten' ) # Discord
            Logs.usedApiCommand(ctx.author.name, ctx.author.id, '/nutzerdaten') # Terminal
        else:
            await ctx.interaction.response.send_message(ephemeral=True, content='Bitte benutze deinen eigenen Kanal dafür')


    """API Commands"""
    
    # /schüleranzahl
    @commands.hybrid_command(description='Gibt die Anzahl an Schülern aus, die zurzeit in Edupage eingetragen sind')
    async def schüleranzahl(self, ctx):
        # Überprüfen ob der jetztige Kanal auch der Kanal des Users ist
        current_channel = ctx.interaction.channel_id
        user_channel = Functions.getUserChannel(ctx.author.id)
        if user_channel == current_channel:
            # User Daten bekommen
            user_edu = Functions.getUserEdu(ctx.author.id)
            if user_edu == None:
                await ctx.interaction.response.send_message(ephemeral=True, embed=Embeds.getWrongLoginData())
            else:
                # Schüleranzhal bekommen
                student_count = len(user_edu.get_all_students())
                # Antwort
                await ctx.send(f'Es sind zurzeit **{student_count}** Schüler in EduPage eingetragen')
                # Logs
                await DiscordLogs.usedApiCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/schüleranzahl' ) # Discord
                Logs.usedApiCommand(ctx.author.name, ctx.author.id, '/schüleranzahl') # Terminal
        else:
            await ctx.interaction.response.send_message(ephemeral=True, content='Bitte benutze deinen eigenen Kanal dafür')
    
    # /stundenplan
    @commands.hybrid_command(description='Hier kannst du deinen Stundenplan bis zu 2 Wochen im Vorraus einsehen')
    async def stundenplan(self, ctx, datum: str):
        # Überprüfen ob der jetztige Kanal auch der Kanal des Users ist
        current_channel = ctx.interaction.channel_id
        user_channel = Functions.getUserChannel(ctx.author.id)
        if user_channel == current_channel:
            # User Daten bekommen
            user_edu = Functions.getUserEdu(ctx.author.id)
            if user_edu == None:
                await ctx.interaction.response.send_message(ephemeral=True, embed=Embeds.getWrongLoginData())
            else:
                if datum == "heute":
                    datum = datetime.today() + timedelta(days=0)
                elif datum == "morgen":
                    datum = datetime.today() + timedelta(days=1)
                elif datum == "übermorgen":
                    datum = datetime.today() + timedelta(days=2)
                else:
                    datum = datetime.strptime(datum, '%Y-%m-%d')
                # Für Embed Anzeigen
                weekday_name = datum.strftime('%A')
                formatted_date = datum.strftime('%d.%m.%Y')
                # Stundenplan bekommen und Bild erstellen
                myTimeTable = user_edu.get_my_timetable(datum)
                image_buf = timetable_to_image(myTimeTable)
                # Bild zu einem File-Objekt konvertieren
                file = discord.File(image_buf, filename="timetable.png")
                # Antwort
                await ctx.interaction.response.send_message(embed=Embeds.getTimetable(weekday_name, formatted_date), file=file)
                # Logs
                await DiscordLogs.usedApiCommand(self.client.get_channel(Config.commands_logs_channel), ctx.author.id, '/timetable' ) # Discord
                Logs.usedApiCommand(ctx.author.name, ctx.author.id, '/timetable') # Terminal
        else:
            await ctx.interaction.response.send_message(ephemeral=True, content='Bitte benutze deinen eigenen Kanal dafür')
    @stundenplan.autocomplete("datum")  # Auto-Completion für das Datum hinzufügen
    async def date_autocomplete(self, interaction: discord.Interaction, current: str):
        available_days = get_available_days()
        return [app_commands.Choice(name=datum, value=datum) for datum in available_days if current in datum]


async def setup(client):
    await client.add_cog(ApiConnection(client))


# Funktion, um die Timetable-Daten in ein Bild (PNG) zu konvertieren
def timetable_to_image(timetable):
    fig, ax = plt.subplots(figsize=(10, 5))  # Breitere Figur
    ax.set_axis_off()  # Achsen ausschalten
    
    # Hintergrundfarbe hinter der Tabelle
    fig.patch.set_facecolor((1, 1, 1, 0))  # Transparent

    # Liste aller möglichen Perioden, z.B. 1 bis 10
    all_periods = range(1, 11)
    
    # Die Daten in eine Liste konvertieren
    table_data = [["Stunde", "Uhrzeit", "Fach", "Lehrer", "Raum"]]

    for period in all_periods:
        # Suche nach der Lektion in diesem Zeitabschnitt
        lesson = next((lesson for lesson in timetable.lessons if lesson.period == period), None)
        
        if lesson:
            # Wenn die Lektion existiert, erfasse die relevanten Daten
            time_range = f"{lesson.start_time.strftime('%H:%M')} - {lesson.end_time.strftime('%H:%M')}"
            subject = lesson.subject.name
            teacher = lesson.teachers[0].name
            classroom = lesson.classrooms[0].name
        else:
            # Wenn keine Lektion vorhanden ist, setze leere Werte
            time_range = "-"
            subject = "-"
            teacher = "-"
            classroom = "-"
        
        # Zeilen-Daten hinzufügen
        table_data.append([period, time_range, subject, teacher, classroom])

    # Tabelle erstellen
    table = Table(ax, bbox=[0, 0, 1, 1])

    # Spalten- und Zeilenbreite dynamisch anpassen
    n_rows, n_cols = len(table_data), len(table_data[0])
    height = 1.0 / n_rows

    # Berechne die maximale Breite jeder Spalte
    max_widths = [max(len(str(item)) for item in column) for column in zip(*table_data)]

    # Setze die Breite jeder Zelle basierend auf der maximalen Breite
    widths = [w / sum(max_widths) for w in max_widths]  # Normiere die Breiten

    # Header-Zeile formatieren
    for j in range(n_cols):
        table.add_cell(0, j, widths[j], height, text=table_data[0][j], loc='center', facecolor="#7b5bff")
        table[(0, j)].set_text_props(color='white', fontsize=25, fontfamily='Inter')  # Header-Schriftart
        table[(0, j)].set_edgecolor('none')  # Kantenfarbe des Headers auf 'none'

    # Daten hinzufügen
    for i in range(1, n_rows):
        for j in range(n_cols):
            cell_text = table_data[i][j]
            # Hintergrundfarben für reguläre Zellen
            facecolor = '#d4c7ff' if i % 2 == 0 else '#f5f2ff'
            text_color = 'black'  # Schriftfarbe für die regulären Zellen

            # Zelle hinzufügen mit berechneter Breite
            table.add_cell(i, j, widths[j], height, text=cell_text, loc='center', facecolor=facecolor)
            table[(i, j)].set_edgecolor('none')  # Kantenfarbe auf 'none'
            table[(i, j)].set_text_props(color=text_color, fontsize=14, fontfamily='Inter')

    ax.add_table(table)

    # Das Bild in einen Puffer (BytesIO) speichern
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')  # bbox_inches sorgt dafür, dass die Inhalte gut sichtbar sind
    plt.close(fig)
    buf.seek(0)

    return buf