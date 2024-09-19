import multiprocessing
from src.controlpanel.panel_startup import start_control_panel

if __name__ == "__main__":
    # Control Panel in separatem Prozess starten
    control_panel_process = multiprocessing.Process(target=start_control_panel)
    control_panel_process.start()