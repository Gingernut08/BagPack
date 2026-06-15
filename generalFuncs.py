from imports import pygame, ctypes
from varSetup import screen, images, items

def focus_pygame_window():
    wm_info = pygame.display.get_wm_info()
    hwnd = wm_info.get("window")

    if hwnd:
        ctypes.windll.user32.ShowWindow(hwnd, 5)
        ctypes.windll.user32.SetForegroundWindow(hwnd)

def draw():
    screen.fill((0, 0, 0))
    for image in images:    screen.blit(*image)
    for item in items:    item.draw()
    pygame.display.flip()
