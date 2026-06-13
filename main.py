import pygame
from colorPicker import ColorPicker

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1920, 1080

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

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
    screen.fill((255, 255, 255))
    colorPick.draw()
    pygame.display.flip()
pygame.quit()