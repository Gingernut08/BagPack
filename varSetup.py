from imports import pygame, tkinter

items = []

root = tkinter.Tk()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

trash = pygame.transform.scale(pygame.image.load("trash.png").convert_alpha(), (40, 40))
trashRect = trash.get_rect(center = (20, 20))

save = pygame.transform.scale(pygame.image.load("save.png").convert_alpha(), (40, 40))
saveRect = save.get_rect(center = (WIDTH - 20, 20))

images = [
    [trash, trashRect],
    [save, saveRect]
]