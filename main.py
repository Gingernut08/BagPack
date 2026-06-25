from imports import  pygame
from item import save_item_states, recall_item_states
from varSetup import root, screen, items, clickables, new_item_makers, texts
from generalFuncs import draw, cycle_text_boxes
from buttonFunctions import create_buttons, create_new_item_picker

pygame.init()
pygame.font.init()
root.withdraw()

running = True

recall_item_states(screen)

create_buttons()
create_new_item_picker()

while running:
    tabPress = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            tabPress = cycle_text_boxes(event, tabPress)

        for clickable in clickables:    clickable.event_handle(event)
    for item in items:    item.update_position()
    draw()
    pygame.display.flip()

pygame.quit()
for clickable in clickables:
    clickable.selected = False
save_item_states()