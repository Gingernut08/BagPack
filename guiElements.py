from imports import pygame
from varSetup import buttons, clickables, new_item_makers, tabPress

class Button:
    def __init__(self, pos, width, height, text, function, perameters, screen):
        buttons.append(self)
        clickables.append(self)
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
    
    def run_function_check(self):
        if self.selected:
            self.selected = False
            if self.function:
                if self.perameters:
                    self.function(*self.perameters)
                else:
                    self.function()
    
    def event_handle(self, event):
        if self.shown:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_clicked(pos):
                    self.selected = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.run_function_check()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                    self.run_function_check()

class TextInput:
    def __init__(self, pos, width, height, text, screen):
        clickables.append(self)
        new_item_makers.append(self)
        self.pos = pos
        self.width = width
        self.height = height
        self.placeholderText = text
        self.screen = screen
        self.text= self.placeholderText
        self.inputText = ""
        self.shown = True
        self.selected = False
        self.color = (20, 20, 20)
        self.highlightColor = (40, 40, 40)
        self.selectColor = (80, 80, 80)
        self.font = pygame.font.SysFont("comicsansms", 24)
        self.placeholderColor = (150, 150, 150)
        self.renderedText = self.font.render(self.text, 1, (255, 255, 255))
    
    def is_clicked(self, pos):
        return 0 <= pos[0] - self.pos[0] <= self.width and 0 <= pos[1] - self.pos[1] <= self.height
    
    def draw(self):
        textColor = (255, 255, 255)
        text = self.inputText
        if self.inputText == "":
            textColor = self.placeholderColor
            text = self.placeholderText
        pos = pygame.mouse.get_pos()
        color = self.color
        if self.is_clicked(pos):
            color = self.highlightColor
        if self.selected:
            color = self.selectColor
        self.renderedText = self.font.render(text, 1, textColor)
        textRect = self.renderedText.get_rect(center = (self.pos[0] + self.width // 2, self.pos[1] + self.height // 2))
        while textRect[2] >= self.width - 10:
            self.text = text[1:]
            self.renderedText = self.font.render(text, 1, textColor)
            textRect = self.renderedText.get_rect(center = (self.pos[0] + self.width // 2, self.pos[1] + self.height // 2))
        if self.shown:
            borderWidth = 2
            pygame.draw.rect(self.screen, color, pygame.Rect(self.pos[0] + borderWidth, self.pos[1] + borderWidth, self.width - 2 * borderWidth, self.height - 2 * borderWidth), border_radius=10 - borderWidth)
            pygame.draw.rect(self.screen, (150, 150, 150), pygame.Rect(self.pos[0], self.pos[1], self.width, self.height), borderWidth, 10)
            self.screen.blit(self.renderedText, textRect)
    
    def tab_check(self):
        if self.selected and not tabPress:
            self.selected = False
            new_item_makers[(new_item_makers.index(self) + 1) % len(new_item_makers)].selected = True
            return True
        return False
    
    def event_handle(self, event):
        if self.shown:
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.selected = False
                if self.is_clicked(pos):
                    self.selected = True
            if event.type == pygame.MOUSEBUTTONUP:
                self.selected = False
                if self.is_clicked(pos):
                    self.selected = True
            if self.selected:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.inputText = self.inputText[:-1]
                    if event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                        self.selected = False
                    if event.unicode.isprintable():
                        self.inputText = self.inputText + event.unicode