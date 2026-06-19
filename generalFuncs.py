from imports import pygame, random, ctypes
from varSetup import screen, clickables, new_item_makers, buttons

def draw():
    screen.fill((0, 0, 0))
    for clickable in clickables: clickable.draw()

def cycle_text_boxes(event, tabPress):
    if event.key == pygame.K_TAB:
        for new_item_maker in new_item_makers:
            if not tabPress:
                if new_item_maker not in buttons:
                    tabPress = new_item_maker.tab_check()
        if not tabPress:
            new_item_makers[0].selected = True
            tabPress = True
    return tabPress

def random_color():
    return [random.randint(100, 255) for _ in range(3)]
