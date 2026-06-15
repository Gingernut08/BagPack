import pygame, json
from item import Item, items

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

trash = pygame.transform.scale(pygame.image.load("trash.png").convert_alpha(), (40, 40))
trashRect = trash.get_rect(center = (20, 20))

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


with open("save.json") as f:
    data = json.load(f)

for item_data in data["items"]:
    item = Item(
        item_data["perameters"],
        item_data["commonKeys"],
        screen,
        item_data["screenWidth"],
        item_data["screenHeight"]
    )

    item.shown = item_data["shown"]
    item.pos = tuple(item_data["pos"])
    item.selected = item_data["selected"]
    item.colorWidth = item_data["colorWidth"]
    item.relPos = item_data["relPos"]
    item.color = tuple(item_data["color"])

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
        for item in items:
            item.event_handle(event)
    for item in items:
        item.update_position()
    screen.fill((0, 0, 0))
    screen.blit(trash, trashRect)
    for item in items:
        item.draw()
    pygame.display.flip()
pygame.quit()

data = {"items": [item.to_dict() for item in items]}
with open('save.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)