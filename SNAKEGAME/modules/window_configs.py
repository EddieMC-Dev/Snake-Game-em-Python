import pygame
from pygame.locals import *


height_window = 480
width_window = 640
__clock = pygame.time.Clock()


def window_init():
    global height_window, width_window
    pygame.init()
    icon = pygame.image.load("images\\icon.ico") 
    pygame.display.set_icon(icon) # Não tá mostrando
    window = pygame.display.set_mode((width_window, height_window))
    pygame.display.set_caption("Snake Game")
    
    return window

def window_update(window:pygame.Surface):
    pygame.display.update()
    __clock.tick(30)
    window.fill((0, 0, 0))
    
def set_clock(fps:int):
    __clock.tick(fps)