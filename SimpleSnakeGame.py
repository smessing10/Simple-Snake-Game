import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
snake_green = (0,200,0)
blue = (0,0,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Simple Snake Game')

clock = pygame.time.Clock()

AppleThickness = 20
block_size = 20
FPS = 15

UP = 'up'
DOWN = 'down'      
LEFT = 'left'
RIGHT = 'right'

direction = "right"

smallfont = pygame.font.SysFont("Times New Roman", 25)
medfont = pygame.font.SysFont("Times New Roman", 50)
largefont = pygame.font.SysFont("Times New Roman", 75)

def game_intro():
        intro = True
        while intro:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        Intro = False 
                        gameLoop()  
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit(q)    
                
            gameDisplay.fill(black)
            message_to_screen("Welcome to the simple snake game!",
                              green,
                              -100,
                              "medium")
            message_to_screen("The objective of the game is to eat red apples.",
                              red, 
                              -30)
            message_to_screen("The more apples you eat the longer you get.",
                              white, 
                              -10)
            message_to_screen("If you run into yourself, or the edges, you die.",
                              white, 
                              10)
            message_to_screen("Use the arrow keys or the WASD keys to control the snake",
                              white, 
                              70)
            message_to_screen('Press "C" to play, "Space" to pause, or "Q" to quit',
                              white, 
                              100,
                              "small")
            
            pygame.display.update()
            clock.tick(4)

def pause():
    
    paused = True
    
    message_to_screen("Paused",
                      white,
                      -50,
                      'large')
    message_to_screen('"',
                      white,
                      30,
                      'large')
    message_to_screen('Press the space bar to resume',
                      white,
                      50,)
    
    
    pygame.display.update()
    
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
    
        #gameDisplay.convert_alpha()
        #gameDisplay.fill(black)
    
        clock.tick(4)

def score(score):
    text = smallfont.render('Score: ' + str(score), True, white)
    gameDisplay.blit(text, [0,0])

def randAppleGen():
    randAppleX = round(random.randrange(0,display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-AppleThickness))#/10.0)*10.0

    return randAppleX, randAppleY

def snake(block_size, snakelist):
        
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, snake_green, [XnY[0],XnY[1],block_size,block_size]) 

def text_objects(text,color, size):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = medfont.render(text, True, color)
    elif size == "large":
        textSurface = largefont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def message_to_screen(msg, color, y_displace = 0, size = "small"):
    
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2),(display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)    
    
def gameLoop():
    global direction
    
    direction = "right"
    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0
    
    snakeList = []
    snakeLength = 3
    
    randAppleX, randAppleY = randAppleGen() 
    
    while not gameExit:
        
        while gameOver:
            gameDisplay.fill(black)
            message_to_screen('GAME OVER',
                              red,
                              -50,
                              size = "large")
            message_to_screen('Your final score is: ' + str((snakeLength-3)*10),
                              green,
                              10,
                              size = "small")
            message_to_screen('Press "C" to play again or "Q" to quit',
                               white,
                                50,
                                size = "medium")
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()    
        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                gameExit = True    
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != RIGHT:
                    direction = "left"
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != LEFT:
                    direction = "right"
                    lead_x_change = block_size
                    lead_y_change = 0
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != DOWN:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != UP:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                    
                elif event.key == pygame.K_SPACE:
                    pause()
                  
        if lead_x + block_size >= display_width or lead_x <= 0 or lead_y >= display_height or lead_y + block_size <= 0:
            gameOver = True      
        
                    
    
        lead_x += lead_x_change  
        lead_y += lead_y_change 
        
        gameDisplay.fill(black)
      
        
        
        
        pygame.draw.rect(gameDisplay,red,[randAppleX,randAppleY,AppleThickness,AppleThickness])
        
    
        
        
      
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        
        if len(snakeList)>snakeLength:
            del snakeList[0]
            
        for eachSegment in snakeList[:-1]: 
            if eachSegment == snakeHead:
                gameOver = True
        
        snake(block_size, snakeList)
        
        score((snakeLength-3)*10)
        
        pygame.display.update() 



        if lead_x >= randAppleX and lead_x <= randAppleX + AppleThickness or lead_x + block_size >= randAppleX and lead_x + block_size <= randAppleX + AppleThickness:
            if lead_y >= randAppleY and lead_y <= randAppleY + AppleThickness or lead_y + block_size >= randAppleY and lead_y + block_size <= randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen() 
                snakeLength += 1
                
                
        clock.tick(FPS)
        
        
    pygame.quit()
    quit()

game_intro()
gameLoop()
