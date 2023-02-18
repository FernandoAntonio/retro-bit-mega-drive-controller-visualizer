import os

#Needs to be set before importing pygame, or can also be set from shell
#while calling the script
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

import pygame

#Starting
pygame.init()
joysticks = []
held_buttons = []
clock = pygame.time.Clock()
clock.tick(60)
keep_playing = True
pressed = False

#Setting icon and title
icon = pygame.image.load(os.getcwd() + "\\images\\icon.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Retro-Bit Mega Drive Controller")

#Setting up main window
screen = pygame.display.set_mode((800, 600))
bg = pygame.image.load(os.getcwd() + "\\images\\background.png").convert_alpha()
main_display = pygame.display.set_mode(bg.get_size())
main_display.blit(bg, (0,0))
pygame.display.flip()
        
#For all the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
    joysticks[-1].init()
 
def draw_pressed_buttons():
    main_display.blit(bg, (0,0))
    for held_button in held_buttons:
        main_display.blit(pygame.image.load(os.getcwd() + "\\images\\"+held_button+".png").convert_alpha(), (0,0))
    pygame.display.flip()
    
def button_down(name):
    held_buttons.append(name)
    draw_pressed_buttons()
    
def button_up(name):
    for button in held_buttons:
        if button == name:
            held_buttons.remove(name)
    draw_pressed_buttons()

while keep_playing:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            done = True
            keep_playing = False
                
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis == 0 and event.value < 0.5 and event.value > -0.5:
                button_up("left")
                button_up("right")
            elif event.axis == 0 and event.value < 0:
                button_down("left")
            elif event.axis == 0 and event.value > 0:
                button_down("right")
            elif event.axis == 4 and event.value < 0.5 and event.value > -0.5:
                button_up("up")
                button_up("down")
            elif event.axis == 4 and event.value < 0:
                button_down("up")
            elif event.axis == 4 and event.value > 0:
                button_down("down")
        
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                button_down("x")
            elif event.button == 1:
                button_down("a")
            elif event.button == 2:
                button_down("b")    
            elif event.button == 3:
                button_down("y")
            elif event.button == 4:
                button_down("c")
            elif event.button == 5:
                button_down("z")
            elif event.button == 6:
                button_down("l")
            elif event.button == 7:
                button_down("r")
            elif event.button == 8:
                button_down("mode")
            elif event.button == 9:
                button_down("start")
                
        elif event.type == pygame.JOYBUTTONUP:
            if event.button == 0:
                button_up("x")
            elif event.button == 1:
                button_up("a")
            elif event.button == 2:
                button_up("b")    
            elif event.button == 3:
                button_up("y")
            elif event.button == 4:
                button_up("c")
            elif event.button == 5:
                button_up("z")
            elif event.button == 6:
                button_up("l")
            elif event.button == 7:
                button_up("r")
            elif event.button == 8:
                button_up("mode")
            elif event.button == 9:
                button_up("start")
