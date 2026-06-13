import pygame
from colorPicker import ColorPicker

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

class Item:
    def __init__(self, perameters, commonKeys, screen):
        self.pos = (100, 100)
        self.selected = False
        self.screen = screen
        self.perameters = perameters
        self.commonKeys = commonKeys
        self.color = (0, 255, 0)
        self.colorWidth = 20
        self.relPos = [0, 0]
        self.setup_font()
    
    def setup_font(self):
        self.headSize = 30
        self.bodySize = 20
        self.spacing = 10
        self.specialistKeys = list(self.perameters["SPECIALIST"].keys())
        self.headFont = pygame.font.SysFont("comicsansms", 22)
        self.font = pygame.font.SysFont("comicsansms", 18)
        self.numItems = len(self.perameters["COMMON"]) + len(self.perameters["SPECIALIST"])
        self.height = (self.spacing + self.bodySize) * (self.numItems - 1) + self.headSize + 2 * self.spacing
        self.keys = self.commonKeys + self.specialistKeys
        self.items = [self.perameters["COMMON"][key] for key in self.commonKeys] + [self.perameters["SPECIALIST"][key] for key in self.specialistKeys]
        self.text = [self.font.render(f"{self.keys[i]}: {self.items[i]}", 1, (255, 255, 255)) for i in range(self.numItems)]
        self.text[0] = self.headFont.render(self.items[0], 1, (255, 255, 255))
        self.widths = [i.get_rect()[2] for i in self.text]
        self.size = (max(self.widths) + self.spacing * 2 + self.colorWidth, self.height)
    
    def draw(self):
        pygame.draw.rect(self.screen, self.color, pygame.Rect(self.pos[0], self.pos[1], max(self.widths) + self.spacing * 2 + self.colorWidth, self.height), border_radius=10)
        pygame.draw.rect(self.screen, (20, 20, 20), pygame.Rect(self.pos[0], self.pos[1], max(self.widths) + self.spacing * 2, self.height), border_radius=10)
        textPos = [self.pos[0] + self.spacing] + list(self.text[0].get_rect(center = self.pos))[1:]
        textPos[1] += self.spacing + self.headSize // 2
        self.screen.blit(self.text[0], textPos)
        textPos[1] += self.spacing + self.bodySize // 2 + self.headSize // 2
        for i in range(1, self.numItems):
            self.screen.blit(self.text[i], textPos)
            textPos[1] += self.spacing + self.bodySize
    
    def is_clicked(self, pos):
        clicked = True
        for i in range(2):
            if not self.pos[i] <= pos[i] <= self.size[i] + self.pos[i]:
                clicked = False
        return clicked
    
    def event_handle(self, event):
        pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_clicked(pos):
                self.selected = True
                self.relPos = [pos[i] - self.pos[i] for i in range(2)]
        if event.type == pygame.MOUSEBUTTONUP:
            self.selected = False
    
    def update_position(self):
        # print(self.selected)
        if self.selected:
            pos = pygame.mouse.get_pos()
            self.pos = [min(max(pos[0] - self.relPos[0], 0), WIDTH - self.size[0]),
                        min(max(pos[1] - self.relPos[1], 0), HEIGHT - self.size[1])
                        ]
    
commonKeys = ["NAME", "BRAND", "WEIGHT", "COLOR", "CATEGORY"]
testItemPeramters = {   
                        "COMMON":{
                            "NAME": "Atmos AG 65",
                            "BRAND": "Osprey",
                            "WEIGHT": 2.09,
                            "COLOR": "Blue",
                            "CATEGORY": "Bag"
                        },
                        "SPECIALIST":{
                            "CAPACITY": "65 Litres"
                        }
                    }
testItem = Item(testItemPeramters, commonKeys, screen)


running = True
colorPick = ColorPicker(screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        colorPick.event_handle(event)
        testItem.event_handle(event)
    colorPick.update_position()
    testItem.update_position()
    screen.fill((0, 0, 0))
    testItem.draw()
    colorPick.draw()
    pygame.display.flip()
pygame.quit()