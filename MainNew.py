# First I have to import PyGame lybrary. I first had to install it via terminal because it wasn't working with the Visual Studio directly 
import pygame
from sys import exit # To fix the error -> pygame.error video system not initialized
print(pygame.ver)
import random

# That is the command which basically "starts" the pygame 
pygame.init()
# Setting dimensions for the game
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('PongGame') #Set the caption of the window e.g. name the game in the system
clock = pygame.time.Clock()

font = pygame.font.SysFont("arial", 30)

#Rectangles
#pygame.Rect(x,y,width,height)
ball = pygame.Rect(screen_width/2-10, screen_height/2-10, 20, 20)
player1 = pygame.Rect(screen_width-100, screen_height/2-50, 10, 100)
player2 = pygame.Rect(100, screen_height/2-50, 10, 100)

player1_score = 0 
player2_score = 0


ball_x_speed = 2.75
ball_y_speed = 2.75

# full list of colors from the pygame -> https://www.pygame.org/docs/ref/color_list.html
background_color = pygame.Color("black")


# I made a loop to make the game running and all the visual content of the game should be in this loop
while True:
    key_pressed = pygame.key.get_pressed() # I created a variable called 
# Creating the "movement" logic of both players using the key pressed to shift the position of rectangles accordingly
    if key_pressed[pygame.K_0]:
       if player1.top > 0: # I have to set up a limit for players like this so that the rectangle doesn't go off the screen
           player1.top -=3
    if key_pressed[pygame.K_9]:
       if player1.bottom < screen_height:
          player1.bottom +=3
    if key_pressed[pygame.K_2]:
       if player2.top > 0:
          player2.top -=3
    if key_pressed[pygame.K_1]:
       if player2.bottom < screen_height:
          player2.bottom +=3

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # this method enables me to close the window with the game
          pygame.quit()
          exit() # exits the loop basically at the same time when the window is closed
   
    if ball.y >= screen_height:
       ball_y_speed -= 2.75
    if ball.y <= 0:
       ball_y_speed = 2.75
    if ball.x <= 0:
       player1_score += 1
       ball.center = (screen_width/2, screen_height/2)
       ball_x_speed = random.choice([2.75,-2.75]) #why do we need randomisation here? Basically if not introduced, ball is always going to the right direction so one of the players gets an advantage, so randomisation of direction makes game more balanced
       ball_y_speed = random.choice([2.75,-2.75])
    if ball.x >= screen_width:
       player2_score += 1
       ball.center = (screen_width/2, screen_height/2)
       ball_x_speed = random.choice([2.75,-2.75])
       ball_y_speed = random.choice([2.75,-2.75])
       # problem - ball is too slow after it gets back to the center 
       # problem solved - in random.choice([]) the values should ideally match the speed of the ball, so in my case i was using -1, 1 at first so after ball was "respowned" to the center it became too slow because of the low value
    if ball.colliderect(player1) or ball.colliderect(player2):
       ball_x_speed *= -1.05
       # problem -> -2.75 reverse speed is way too high, try make it 50% less . upd -> 1.32 is also too much, try -1 now. upd: -1 is way better but -1.05 might be more fun as it should accelerate the speed a little. upd: -1.05 mihght add a bit of smoothness as well so I decide to keep it 
    
       
    player1_score_text = font.render(str(player1_score), True, "azure")
    player2_score_text = font.render(str(player2_score), True, "azure")

    ball.x += ball_x_speed 
    ball.y += ball_y_speed 
    #pygame.display.update() # Updates the game all the time
    screen.fill("black") # this line is needed so that the positions of the players get "visually" updated by filling the screen again and again while the game is running 
    pygame.draw.rect(screen, "white", player1, 5)
    pygame.draw.rect(screen, "white", player2, 5)
    pygame.draw.circle(screen, "yellow", ball.center, 10) #important to specify the radius here if we making a circle
    pygame.draw.aaline(screen, 'azure', (screen_width/2, 0), (screen_width/2, screen_height))
    
    screen.blit(player1_score_text, (screen_width/2+50, 50))
    screen.blit(player2_score_text, (screen_width/2-50, 50))

    pygame.display.flip()
    clock.tick(120) # updating the window at 120 fps (x)=fps of the game. by adjusting this parameter we can regulate the update speed (frames)
