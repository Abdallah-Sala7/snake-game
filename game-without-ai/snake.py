import pygame
pygame.init()
from sankeClass import *
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("AI Snake Game")
clock = pygame.time.Clock()

screenWidth=640
screenHeight=480
direction = 'R'
backgroun = pygame.image.load("image-and-audio/snakeBg.jpg")
mySnake = Snake(screen,direction, screenWidth, screenHeight)



while True:
    # screen.fill((0, 50, 100))
    screen.blit(backgroun,(0,0))

    game, score, speed = mySnake.step()
    if game == True:
        break
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         direction = 'L'
        #     elif event.key == pygame.K_RIGHT:
        #         direction = 'R'
        #     elif event.key == pygame.K_UP:
        #         direction = 'U'
        #     elif event.key == pygame.K_DOWN:
        #         direction = 'D'
    clock.tick(speed)
pygame.display.update() 
print('Your Score => ', score)