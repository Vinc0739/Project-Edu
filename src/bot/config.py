import discord

class Config:
    
    
    """System"""
    
    # Intents
    bot_intents = discord.Intents.all()
    
    
    """Farben"""
    
    # Embeds
    default_embed_colour = '7b5bff'
    success_embed_colour = '18a76c'
    error_embed_colour = 'a71818'
    error_light_embed_colour = 'cf8282'
    
    # Logs
    default_log_colour = '7b5bff'
    bot_start_log_colour = '9cff7d'
    login_log_colour = '239300'
    logout_log_colour = '932800'
    command_log_colour = 'd9c4ff'
    dev_command_log_colour = '5712d5'
    success_log_colour = '18a76c'
    error_log_colour = 'a71818'
    error_light_log_colour = 'cf8282'
    control_panel_log_colour = 'ffff7d'
    commands_synced_log_colour = 'e6c793'
    
    
    """Kanäle"""
    
    # Control Panel
    control_panel_channel = 1283384588349210716
    
    # Join
    welcome_channel = 1281634156778094602
    
    # Logs
    system_logs_channel = 1285293697356791808
    control_panel_logs_channel = 1285293364115275797
    commands_logs_channel = 1285293599210213376
    joins_logs_channel = 1285294767852355690
    
    
    """Rollen"""
    
    join_roles = ['↣ | Mitglied', '-- Team Roles --', '-- Custom Roles --', '-- User Roles--', '-- Permission Roles --']