from varSetup import screen, items, buttons, HEIGHT, topSpacing, bottomSpacing, numLeftButtons
from guiElements import Button
from buttonFunctions import import_item
from colorPicker import from_8Bit_RGB

def draw():
    screen.fill((0, 0, 0))
    for button in buttons:    button.draw()
    for item in items:    item.draw()

def create_buttons():
    button = Button((0, topSpacing), 200, (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons, "DELETE", None, None, screen)
    button.color = (40, 20, 20)
    button = Button((0, topSpacing + (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons), 200, (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons, "SAVE", None, None, screen)
    button.color = (20, 40, 20)
    button = Button((0, topSpacing + 2 * (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons), 200, (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons, "IMPORT", import_item, (screen, None), screen)
    button = Button((0, topSpacing + 3 * (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons), 200, (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons, "NEW", None, None, screen)