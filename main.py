from imports import  pygame
from item import save_item_states, recall_item_states
from varSetup import root, screen, items, clickables, new_item_makers
from generalFuncs import draw, cycle_text_boxes
from buttonFunctions import create_buttons, create_new_item_picker

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
create_new_item_picker()

for new_item_maker in new_item_makers:
    new_item_maker.shown = False
for item in items:
    item.shown = True

while running:
    tabPress = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_1:
                for new_item_maker in new_item_makers:
                    new_item_maker.shown = not new_item_maker.shown
                    
            if event.key == pygame.K_2:
                for item in items:
                    item.shown = not item.shown

            tabPress = cycle_text_boxes(event, tabPress)

        for clickable in clickables:    clickable.event_handle(event)
    for item in items:    item.update_position()
    draw()
    pygame.display.flip()

pygame.quit()
for clickable in clickables:
    clickable.selected = False
save_item_states()