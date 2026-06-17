from imports import  pygame
from item import save_item_states, recall_item_states
from varSetup import root, screen, items, clickables, texts
from generalFuncs import draw, create_buttons, create_text, cycle_text_boxes

pygame.init()
pygame.font.init()
root.withdraw()

commonKeys = [
    "NAME", "BRAND", "WEIGHT", "COLOR", "CATEGORY"
    ]
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

running = True

recall_item_states(screen)

create_buttons()
create_text()

while running:
    tabPress = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_BACKSPACE:
                for text in texts:
                    text.shown = not text.shown

            tabPress = cycle_text_boxes(event, tabPress)

        for clickable in clickables:    clickable.event_handle(event)
    for item in items:    item.update_position()
    draw()
    pygame.display.flip()

pygame.quit()
save_item_states()