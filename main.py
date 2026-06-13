import pygame
from colorPicker import ColorPicker

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

class Item:
    def __init__(self, perameters, commonKeys, screen):
        self.screen = screen
        self.headSize = 30
        self.bodySize = 20
        self.spacing = 10
        self.perameters = perameters
        self.commonKeys = commonKeys
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
    
    def draw(self, pos):
        pygame.draw.rect(self.screen, (20, 20, 20), pygame.Rect(pos[0], pos[1], max(self.widths) + self.spacing * 2, self.height), border_radius=10)
        textPos = [pos[0] + self.spacing] + list(self.text[0].get_rect(center = pos))[1:]
        textPos[1] += self.spacing + self.headSize // 2
        self.screen.blit(self.text[0], textPos)
        textPos[1] += self.spacing + self.bodySize // 2 + self.headSize // 2
        for i in range(1, self.numItems):
            self.screen.blit(self.text[i], textPos)
            textPos[1] += self.spacing + self.bodySize

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
    colorPick.update_position(pygame.mouse.get_pos())
    screen.fill((0, 0, 0))
    testItem.draw((100, 100))
    colorPick.draw()
    pygame.display.flip()
pygame.quit()