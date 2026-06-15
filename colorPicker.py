import colorsys, pygame

def to_8Bit_RGB(color):
    return [255 * i for i in color]

def from_8Bit_RGB(color):
    return [i / 255 for i in color]

class ColorSlider:
    def __init__(self, pos, width, height, type, group, screen):
        self.width = width
        self.height = height
        self.pos = pos
        self.focused = False
        self.value = 0
        self.type = type
        self.group = group
        self.screen = screen

    def is_clicked(self, pos):
        return self.pos[0] <= pos[0] <= self.pos[0] + self.width and self.pos[1] <= pos[1] <= self.pos[1] + self.height

    def draw(self):
        self.colors = [i / self.width for i in range(self.width)]
        self.hlsColor = self.group.hlsColor
        for i in range(self.width):
            self.hlsColor[self.type] = self.colors[i]
            self.rgbColor = to_8Bit_RGB(colorsys.hls_to_rgb(*self.hlsColor))
            pygame.draw.rect(self.screen, (self.rgbColor), pygame.Rect(self.pos[0] + i, self.pos[1], 1, self.height))
        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.pos[0] + self.width * self.value, self.pos[1], 1, self.height))

    def event_handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if self.is_clicked(pos):
                self.focused = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.focused = False
    
    def update_position(self, pos):
        if self.focused:
            self.value = min(max((pos[0] - self.pos[0]) / self.width, 0), 1)

class ColorPicker:
    def __init__(self, screen):
        self.shown = False
        self.pos = [100, 100]
        self.sliderWidth = 300
        self.sliderHeight = 20
        self.sliderSpacing = 10
        self.width = self.sliderWidth + self.sliderHeight * 3 + self.sliderSpacing * 3 + 2 * self.sliderSpacing
        self.height = self.sliderHeight * 3 + self.sliderSpacing * 2 + 2 * self.sliderSpacing
        self.sliderPos = [[self.sliderSpacing + self.pos[0], self.sliderSpacing + self.pos[1] + i * (self.sliderHeight + self.sliderSpacing)] for i in range(3)]
        self.types = [0, 1, 2]
        self.sliders = [ColorSlider(self.sliderPos[i], self.sliderWidth, self.sliderHeight, self.types[i], self, screen) for i in range(len(self.sliderPos))]
        self.sliders[1].value = 1
        self.hlsColor = [0, 0, 0]
        self.rgbColor = colorsys.hsv_to_rgb(*self.hlsColor)
        self.font = pygame.font.SysFont("comicsansms", 18)
        self.screen = screen
        self.submit = False
    
    def event_handle(self, event):
        if self.shown:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.pos[0] + self.width - self.height + self.sliderSpacing <= pos[0] <= self.pos[0] + self.width - self.sliderSpacing:
                    if self.pos[1] + self.sliderHeight * 2 + self.sliderSpacing * 3 <= pos[1] <= self.pos[1] + self.height - self.sliderSpacing:
                        self.submit = True
                if not (self.pos[0] <= pos[0] <= self.pos[0] + self.width and self.pos[1] <= pos[1] <= self.pos[1] + self.height):
                    self.shown = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.submit = True
            for slider in self.sliders:
                slider.event_handle(event)
    
    def update_position(self):
        pos = pygame.mouse.get_pos()
        for slider in self.sliders:
            slider.update_position(pos)
        self.sliderPos = [[self.sliderSpacing + self.pos[0], self.sliderSpacing + self.pos[1] + i * (self.sliderHeight + self.sliderSpacing)] for i in range(3)]
        for i in range(3):
            self.sliders[i].pos = self.sliderPos[i]
    
    def update_color(self):
        self.hlsColor = [slider.value for slider in self.sliders]
        self.rgbColor = colorsys.hls_to_rgb(*self.hlsColor)
    
    def draw(self):
        if self.shown:
            pygame.draw.rect(self.screen, (20, 20, 20), pygame.Rect(self.pos[0], self.pos[1], self.width, self.height))
            renderText = self.font.render("Submit", 1, (0, 0, 0))
            textPos = (self.pos[0] + self.sliderWidth + self.sliderSpacing * 3 + self.sliderHeight * 1.5, self.pos[1] + self.sliderHeight * 2.5 + self.sliderSpacing * 3)
            textRect = renderText.get_rect(center = textPos)
            for slider in self.sliders:
                self.update_color()
                slider.draw()
            pygame.draw.rect(self.screen, to_8Bit_RGB(self.rgbColor), pygame.Rect(self.pos[0] + self.sliderWidth + self.sliderSpacing * 2, self.pos[1] + self.sliderSpacing, self.sliderHeight * 3 + self.sliderSpacing * 2, self.sliderHeight * 2 + self.sliderSpacing))
            pygame.draw.rect(self.screen, (200, 200, 200), pygame.Rect(self.pos[0] + self.sliderWidth + self.sliderSpacing * 2, self.pos[1] + self.sliderHeight * 2 + self.sliderSpacing * 3, self.sliderHeight * 3 + self.sliderSpacing * 2, self.sliderHeight))
            self.screen.blit(renderText, textRect)