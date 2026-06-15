from imports import pygame, colorsys, tkinter, json
from colorPicker import ColorPicker, to_8Bit_RGB, from_8Bit_RGB
from generalFuncs import focus_pygame_window
from varSetup import items

def create_item(data, pos, screen):
    item = Item(
        data["perameters"],
        data["commonKeys"],
        screen,
        data["screenWidth"],
        data["screenHeight"]
    )

    item.shown = data["shown"]
    item.pos = pos
    item.selected = data["selected"]
    item.colorWidth = data["colorWidth"]
    item.relPos = data["relPos"]
    item.color = tuple(data["color"])
    item.picker.hlsColor = colorsys.rgb_to_hls(*from_8Bit_RGB(data["color"]))
    item.picker.rgbColor = from_8Bit_RGB(item.color)
    for i in range(3):
        item.picker.sliders[i].value = item.picker.hlsColor[i]

def import_item(screen):
    filename = tkinter.filedialog.askopenfilename(
                                                                title="Select File To Import",
                                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
                                                            )
    if filename:
        try:
            with open(filename) as f:
                data = json.load(f)
            create_item(data, [100, 100], screen)
        except:
            pass
    focus_pygame_window()

def save_item_states():
    data = {"items": [item.to_dict() for item in items]}
    with open('save.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def recall_item_states(screen):
    with open("save.json") as f:
        data = json.load(f)
    for item_data in data["items"]:
        create_item(item_data, item_data["pos"], screen)

class Item:
    def __init__(self, perameters, commonKeys, screen, WIDTH, HEIGHT):
        items.append(self)
        self.shown = True
        self.pos = [100, 100]
        self.selected = False
        self.screen = screen
        self.perameters = perameters
        self.commonKeys = commonKeys
        self.colorWidth = 20
        self.relPos = [0, 0]
        self.picker = ColorPicker(self.screen)
        self.color = (255, 255, 255)
        self.setup_font()
        self.screenWidth = WIDTH
        self.screenHeight = HEIGHT
        self.picker.pos = [self.pos[0] + self.size[0] + self.spacing, self.pos[1]]
    
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
    
    def delete(self):
        items.remove(self)
    
    def to_dict(self):
        return {
            "shown": self.shown,
            "pos": list(self.pos),
            "selected": self.selected,
            "perameters": self.perameters,
            "commonKeys": self.commonKeys,
            "colorWidth": self.colorWidth,
            "relPos": self.relPos,
            "color": list(self.color),
            "screenWidth": self.screenWidth,
            "screenHeight": self.screenHeight
        }
    
    def save(self):
        data = self.to_dict()
        filename = tkinter.filedialog.asksaveasfilename(
                                                title="Save File",
                                                defaultextension=".json",
                                                filetypes=[("JSON files", "*.json")]
                                            )
        if filename:
            with open(filename, "w") as f:
                json.dump(data, f, indent=4)
            self.delete()
        else:
            self.pos = [self.screenWidth - self.size[0] - 50, 50]
        focus_pygame_window()
    
    def draw(self):
        if self.shown:
            backgroundColor = (20, 20, 20)
            if self.pos[0] <= 40 and self.pos[1] <= 40:
                backgroundColor = (40, 20, 20)
            if self.screenWidth - self.size[0] - self.pos[0] <= 40 and self.pos[1] <= 40:
                backgroundColor = (20, 40, 20)
            pygame.draw.rect(self.screen, self.color, pygame.Rect(self.pos[0], self.pos[1], max(self.widths) + self.spacing * 2 + self.colorWidth, self.height), border_radius=10)
            pygame.draw.rect(self.screen, backgroundColor, pygame.Rect(self.pos[0], self.pos[1], max(self.widths) + self.spacing * 2, self.height), border_radius=10)
            textPos = [self.pos[0] + self.spacing] + list(self.text[0].get_rect(center = self.pos))[1:]
            textPos[1] += self.spacing + self.headSize // 2
            self.screen.blit(self.text[0], textPos)
            textPos[1] += self.spacing + self.bodySize // 2 + self.headSize // 2
            for i in range(1, self.numItems):
                self.screen.blit(self.text[i], textPos)
                textPos[1] += self.spacing + self.bodySize
            self.picker.draw()
    
    def is_clicked(self, pos):
        clicked = True
        for i in range(2):
            if not self.pos[i] <= pos[i] <= self.size[i] + self.pos[i]:
                clicked = False
        return clicked
    
    def is_color_clicked(self, pos):
        if self.pos[0] + self.size[0] - self.colorWidth <= pos[0] <= self.size[0] + self.pos[0]:
            return self.pos[1] <= pos[1] <= self.size[1] + self.pos[1]
        return False
    
    def event_handle(self, event):
        if self.shown:
            if not self.picker.shown:
                color = colorsys.rgb_to_hls(*[self.color[i] / 255 for i in range(3)])
                for i in range(3):
                    self.picker.sliders[i].value = color[i]
            self.picker.event_handle(event)
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.is_color_clicked(pos):
                    self.picker.shown = True
                if self.is_clicked(pos):
                    self.selected = True
                    self.relPos = [pos[i] - self.pos[i] for i in range(2)]
            if event.type == pygame.MOUSEBUTTONUP:
                self.selected = False
                if self.pos[0] <= 40 and self.pos[1] <= 40:
                    self.delete()
                if self.screenWidth - self.size[0] - self.pos[0] <= 40 and self.pos[1] <= 40:
                    self.save()
            if self.picker.submit:
                self.color = to_8Bit_RGB(self.picker.rgbColor)
                self.picker.submit = False
                self.picker.shown = False
    
    def update_position(self):
        for item in reversed(items):
            if item.selected and item != self:
                self.selected = False
            if item.picker.shown and item != self:
                self.picker.shown = False
            if self.selected and items[-1] != self:
                items.remove(self)
                items.append(self)
        if self.selected:
            pos = pygame.mouse.get_pos()
            self.pos = [min(max(pos[0] - self.relPos[0], 0), self.screenWidth - self.size[0]),
                        min(max(pos[1] - self.relPos[1], 0), self.screenHeight - self.size[1])
                        ]
        self.picker.update_position()
        self.picker.pos = [self.pos[0] + self.size[0] + self.spacing, self.pos[1]]
