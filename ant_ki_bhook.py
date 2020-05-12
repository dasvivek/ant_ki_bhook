"""
About the game
Year: 2020
Name: Ant Ki Bhook (Hunger of an ant)
Version: 1
Player: Single Player
Description:
    The player tries to eat all the sugar cubes droping on the screen.
    With each sugar cube the ant consumes, the speed of the cubes droping
    on screen increases.
    If the ant touches any of the right or left boudary the game ends and 
    player can restart playing again.
    With each cube consumed the score increases +1.

Image Courtesy: Gluster logo as ant
Sound: Youtube free audio
Author: Vivek Das

"""

import pygame
import time
import random

pygame.init()

# Import sound
sound_1 = pygame.mixer.Sound("Carmelized.mp3")
# load sound in memory
pygame.mixer.music.load("Carmelized.mp3")

# game screen dimensions
screen_width = 800
screen_height = 600

# Define colors for using it in code
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
dark_red = (138,0,0)
green = (0,128,0)
dark_green = (0,200,0)
silver = (192,192,192)
ant_width = 200

# 
display_mygame = pygame.display.set_mode((screen_width,screen_height))

# Name the game window
# Doesn't work in Fedora yet
pygame.display.set_caption('test game')
clock = pygame.time.Clock()

# Load primary customized image for game
my_img = pygame.image.load('gluster-ant-1.png')
# Load drop image for game
game_icon = pygame.image.load('gluster-ant-3.png')

# Gmae icon for game window
# Doesn't reflect in Fedora yet
pygame.display.set_icon(game_icon)

# Score counter at top of screen with cordinates
def ate(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Sugar Cubes Ate: "+ str(count), True, green)
    display_mygame.blit(text, (0,0))


def support(supportx, supporty, supportw, supporth, color):
    pygame.draw.rect(display_mygame, color, [supportx, supporty, supportw, supporth])

# blit is used to reflect anything text on game screen.
def game(x,y):
    display_mygame.blit(my_img, (x,y))

# Add color to structure surface
def text_objects(style, font):
    text_surface = font.render(style, True, white)
    return text_surface, text_surface.get_rect()

# Enhance with font and position
def message_display(text):
    text_style = pygame.font.Font('freesansbold.ttf',50)
    text_area, text_shape = text_objects(text, text_style)
    text_shape.center = ((screen_width/2), (screen_height/2))
    display_mygame.blit(text_area,text_shape)

    pygame.display.update()

    time.sleep(2)

    game_loop()

"""
When the game ends it will reflect the total score in the center.
It will give option to Play Again or Quit the game.
"""
def game_crash(score):
    #message_display('RESTARTING . . .')
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(sound_1)

    text_style = pygame.font.SysFont('comicsansms',70)
    text_area, text_shape = text_objects("TOTAL SCORE = " + str(score), text_style)
    text_shape.center = ((screen_width/2), (screen_height/2))
    display_mygame.blit(text_area,text_shape)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("AGAIN", 150, 450, 100, 50, green, dark_green,game_loop)
        button("QUIT !", 550, 450, 100, 50, red, dark_red,quit_game)

        pygame.display.update()
        clock.tick(15)


# Creates button for the game eg. Start, Quit, replay with color cordinate
def button(button_msg, x, y, w, h, inactive_color, active_color, action=None):

    # Button creation

        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        if x + w > mouse_pos[0] > x and y + h > mouse_pos[1] > y:
            pygame.draw.rect(display_mygame, active_color, (x, y, w, h))
            if mouse_click[0] == 1 and action != None:
                action()
#                if action == "play":
#                    game_loop()
#                elif action == "quit":
#                    pygame.quit()
#                    quit()
        else:
            pygame.draw.rect(display_mygame, inactive_color, (x, y, w, h))

        green_box_txt = pygame.font.Font("freesansbold.ttf", 20)
        box_area, box_shape = text_objects(button_msg, green_box_txt)
        box_shape.center = ((x + (w/2)), (y + (h/2)))
        display_mygame.blit(box_area, box_shape)


# WHen you end the game the game window should exit.
def quit_game():
    pygame.quit()
    quit()


# Introduction window for game with Title and Interactive options
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display_mygame.fill(black)
        text_style = pygame.font.Font('freesansbold.ttf',80)
        text_area, text_shape = text_objects("ANT KI BHOOK", text_style)
        text_shape.center = ((screen_width/2), (screen_height/2))
        display_mygame.blit(text_area,text_shape)
        

        # Button creation

        button("GO !", 150, 450, 100, 50, green, dark_green,game_loop)
        button("QUIT !", 550, 450, 100, 50, red, dark_red,quit_game)


        pygame.display.update()
        clock.tick(15)
    
# Actual game logic
def game_loop():
    # Play the game music
    pygame.mixer.music.play(-1)

    # Positioning of the primary image
    x = (screen_width * 0.25)
    y = (screen_height * 0.8)

    # Key movement flexibility
    x_move = 0

    """
    Drop image specifications
    start_supportx = drop the image from random cordinates
    start_supporty = start droping from beyond the game window so that it gives time for player
    start_speed = speed with which images are dropped
    start_width = Adjust the drop image according to game window
    start_height = Adjust the drop image according to game window
    """
    start_supportx = random.randrange(0, screen_width)
    start_supporty = -600
    start_speed = 7
    start_width = 50
    start_height = 50

    # Score Counter
    ant_ate = 0

    crashed = False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
#                crashed = True
                pygame.quit()
                quit()

            # Movement of Left key, Right Key and other key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_move = -10
                if event.key == pygame.K_RIGHT:
                    x_move = 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_move = 0

        x += x_move

        display_mygame.fill(black)

        support(start_supportx, start_supporty, start_width, start_height, red)
        start_supporty +=  start_speed
        game(x,y)
        ate(ant_ate)

        if x > screen_width - ant_width or x < 0:
            #crashed = True
            game_crash(ant_ate)
        if start_supporty > screen_height:
            start_supporty = 0 - start_height
            start_supportx = random.randrange(0, screen_width)

        if y < start_supporty + start_height:
            if x > start_supportx and x < start_supportx + start_width or x + ant_width > start_supportx and x + ant_width < start_supportx + start_width:
                #game_crash()
                ant_ate += 1
                start_supporty = -600
                start_supportx = random.randrange(0, screen_width)
                start_speed += 1

                

        pygame.display.update()
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
