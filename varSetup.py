from imports import pygame, tkinter

items = []
buttons = []

root = tkinter.Tk()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

topSpacing = 100
bottomSpacing = 0
leftSpacing = 100
rightSpacing = 100
numLeftButtons = 4