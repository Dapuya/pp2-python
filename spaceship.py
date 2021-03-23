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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            print("keystrock is pressed")
            if event.key == pygame.K_LEFT:
                print("left")
            if event.key == pygame.K_RIGHT:
                print("right")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("keystroke is released")

    player(pX, pY)
    pygame.display.update()
