import colorsys, pygame

pygame.init()

class Slider:
    def __init__(self, pos, width, height, type, group):
        # sliders.append(self)
        self.width = width
        self.height = height
        self.pos = pos
        self.focused = False
        self.value = 0
        self.type = type
        self.group = group

    def is_clicked(self, pos):
        return self.pos[0] <= pos[0] <= self.pos[0] + self.width and self.pos[1] <= pos[1] <= self.pos[1] + self.height

    def draw(self):
        self.colors = [i / self.width for i in range(self.width)]
        self.hlsColor = self.group.hlsColor
        for i in range(self.width):
            self.hlsColor[self.type] = self.colors[i]
            self.rgbColor = to_8Bit_RGB(colorsys.hls_to_rgb(*self.hlsColor))
            pygame.draw.rect(screen, (self.rgbColor), pygame.Rect(self.pos[0] + i, self.pos[1], 1, self.height))
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(self.pos[0] + self.width * self.value, self.pos[1], 1, self.height))

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
    def __init__(self):
        self.pos = [100, 100]
        self.sliderWidth = 300
        self.sliderHeight = 20
        self.sliderSpacing = 10
        self.sliderPos = [[self.pos[0], self.pos[1] + i * (self.sliderHeight + self.sliderSpacing)] for i in range(3)]
        self.types = [0, 1, 2]
        self.sliders = [Slider(self.sliderPos[i], self.sliderWidth, self.sliderHeight, self.types[i], self) for i in range(len(self.sliderPos))]
        self.hlsColor = [0, 0, 0]
        self.rgbColor = colorsys.hsv_to_rgb(*self.hlsColor)
    
    def event_handle(self, event):
        for slider in self.sliders:
            slider.event_handle(event)
    
    def update_position(self, pos):
        for slider in self.sliders:
            slider.update_position(pos)
    
    def update_color(self):
        self.hlsColor = [slider.value for slider in self.sliders]
        self.rgbColor = colorsys.hls_to_rgb(*self.hlsColor)
    
    def draw(self):
        for slider in self.sliders:
            self.update_color()
            slider.draw()
        pygame.draw.rect(screen, to_8Bit_RGB(self.rgbColor), pygame.Rect(self.pos[0] + self.sliderWidth + self.sliderSpacing, self.pos[1], self.sliderHeight * 3 + self.sliderSpacing * 2, self.sliderHeight * 3 + self.sliderSpacing * 2))


WIDTH, HEIGHT = 1920, 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

running = True

hlsColor = [0, 0.5, 0.5]
rgbColor = colorsys.hls_to_rgb(*hlsColor)
step = 0.001

colorPick = ColorPicker()

def to_8Bit_RGB(color):
    return [255 * i for i in color]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        colorPick.event_handle(event)
    colorPick.update_position(pygame.mouse.get_pos())
    keys = pygame.key.get_pressed()
    if keys[pygame.K_q]:
        hlsColor[0] += step
        hlsColor[0] %= 1
    if keys[pygame.K_a]:
        hlsColor[0] -= step
        hlsColor[0] %= 1
    if keys[pygame.K_w]:
        hlsColor[1] += step
        hlsColor[1] = max(min(hlsColor[1], 1), 0)
    if keys[pygame.K_s]:
        hlsColor[1] -= step
        hlsColor[1] = max(min(hlsColor[1], 1), 0)
    if keys[pygame.K_e]:
        hlsColor[2] += step
        hlsColor[2] = max(min(hlsColor[2], 1), 0)
    if keys[pygame.K_d]:
        hlsColor[2] -= step
        hlsColor[2] = max(min(hlsColor[2], 1), 0)
    rgbColor = colorsys.hls_to_rgb(*hlsColor)
    screen.fill((to_8Bit_RGB(rgbColor)))
    colorPick.draw()
    # print(testSlider.value)
    pygame.display.flip()
pygame.quit()