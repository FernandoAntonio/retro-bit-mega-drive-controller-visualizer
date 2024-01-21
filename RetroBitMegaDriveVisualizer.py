import os

# Needs to be set before importing pygame, or can also be set from shell
# while calling the script
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

import platform
import pygame
import sys

# Starting
pygame.init()
joysticks = []
held_buttons = []
clock = pygame.time.Clock()
clock.tick(60)
keep_playing = True
pressed = False
themes = ["overlay_grey", "overlay_subtle", "overlay_white"]
theme = themes[0]
root_dir = getattr(sys, "_MEIPASS", os.path.abspath(os.path.dirname(__file__)))
images_dir = os.path.join(root_dir, "images")

# Setting icon and title
icon = pygame.image.load(os.path.join(images_dir, "icon.png"))
pygame.display.set_icon(icon)
pygame.display.set_caption("Retro-Bit Mega Drive Controller")

# Setting up main window
if platform.system() == "Windows":
    import win32api
    import win32con
    import win32gui

    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(
        hwnd,
        win32con.GWL_EXSTYLE,
        win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED,
    )
    win32gui.SetLayeredWindowAttributes(
        hwnd, win32api.RGB(*(255, 0, 128)), 0, win32con.LWA_COLORKEY
    )

bg = pygame.image.load(os.path.join(images_dir, "background.png"))
main_display = pygame.display.set_mode(bg.get_size())
main_display.fill((255, 0, 128))
main_display.blit(bg, (0, 0))
pygame.display.flip()


def draw_pressed_buttons():
    main_display.blit(bg, (0, 0))
    for held_button in held_buttons:
        main_display.blit(
            pygame.image.load(
                os.path.join(images_dir, theme, held_button + ".png")
            ).convert_alpha(),
            (0, 0),
        )
    pygame.display.flip()


def button_down(name):
    held_buttons.append(name)
    draw_pressed_buttons()


def button_up(name):
    for button in held_buttons:
        if button == name:
            held_buttons.remove(name)
    draw_pressed_buttons()


def switch_theme(theme):
    if theme == themes[-1]:
        return themes[0]
    else:
        return themes[themes.index(theme) + 1]


while keep_playing:
    for event in pygame.event.get():
        # Check for connected joysticks
        if event.type == pygame.JOYDEVICEADDED:
            for i in range(0, pygame.joystick.get_count()):
                joysticks.append(pygame.joystick.Joystick(i))
                joysticks[-1].init()

        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            keep_playing = False

        if event.type == pygame.MOUSEBUTTONUP:
            theme = switch_theme(theme)

        elif platform.system() == "Darwin":
            if event.type == pygame.KEYUP and event.key == 27:
                pygame.display.quit()
                pygame.quit()
                keep_playing = False

            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and event.value < 0:
                    button_down("left")
                if event.axis == 0 and event.value > 0:
                    button_up("left")
                if event.axis == 0 and event.value > 0.5:
                    button_down("right")
                if event.axis == 0 and event.value < 0.5:
                    button_up("right")
                if event.axis == 1 and event.value < 0:
                    button_down("up")
                if event.axis == 1 and event.value > 0:
                    button_up("up")
                if event.axis == 1 and event.value > 0.5:
                    button_down("down")
                if event.axis == 1 and event.value < 0.5:
                    button_up("down")
                if event.axis == 5 and event.value > 0:
                    button_down("c")
                if event.axis == 5 and event.value < 0:
                    button_up("c")
                if event.axis == 4 and event.value > 0:
                    button_down("z")
                if event.axis == 4 and event.value < 0:
                    button_up("z")

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    button_down("a")
                if event.button == 1:
                    button_down("b")
                if event.button == 2:
                    button_down("x")
                if event.button == 3:
                    button_down("y")
                if event.button == 4:
                    button_down("mode")
                if event.button == 6:
                    button_down("start")
                if event.button == 9:
                    button_down("l")
                if event.button == 10:
                    button_down("r")

            if event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    button_up("a")
                if event.button == 1:
                    button_up("b")
                if event.button == 2:
                    button_up("x")
                if event.button == 3:
                    button_up("y")
                if event.button == 4:
                    button_up("mode")
                if event.button == 6:
                    button_up("start")
                if event.button == 9:
                    button_up("l")
                if event.button == 10:
                    button_up("r")

        if platform.system() == "Windows":
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 0 and event.value < 0.5 and event.value > -0.5:
                    button_up("left")
                    button_up("right")
                if event.axis == 0 and event.value < 0:
                    button_down("left")
                if event.axis == 0 and event.value > 0:
                    button_down("right")
                if event.axis == 4 and event.value < 0.5 and event.value > -0.5:
                    button_up("up")
                    button_up("down")
                if event.axis == 4 and event.value < 0:
                    button_down("up")
                if event.axis == 4 and event.value > 0:
                    button_down("down")

            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:
                    button_down("x")
                if event.button == 1:
                    button_down("a")
                if event.button == 2:
                    button_down("b")
                if event.button == 3:
                    button_down("y")
                if event.button == 4:
                    button_down("c")
                if event.button == 5:
                    button_down("z")
                if event.button == 6:
                    button_down("l")
                if event.button == 7:
                    button_down("r")
                if event.button == 8:
                    button_down("mode")
                if event.button == 9:
                    button_down("start")

            if event.type == pygame.JOYBUTTONUP:
                if event.button == 0:
                    button_up("x")
                if event.button == 1:
                    button_up("a")
                if event.button == 2:
                    button_up("b")
                if event.button == 3:
                    button_up("y")
                if event.button == 4:
                    button_up("c")
                if event.button == 5:
                    button_up("z")
                if event.button == 6:
                    button_up("l")
                if event.button == 7:
                    button_up("r")
                if event.button == 8:
                    button_up("mode")
                if event.button == 9:
                    button_up("start")
