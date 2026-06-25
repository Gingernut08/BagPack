from imports import tkinter, json, os
from item import create_item, new_item, focus_pygame_window
from guiElements import Button, TextInput
from varSetup import new_item_makers, items, WIDTH, HEIGHT, screen, leftSpacing, topSpacing, bottomSpacing, numLeftButtons, numRightButtons, itemColor, baseDir, buttons

def create_new_item_picker():
    xPos = leftSpacing * 2
    i = 0
    j = 0
    text = TextInput((xPos, topSpacing + i * 100), 400, 60, "ENTER NAME", screen)
    i += 1
    text = TextInput((xPos, topSpacing + i * 100), 400, 60, "ENTER BRAND", screen)
    i += 1
    text = TextInput((xPos, topSpacing + i * 100), 400, 60, "ENTER WEIGHT", screen)
    i += 1
    text = TextInput((xPos, topSpacing + i * 100), 400, 60, "ENTER COLOR", screen)
    i += 1
    text = TextInput((xPos, topSpacing + i * 100), 400, 60, "ENTER CATEGORY", screen)
    i += 1
    button = Button((xPos + j * 250, topSpacing + i * 100), 150, 60, "CANCEL", cancel, None, screen)
    new_item_makers.append(button)
    j += 1
    button = Button((xPos + j * 250, topSpacing + i * 100), 150, 60, "SUBMIT", submit_item, None, screen)
    new_item_makers.append(button)
    
    for new_item_maker in new_item_makers:
        new_item_maker.shown = False

def create_buttons():
    i = 0
    button = Button((WIDTH - 200, topSpacing + i * (HEIGHT - topSpacing - bottomSpacing) // numRightButtons), 200, (HEIGHT - topSpacing - bottomSpacing) // numRightButtons, "DELETE", None, None, screen)
    button.color = (40, 20, 20)
    i += 1
    button = Button((WIDTH - 200, topSpacing + i * (HEIGHT - topSpacing - bottomSpacing) // numRightButtons), 200, (HEIGHT - topSpacing - bottomSpacing) // numRightButtons, "EDIT", None, None, screen)
    button.color = (40, 40, 20)
    i += 1
    button = Button((WIDTH - 200, topSpacing + i * (HEIGHT - topSpacing - bottomSpacing) // numRightButtons), 200, (HEIGHT - topSpacing - bottomSpacing) // numRightButtons, "SAVE", None, None, screen)
    button.color = (20, 40, 20)
    
    i = 0
    button = Button((0, topSpacing + i * (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons), 200, (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons, "IMPORT", import_item, (screen, None), screen)
    i += 1
    button = Button((0, topSpacing + i * (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons), 200, (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons, "NEW", new_item, None, screen)
    
for item in items:
    item.shown = True

def cancel(*args):
    import_item(screen, os.path.join(baseDir, "tempSave/editSave.json"))
    for new_item_maker in new_item_makers:
        new_item_maker.shown = False
    for item in items:
        item.shown = True
    try:
        os.remove(os.path.join(baseDir, "tempSave/editSave.json"))
    except:
        pass

def submit_item(*args):
    global itemColor
    common = {}
    for i in range(len(new_item_makers)):
        text = new_item_makers[i]
        if text not in buttons:
            common[text.placeholderText[6:]] = text.inputText
    keys = list(common.keys())
    for key in keys:
        if common[key] == "":
            return
    create_item({"shown": True, "pos": [0, 0], "selected": False, "perameters": {
                    "COMMON": common,
                    "SPECIALIST": {
                    }
                },
                "commonKeys": keys, "colorWidth": 20, "relPos": [0, 0],"color": itemColor, "screenWidth": WIDTH, "screenHeight": HEIGHT}, [250, 150], screen)
    for new_item_maker in new_item_makers:
        new_item_maker.shown = False
    for item in items:
        item.shown = True

def import_item(screen, filename = None, *args):
    if not filename:
        filename = tkinter.filedialog.askopenfilename(
                                                                    title="Select File To Import",
                                                                    initialdir=os.path.join(baseDir, "SavedItems"),
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