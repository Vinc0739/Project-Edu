def startControlPanel():
    import asyncio
    import multiprocessing
    from ..bot.bot_startup import start_bot
    import customtkinter as ck
    from .config import Config
    from ..classes.logs import Logs
    
    # Logs nur Terminal
    Logs.newControlPanel()
    
    """Funktionen"""
    # Beim Start
    def startBot():
        # Bot in separatem Prozess starten
        bot_process = multiprocessing.Process(target=start_bot)
        bot_process.start()
        # Logs nur Terminal
        Logs.controlPanelBotStart()
    
    # Beim Stoppen
    def stopBot():
        # Logs.controlPanelBotStopped()
        ...
    
    """App"""
    # Fenster
    app = ck.CTk()
    app.geometry('1280x720')
    app.title('Project Edu - Control Panel')

    """System Frame"""
    # Frame
    system_frame = ck.CTkFrame(app, corner_radius=Config.app_radius, border_width=1)
    system_frame.pack(pady=10, padx=10, fill='both')
    system_frame.place(relx=0.01, rely=0.01, anchor= "nw")

    system_label = ck.CTkLabel(system_frame, text='Bot - Start/Stop', font=(Config.font_family, Config.font_label_size, 'bold'))
    system_label.pack(pady=5, padx=10, side='top')

    system_button_start = ck.CTkButton(system_frame, text='Bot Starten', command=startBot)
    system_button_start.pack(pady=(5, 10), padx=(10, 5), side='left')

    system_button_stop = ck.CTkButton(system_frame, text='Bot Stoppen - in work', command=stopBot)
    system_button_stop.pack(pady=(5, 10), padx=(5, 10), side='left')

    """App"""
    # App Loop
    app.mainloop()