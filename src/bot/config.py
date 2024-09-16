import discord

class Config:
    
    # Embed Farben
    default_embed_colour = '7b5bff'
    success_embed_colour = '18a76c'
    error_embed_colour = 'a71818'
    error_light_embed_colour = 'cf8282'
    
    # Logs Farben
    default_log_colour = '7b5bff'
    bot_start_log_colour = '9cff7d'
    login_log_colour = '239300'
    logout_log_colour = '932800'
    command_log_colour = 'd9c4ff'
    dev_command_log_colour = '5712d5'
    success_log_colour = '18a76c'
    error_log_colour = 'a71818'
    error_light_log_colour = 'cf8282'
    database_log_colour = '82a1cf'
    
    # Bot Intends
    bot_intents = discord.Intents.all()
    
    # Kanäle
    welcome_channel = 1281634156778094602
    logs_channel = 1285183147582951435
    
    # Rollen
    join_roles = ['↣ | Mitglied', '-- Team Roles --', '-- Custom Roles --', '-- User Roles--', '-- Permission Roles --']