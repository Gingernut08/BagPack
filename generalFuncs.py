from varSetup import screen, items, buttons, WIDTH, HEIGHT, topSpacing, bottomSpacing, numRightButtons, numLeftButtons
from guiElements import Button, TextInput
from buttonFunctions import import_item
from colorPicker import from_8Bit_RGB

def draw():
    screen.fill((0, 0, 0))
    for button in buttons:    button.draw()
    for item in items:    item.draw()


def create_text():
    i = TextInput

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
    button = Button((0, topSpacing + i * (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons), 200, (HEIGHT - topSpacing - bottomSpacing) // numLeftButtons, "NEW", None, None, screen)