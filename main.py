import pygame
import math
import random
import os

# Initialize pygame
pygame.init()
pygame.mixer.init()
# Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
# Sizes
screenwidth=1200
screenheight=600
# Video mode
gamewindow=pygame.display.set_mode((screenwidth,screenheight))
# Images and backgrounds
bg=pygame.image.load('2.jpg')
bg=pygame.transform.scale(bg,(screenwidth,screenheight)).convert_alpha()
bg1=pygame.image.load('1.png')
bg1=pygame.transform.scale(bg1,(screenwidth,screenheight)).convert_alpha()
admin=pygame.image.load('3.jpg')
admin=pygame.transform.scale(admin,(250,250)).convert_alpha()
food=pygame.image.load('4.png')
food=pygame.transform.scale(food,(35,45)).convert_alpha()
# Making display
pygame.display.set_caption("Snakes")
pygame.display.update()
clock=pygame.time.Clock()
font=pygame.font.SysFont(None,55)
# Screen text
def screentext(text,color,x,y):
    sctext=font.render(text,True,red)
    gamewindow.blit(sctext,[x,y])
# Making snake
def plot_snake(color,snk_list,gamewindow,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,black,[x,y,snake_size,snake_size])
# Initialising game
def welcome():
    exit_game=False
    while not exit_game:
        pygame.mixer.music.load('1.mp3')
        pygame.mixer.music.play(-1)
        gamewindow.fill((120,150,80))
        gamewindow.blit(bg1,(0,0))
        gamewindow.blit(admin,(40,0))
        screentext("Welcome to Snakes",black,400,150)
        screentext("Press Space bar to play",black,385,200)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                exit_game=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(30)
def gameloop():
    exit_game=False
    game_over=False
    snake_x=45
    snake_y=55
    snake_size=25
    fps=40
    velocity_x=0
    velocity_y=0
    init_velocity=8
    food_x=random.randint(20,int(screenwidth/2))
    food_y=random.randint(20,int(screenheight/2))
    score=0
    snk_list=[]
    snk_length=1
    if not os.path.exists("high1.txt"):
        with open("high1.txt","w") as f:
            f.write('0')
    with open("high1.txt") as f:
        high_score=f.read()
    while not exit_game:
        if game_over:
            with open('high1.txt','w') as f:
                f.write(str(high_score))
            gamewindow.blit(bg1,(0,0))
            screentext("Game Over! Press enter to continue ",black,250,150)
            screentext(f'Score: {str(score)}',red,250,200)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    exit_game=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_RIGHT:
                        velocity_x=init_velocity
                        velocity_y=0
                    if event.key==pygame.K_LEFT:
                        velocity_x=-init_velocity
                        velocity_y=0
                    if event.key==pygame.K_UP:
                        velocity_y=-init_velocity
                        velocity_x=0
                    if event.key==pygame.K_DOWN:
                        velocity_y=init_velocity
                        velocity_x=0
            snake_x+=velocity_x
            snake_y+=velocity_y
            if abs(snake_x-food_x)<14 and abs(snake_y-food_y)<14:
                pygame.mixer.Sound('kill.wav').play()
                score+=10
                if score>int(high_score):
                    high_score=score
                food_x = random.randint(20, int(screenwidth / 2))
                food_y = random.randint(20, int(screenheight / 2))
                snk_length+=5
            gamewindow.blit(bg,(0,0))
            screentext(f'Score: {str(score)}     High Score: {str(high_score)}',red,5,5)
            # pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
            gamewindow.blit(food,(food_x,food_y))
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
            if len(snk_list) > snk_length:
                del snk_list[0]
            if snake_x<0 or snake_x>screenwidth or snake_y<0 or snake_y>screenheight:
                pygame.mixer.music.load('2.mp3')
                pygame.mixer.music.play()
                game_over=True
            if head in snk_list[:-1]:
                pygame.mixer.music.load('2.mp3')
                pygame.mixer.music.play()
                game_over=True
            plot_snake(black,snk_list,gamewindow,snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    exit()
welcome()