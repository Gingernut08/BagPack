from imports import tkinter, json, os
from item import create_item, new_item, focus_pygame_window
from guiElements import Button, TextInput
from varSetup import numPerametersAdit, maxAditPerameters, buttons, clickables, texts, yOfset, xOfset, xPos, xSpacing, ySpacing, new_item_makers, items, WIDTH, HEIGHT, screen, leftSpacing, topSpacing, bottomSpacing, numLeftButtons, numRightButtons, itemColor, baseDir, buttons

def create_new_item_picker():
    global yOfset
    yOfset = 0
    xOfset = 0
    text = TextInput((xPos, topSpacing + yOfset * ySpacing), 400, 60, "ENTER NAME", screen)
    yOfset += 1
    text = TextInput((xPos, topSpacing + yOfset * ySpacing), 400, 60, "ENTER BRAND", screen)
    yOfset += 1
    text = TextInput((xPos, topSpacing + yOfset * ySpacing), 400, 60, "ENTER WEIGHT", screen)
    yOfset += 1
    text = TextInput((xPos, topSpacing + yOfset * ySpacing), 400, 60, "ENTER COLOR", screen)
    yOfset += 1
    text = TextInput((xPos, topSpacing + yOfset * ySpacing), 400, 60, "ENTER CATEGORY", screen)
    yOfset += 1
    
    xOfset = 0
    button = Button((xPos + xOfset * 250, topSpacing + yOfset * ySpacing), 150, 60, "CANCEL", cancel, None, screen)
    new_item_makers.insert(0, button)
    xOfset += 1
    button = Button((xPos + xOfset * 250, topSpacing + yOfset * ySpacing), 150, 60, "SUBMIT", submit_item, None, screen)
    new_item_makers.insert(0, button)
    
    # yOfset = 0    
    # button = Button((xSpacing + xPos, topSpacing + yOfset * 100), 750, 60, "ADD NEW PERAMETER", add_perameter, None, screen)
    # new_item_makers.insert(0, button)
    
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

def add_perameter(*args):
    global yOfset, numPerametersAdit, maxAditPerameters
    if numPerametersAdit == maxAditPerameters:
        return
    numPerametersAdit += 1
    
    perameterButton = new_item_makers.pop(0)
    buttons.remove(perameterButton)
    clickables.remove(perameterButton)
    
    xOfset = 0
    text = TextInput((xSpacing + xPos + xOfset * 250, topSpacing + yOfset * ySpacing), 300, 60, "ENTER PERAMETER", screen)
    xOfset += 1
    text = TextInput((xSpacing + xPos + xOfset * 350, topSpacing + yOfset * ySpacing), 300, 60, "ENTER VALUE", screen)
    xOfset += 1
    button = Button((xSpacing + xPos + xOfset * 350, topSpacing + yOfset * ySpacing), 50, 60, "X", remove_perameter, None, screen)
    button.perameters = [button, None]
    new_item_makers.append(button)
    yOfset += 1
    
    
    if numPerametersAdit != maxAditPerameters:
        button = Button((xSpacing + xPos, topSpacing + yOfset * 100), 750, 60, "ADD NEW PERAMETER", add_perameter, None, screen)
        new_item_makers.insert(0, button)

def remove_perameter(closeButton, *args):
    global yOfset, numPerametersAdit
    numPerametersAdit -= 1
    
    if new_item_makers[0].text == "ADD NEW PERAMETER":
        perameterButton = new_item_makers.pop(0)
        buttons.remove(perameterButton)
        clickables.remove(perameterButton)
    
    closeIndex = new_item_makers.index(closeButton)

    yOfset -= 1

    for i in range(1, 1 + (len(new_item_makers) - closeIndex + 1) // 3):
        j = 0
        for j in reversed(range(3)):
            new_item_makers[1 - 3 * i - j].pos = (j * 350 + xSpacing + xPos, topSpacing + (yOfset - i) * 100)
            print(new_item_makers[1 - 3 * i - j].text, new_item_makers[1 - 3 * i - j].pos)
    
    
    new_item_makers.remove(closeButton)
    buttons.remove(closeButton)
    clickables.remove(closeButton)
    perameterName = new_item_makers.pop(closeIndex - 2)
    texts.remove(perameterName)
    clickables.remove(perameterName)
    perameterValue = new_item_makers.pop(closeIndex - 2)
    texts.remove(perameterValue)
    clickables.remove(perameterValue)
    
    for i in range(1 + (len(new_item_makers) - closeIndex + 1) // 3):
        new_item_makers[-1 - 3 * i].pos = (new_item_makers[-1 - 3 * i].pos[0], new_item_makers[-1 - 3 * i].pos[1] - 100)
    
    button = Button((xSpacing + xPos, topSpacing + yOfset * 100), 750, 60, "ADD NEW PERAMETER", add_perameter, None, screen)
    new_item_makers.insert(0, button)


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