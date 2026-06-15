from item import Item, items, pygame, tkinter, json, colorsys, from_8Bit_RGB, focus_pygame_window
import ctypes

root = tkinter.Tk()
root.withdraw()

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

trash = pygame.transform.scale(pygame.image.load("trash.png").convert_alpha(), (40, 40))
save = pygame.transform.scale(pygame.image.load("save.png").convert_alpha(), (40, 40))
trashRect = trash.get_rect(center = (20, 20))
saveRect = save.get_rect(center = (WIDTH - 20, 20))

commonKeys = ["NAME", "BRAND", "WEIGHT", "COLOR", "CATEGORY"]
testItemPeramters = {   
                        "COMMON":{
                            "NAME": "Atmos AG 65",
                            "BRAND": "Osprey",
                            "WEIGHT": 2.09,
                            "COLOR": "Blue",
                            "CATEGORY": "Bag"
                        },
                        "SPECIALIST":{
                            "CAPACITY": "65 Litres"
                        }
                    }
# testItem = Item(testItemPeramters, commonKeys, screen, WIDTH, HEIGHT)

def create_item(data, pos):
    item = Item(
        data["perameters"],
        data["commonKeys"],
        screen,
        data["screenWidth"],
        data["screenHeight"]
    )

    item.shown = data["shown"]
    item.pos = pos
    item.selected = data["selected"]
    item.colorWidth = data["colorWidth"]
    item.relPos = data["relPos"]
    item.color = tuple(data["color"])
    item.picker.hlsColor = colorsys.rgb_to_hls(*from_8Bit_RGB(data["color"]))
    item.picker.rgbColor = from_8Bit_RGB(item.color)
    for i in range(3):
        item.picker.sliders[i].value = item.picker.hlsColor[i]


with open("save.json") as f:
    data = json.load(f)

for item_data in data["items"]:
    create_item(item_data, item_data["pos"])

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                Item(testItemPeramters, commonKeys, screen, WIDTH, HEIGHT)
            if event.key == pygame.K_BACKSPACE:
                filename = tkinter.filedialog.askopenfilename(
                                                                title="Select File To Import",
                                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
                                                            )
                if filename:
                    try:
                        with open(filename) as f:
                            data = json.load(f)
                        create_item(data, [100, 100])
                    except:
                        pass
                focus_pygame_window()
        for item in items:
            item.event_handle(event)
    for item in items:
        item.update_position()
    screen.fill((0, 0, 0))
    screen.blit(trash, trashRect)
    screen.blit(save, saveRect)
    for item in items:
        item.draw()
    pygame.display.flip()
pygame.quit()

data = {"items": [item.to_dict() for item in items]}
with open('save.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)