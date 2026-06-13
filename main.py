import pygame, json
from item import Item, items

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)



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
testItem = Item(testItemPeramters, commonKeys, screen, WIDTH, HEIGHT)


# with open('save.json') as f:
#     data = json.load(f)
# items = data["items"]

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        for item in items:
            item.event_handle(event)
    for item in items:
        item.update_position()
    screen.fill((0, 0, 0))
    for item in items:
        item.draw()
    pygame.display.flip()
pygame.quit()

# data = {"items": items}
# with open('save.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)