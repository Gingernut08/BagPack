from imports import tkinter, json
from item import focus_pygame_window, create_item

def import_item(screen, *args):
    filename = tkinter.filedialog.askopenfilename(
                                                                title="Select File To Import",
                                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
                                                            )
    if filename:
        try:
            with open(filename) as f:
                data = json.load(f)
            create_item(data, [250, 150], screen)
        except:
            pass
    focus_pygame_window()