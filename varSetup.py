from imports import pygame, tkinter

items = []
buttons = []
clickables = []
texts = []

root = tkinter.Tk()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

tabPress = False

topSpacing = 100
bottomSpacing = 0
leftSpacing = 200
rightSpacing = 100
numRightButtons = 3
numLeftButtons = 2