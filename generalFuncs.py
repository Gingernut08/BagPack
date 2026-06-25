from imports import pygame, random
from varSetup import screen, clickables, new_item_makers, buttons, texts

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

def random_color():
    return [random.randint(100, 255) for _ in range(3)]
