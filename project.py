import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("First")

icon = pygame.image.load('f.png')

pygame.display.set_icon(icon)

playerIcon = pygame.image.load('rocket.png')
pX = 370
pY = 480

def player(x,y):
    screen.blit(playerIcon, (x, y))


run = True
while run:
    screen.fill((0, 0, 0))
    pX += 0.1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player(pX, pY)
    pygame.display.update()
