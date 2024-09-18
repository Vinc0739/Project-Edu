import multiprocessing
from src.controlpanel.panel_startup import startControlPanel

if __name__ == "__main__":
    # Control Panel in separatem Prozess starten
    control_panel_process = multiprocessing.Process(target=startControlPanel)
    control_panel_process.start()