from imports import  pygame
from item import Item, save_item_states, recall_item_states
from varSetup import root, screen, WIDTH, HEIGHT, items, buttons
from generalFuncs import draw, create_buttons
from buttonFunctions import import_item

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


# from guiElements import Button
# def buttonFunc():
#     print("TEST BUTTON PRESSED")
# buttonPerameters = (
#                         (200, 200),
#                         200, 
#                         100, 
#                         "TEST",
#                         buttonFunc,
#                         screen
#                     )
# Button(*buttonPerameters)


create_buttons()

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
                import_item(screen)

        for item in items:    item.event_handle(event)
        for button in buttons:    button.event_handle(event)
    for item in items:    item.update_position()
    draw()
    pygame.display.flip()

pygame.quit()
save_item_states()