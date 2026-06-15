from imports import pygame
from varSetup import buttons

class Button:
    def __init__(self, pos, width, height, text, function, perameters, screen):
        buttons.append(self)
        self.pos = pos
        self.width = width
        self.height = height
        self.text = text
        self.function = function
        self.perameters = perameters
        self.screen = screen
        self.shown = True
        self.selected = False
        self.color = (20, 20, 20)
        self.highlightColor = (40, 40, 40)
        self.selectColor = (80, 80, 80)
        self.font = pygame.font.SysFont("comicsansms", 24)
        self.renderedText = self.font.render(self.text, 1, (255, 255, 255))
    
    def draw(self):
        pos = pygame.mouse.get_pos()
        color = self.color
        if self.function:
            if self.is_clicked(pos):
                color = self.highlightColor
            if self.selected:
                color = self.selectColor
        if self.shown:
            borderWidth = 2
            pygame.draw.rect(self.screen, color, pygame.Rect(self.pos[0] + borderWidth, self.pos[1] + borderWidth, self.width - 2 * borderWidth, self.height - 2 * borderWidth), border_radius=10 - borderWidth)
            pygame.draw.rect(self.screen, (150, 150, 150), pygame.Rect(self.pos[0], self.pos[1], self.width, self.height), borderWidth, 10)
            self.screen.blit(self.renderedText, self.renderedText.get_rect(center = (self.pos[0] + self.width // 2, self.pos[1] + self.height // 2)))
    
    def is_clicked(self, pos):
        return 0 <= pos[0] - self.pos[0] <= self.width and 0 <= pos[1] - self.pos[1] <= self.height
    
    def event_handle(self, event):
        if self.shown:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_clicked(pos):
                    self.selected = True
            if event.type == pygame.MOUSEBUTTONUP:
                if self.selected:
                    self.selected = False
                    if self.function:
                        self.function(*self.perameters)