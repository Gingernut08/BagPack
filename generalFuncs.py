from imports import pygame
from varSetup import screen, clickables, WIDTH, HEIGHT, leftSpacing, topSpacing, bottomSpacing, numRightButtons, numLeftButtons, texts
from guiElements import Button, TextInput
from buttonFunctions import import_item

def draw():
    screen.fill((0, 0, 0))
    for clickable in clickables: clickable.draw()

def cycle_text_boxes(event, tabPress):
    if event.key == pygame.K_TAB:
        for text in texts:
            if not tabPress:
                tabPress = text.tab_check()
        if not tabPress:
            texts[0].selected = True
            tabPress = True
    return tabPress

def create_text():
    xPos = leftSpacing * 2
    i = 0
    text = TextInput((xPos, topSpacing + i * 100), 400, 60, "ENTER NAME", screen)
    i += 1
    text = TextInput((xPos, topSpacing + i * 100), 400, 60, "ENTER BRAND", screen)
    i += 1
    text = TextInput((xPos, topSpacing + i * 100), 400, 60, "ENTER WEIGHT", screen)
    i += 1
    text = TextInput((xPos, topSpacing + i * 100), 400, 60, "ENTER WEIGHT", screen)
    i += 1
    text = TextInput((xPos, topSpacing + i * 100), 400, 60, "ENTER COLOR", screen)
    i += 1
    text = TextInput((xPos, topSpacing + i * 100), 400, 60, "ENTER CATEGORY", screen)

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