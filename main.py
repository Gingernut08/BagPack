import colorsys, pygame

pygame.init()


class ColorPicker:
    def __init__(self):
        pass





WIDTH, HEIGHT = 1920, 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

running = True

hlsColor = [0, 0, 0]
rgbColor = colorsys.hls_to_rgb(*hlsColor)
step = 0.001

def to_8Bit_RGB(color):
    return [255 * i for i in color]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
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
    pygame.display.flip()
pygame.quit()