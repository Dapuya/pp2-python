import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("First")

icon = pygame.image.load('f.png')

pygame.display.set_icon(icon)

playerIcon = pygame.image.load('rocket.png')
pX = 370
pY = 480

def player():
    screen.blit(playerIcon, (pX, pY))


run = True
while run:
    screen.fill((200, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    player()
    pygame.display.update()
