import pygame

pygame.init()

screen = pygame.display.set_mode((700, 500))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

