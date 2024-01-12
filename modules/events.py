import pygame
from pygame.locals import *
#============================
from sys import exit
#============================
from modules.window_configs import height_window, width_window

def check_events(snake_position:list[float], directions:list[int], gameState:bool): 
    restartGame = [False]
    if gameState:
        for event in pygame.event.get():
            check_game_is_over(event)   
            eventSucess = check_keydown(event, directions, restartGame)
            if restartGame[0] or eventSucess:
                break
        check_window_exit(snake_position, directions)
    else:
        for event in pygame.event.get():
            check_game_is_over(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                restartGame[0] = True
    return restartGame[0]
        
def check_game_is_over(event:pygame.event.Event):
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()

def check_keydown(event:pygame.event.Event, 
                  directions: list[int],
                  restart_game: list[bool]) -> bool:
    if event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_UP):
            if directions[1] != 1: 
                directions[1] = -1
                directions[0] = 0
                return True
        elif (event.key == pygame.K_DOWN):
            if directions[1] != -1:
                directions[1] = 1
                directions[0] = 0
                return True
        elif (event.key == pygame.K_RIGHT):
            if directions[0] != -1:
                directions[0] = 1
                directions[1] = 0
                return True
        elif (event.key == pygame.K_LEFT):
            if directions[0] != 1:
                directions[0] = -1
                directions[1] = 0 
                return True
        elif (event.key == pygame.K_r):
            restart_game[0] = True
        return False
                
def check_window_exit(snake_position:list[float], directions:list[int]):
    if snake_position[0] < 0:
        snake_position[0] = width_window 
        directions[0] = -1
        directions[1] = 0
    if snake_position[0] > width_window:
        snake_position[0] = -20
        directions[0] = 1
        directions[1] = 0
    if snake_position[1] > height_window:
        snake_position[1] = 0
        directions[1] = 1
        directions[0] = 0
    if snake_position[1] < 0:
        snake_position[1] = height_window + 10
        directions[1] = -1 
        directions[0] = 0 