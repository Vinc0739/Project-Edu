def start_control_panel():
    import multiprocessing
    import customtkinter as ck
    from .panel_config import PanelConfig
    from ..classes.logs import Logs
    from ..bot.bot_startup import start_bot

    bot_process = None

    class App(ck.CTk):
        def __init__(self):
            super().__init__()
            
            self.title("Project Edu - Bot Control Panel")
            self.geometry("1280x720")
            self.grid_columnconfigure(1, weight=1)
            self.grid_rowconfigure(1, weight=1)


            """Side Bar"""
            
            # Frame
            self.sidebar_frame = ck.CTkFrame(self, width=250, corner_radius=PanelConfig.radius_sidebar)
            self.sidebar_frame.grid(row=0, column=0, rowspan=10, sticky="nsew")
            self.sidebar_frame.grid_rowconfigure(6, weight=1)
            
            # Label h1 (Project Edu)
            self.titel_label = ck.CTkLabel(self.sidebar_frame, text='Project Edu Bot', font=(PanelConfig.font_family, PanelConfig.font_h1_size, 'bold'))
            self.titel_label.grid(row=0, column=0, padx=15, pady=10)
            
            # Buttons
            self.sidebar_button_1 = ck.CTkButton(self.sidebar_frame, text='Start Bot', command=self.startBot)
            self.sidebar_button_1.grid(row=1, column=0, pady=10)
            
            self.sidebar_button_2 = ck.CTkButton(self.sidebar_frame, text='Stop Bot', command=self.stopBot)
            self.sidebar_button_2.grid(row=2, column=0, pady=10)
            
            self.sidebar_button_3 = ck.CTkButton(self.sidebar_frame, text='Restart Bot', command=self.restartBot)
            self.sidebar_button_3.grid(row=3, column=0, pady=10)
            
            # Label h2 (Erscheinungsmodus)
            self.appearance_label = ck.CTkLabel(self.sidebar_frame, text='Erscheinungsmodus', font=(PanelConfig.font_family, PanelConfig.font_h2_size, 'bold'))
            self.appearance_label.grid(row=4, column=0, pady=10)
            
            # Drop Down Menu
            self.appearance_options = ck.CTkOptionMenu(self.sidebar_frame, values=['Hell', 'Dunkel', 'System'], command=self.changeAppearanceMode)
            self.appearance_options.grid(row=5, column=0, pady=10)
            self.appearance_options.set('System')
            
            # Footer
            self.footer_label = ck.CTkLabel(self.sidebar_frame, text='made by Vinc', font=(PanelConfig.font_family, PanelConfig.font_footer_size, 'bold'))
            self.footer_label.grid(row=6, column=0, pady=10, sticky='s')
            
            # Logs
            Logs.controlPanelCreated()
            
            
        """Functions"""
        
        #
        def changeAppearanceMode(self, choice):
            if choice == 'System':
                newMode = 'system'
            elif choice == 'Hell':
                newMode = 'light'
            elif choice == 'Dunkel':
                newMode = 'dark'
            ck.set_appearance_mode(newMode)
        
        # Bot starten
        def startBot(self):
            nonlocal bot_process
            if bot_process == None:
                bot_process = multiprocessing.Process(target=start_bot)
                bot_process.daemon = True
                bot_process.start()
                #Logs
                Logs.controlPanelBotStart()
            else:
                Logs.controlPanelBotAlreadyOnline()
        
        # Bot stoppen
        def stopBot(self):
            nonlocal bot_process
            if bot_process != None and bot_process.is_alive():
                bot_process.terminate()
                bot_process.join()
                bot_process = None
                #Logs
                Logs.controlPanelBotStop()
            else:
                Logs.controlPanelBotNotOnline()
        
        # Bot neustarten
        def restartBot(self):
            nonlocal bot_process
            if bot_process != None and bot_process.is_alive():
                # stoppen
                bot_process.terminate()
                bot_process.join()
                # starten
                bot_process = multiprocessing.Process(target=start_bot)
                bot_process.daemon = True
                bot_process.start()
                #Logs
                Logs.controlPanelBotRestarted()
            else:
                Logs.controlPanelBotNotOnline()

    app = App()
    app.mainloop()