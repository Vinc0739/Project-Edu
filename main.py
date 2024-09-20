import multiprocessing
from src.controlpanel.panel_startup import start_control_panel
if __name__ == '__main__':
    # Control Panel in separatem Prozess starten
    control_panel_process = multiprocessing.Process(target=start_control_panel)
    control_panel_process.start()
    
    # Asci Banner erstellen
    ascii_banner = [
    '██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗   ███████╗██████╗ ██╗   ██╗    ██████╗ ██╗   ██╗    ██╗   ██╗██╗███╗   ██╗ ██████╗',
    '██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝   ██╔════╝██╔══██╗██║   ██║    ██╔══██╗╚██╗ ██╔╝    ██║   ██║██║████╗  ██║██╔════╝',
    '██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║█████╗█████╗  ██║  ██║██║   ██║    ██████╔╝ ╚████╔╝     ██║   ██║██║██╔██╗ ██║██║     ',
    '██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║╚════╝██╔══╝  ██║  ██║██║   ██║    ██╔══██╗  ╚██╔╝      ╚██╗ ██╔╝██║██║╚██╗██║██║     ',
    '██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║      ███████╗██████╔╝╚██████╔╝    ██████╔╝   ██║        ╚████╔╝ ██║██║ ╚████║╚██████╗',
    '╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝      ╚══════╝╚═════╝  ╚═════╝     ╚═════╝    ╚═╝         ╚═══╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝'
    ]
    start_color = (162, 0, 255)  # Pink
    end_color = (55, 0, 133)     # Dunkel Lila
    
    # Farbe zu Asci
    def colored_text(r, g, b, text):
        return f'\033[38;2;{r};{g};{b}m{text}\033[0m'
    # Farbverlauf erstellen
    def get_color(start, end, factor):
        return (
            int(start[0] + (end[0] - start[0]) * factor),
            int(start[1] + (end[1] - start[1]) * factor),
            int(start[2] + (end[2] - start[2]) * factor)
    )

    # Banner printen mit Farbverlauf
    for i, line in enumerate(ascii_banner):
        progress = i / (len(ascii_banner) - 1)
        r, g, b = get_color(start_color, end_color, progress)
        print(colored_text(r, g, b, line))