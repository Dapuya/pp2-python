import pygame
import random
import math

# frame
pygame.init()
screen = pygame.display.set_mode((800, 600))
background = pygame.image.load('background.png')
pygame.display.set_caption("First")
icon = pygame.image.load('galaxy.png')
pygame.display.set_icon(icon)

playerIcon = pygame.image.load('player.png')
# p - player
pX = 370
pY = 480
pX_change = 0

enemyIcon = pygame.image.load('alien.png')
# e = enemy
eX = random.randint(0, 736)
eY = random.randint(50, 150)
eX_change = 4
eY_change = 40

bulletIcon = pygame.image.load('bullet.png')
# b = bullet
bX = 0
bY = 480
bX_change = 0
bY_change = 40
b_state = 'ready'

score = 0

def player(x, y):
    screen.blit(playerIcon, (x, y))

def enemy(x, y):
    screen.blit(enemyIcon, (x, y))

def fire_bullet(x, y):
    global b_state
    b_state = 'fire'
    screen.blit(bulletIcon, (x+16, y+10))

def isCollision(eX, eY, bX, bY):
    distance = math.sqrt((math.pow(eX - bX, 2)) + (math.pow(eY - bY, 2)))
    if distance < 27:
        return True
    else:
        return False

run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pX_change = -5
            if event.key == pygame.K_RIGHT:
                pX_change = 5
            if event.key == pygame.K_SPACE:
                if b_state is 'ready':
                    bX = pX
                    fire_bullet(bX, bY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                pX_change = 0

    pX += pX_change
    if pX <= 0:
        pX = 0
    elif pX >= 736:
        pX = 736

    eX += eX_change
    if eX <= 0:
        eX_change = 4
        eY += eY_change
    elif eX >= 736:
        eX_change = -4
        eY += eY_change

    if bY <= 0:
        bY = 480
        b_state = 'ready'

    if b_state is 'fire':
        fire_bullet(bX, bY)
        bY -= bY_change

    collision = isCollision(eX, eY, bX, bY)
    if collision:
        bY = 480
        b_state = 'ready'
        score += 1
        print(score)
        eX = random.randint(0, 736)
        eY = random.randint(50, 150)

    player(pX, pY)
    enemy(eX, eY)
    pygame.display.update()
