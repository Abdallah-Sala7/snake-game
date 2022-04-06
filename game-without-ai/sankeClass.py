import pygame
import random
from collections import namedtuple

# pygame.init()
font = pygame.font.SysFont('comicsans', 25)

Point = namedtuple('Point', 'x, y')
aplle = pygame.image.load("image-and-audio/aplle2.png")
# screen = pygame.display.set_mode((640,480))

HEAD_SIZE = 20

class Snake():
    def __init__(self, screen,direction, screenWidth, screenHeight):
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.screen = screen
        self.direction = direction
        self.head = Point(screenWidth/2, screenHeight/2)
        self.snake = [self.head, Point(self.head.x-HEAD_SIZE, self.head.y),Point(self.head.x-(2*HEAD_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self.snakeSpeed = 5
        self.place_of_food()
        
    def place_of_food(self):
        x = random.randint(0, (self.screenWidth-HEAD_SIZE )//HEAD_SIZE )*HEAD_SIZE 
        y = random.randint(0, (self.screenHeight-HEAD_SIZE )//HEAD_SIZE )*HEAD_SIZE

        self.food = Point(x, y)
        if self.food in self.snake:
            self.place_of_food()


    def step(self):

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = 'L'
                elif event.key == pygame.K_RIGHT:
                    self.direction = 'R'
                elif event.key == pygame.K_UP:
                    self.direction = 'U'
                elif event.key == pygame.K_DOWN:
                    self.direction = 'D'

        self.move(self.direction)
        self.snake.insert(0, self.head)

        end_game = False
        if self.is_hit():
            end_game = True
            return end_game, self.score, self.snakeSpeed
            
        if self.head == self.food:
            self.score += 1
            self.snakeSpeed += 0.1
            self.place_of_food()
        else:
            self.snake.pop()
        self.draw()
        return end_game, self.score, self.snakeSpeed
    
    def is_hit(self):
        if self.head.x > self.screenWidth - HEAD_SIZE or self.head.x < 0 or self.head.y > self.screenHeight - HEAD_SIZE or self.head.y < 0:
            return True
        if self.head in self.snake[1:]:
            return True
        return False
        
    def draw(self):
        for rect in self.snake:
            pygame.draw.rect(self.screen, (80,100,200),(rect.x, rect.y, HEAD_SIZE, HEAD_SIZE))
            pygame.draw.rect(self.screen, (80,10,100),(rect.x+4, rect.y+4, HEAD_SIZE - 8,  HEAD_SIZE - 8),border_radius=50)
            
        pygame.draw.rect(self.screen, (0,255,0),(self.food.x + 10, self.food.y -5, 5, HEAD_SIZE),border_radius=5)
        pygame.draw.rect(self.screen, (255,0,0),(self.food.x, self.food.y, HEAD_SIZE, HEAD_SIZE),border_radius=5)
        # self.screen.blit(aplle,(self.food.x, self.food.y))
        
        text = font.render("Score: " + str(self.score), True, (255,255,255))
        self.screen.blit(text, [0, 0])
        pygame.display.flip()
        
    def move(self,direction = 'R'):
        x = self.head.x
        y = self.head.y
        if direction == 'R':
            x += HEAD_SIZE
        elif direction == 'L':
            x -= HEAD_SIZE
        elif direction == 'D':
            y += HEAD_SIZE
        elif direction == 'U':
            y -= HEAD_SIZE
        self.head = Point(x, y)
        # print(direction)
