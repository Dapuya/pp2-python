import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("First")

icon = pygame.image.load('galaxy.png')

pygame.display.set_icon(icon)

playerIcon = pygame.image.load('rocket.png')
pX = 370
pY = 480
pX_change = 0
def player(x,y):
    screen.blit(playerIcon, (x, y))


run = True
while run:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pX_change = -0.3
            if event.key == pygame.K_RIGHT:
                pX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pX_change = 0
    pX += pX_change
    if pX <= 0:
        pX = 0
    elif pX >= 736:
        pX = 736
    player(pX, pY)
    pygame.display.update()
