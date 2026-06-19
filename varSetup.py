from imports import pygame, tkinter, os

items = []
buttons = []
clickables = []
new_item_makers = []

itemColor = [255, 255, 255]

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

baseDir = os.path.dirname(os.path.abspath(__file__))