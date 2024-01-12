import pygame
from pygame.locals import *
#===================================================
from modules.window_configs import width_window, height_window

col_snake = (0, 255, 0)
height_snake = 20
width_snake = 20
x_snake = width_window/2 - width_snake/2
y_snake = height_window/2 - height_snake/2
body_snake = [[x_snake, y_snake]]
snake_length = 5
directionX = 1
directionY = 0

def draw_body_snake(body_snake:list[list[float]],
                    window:pygame.Surface,
                    col_snake:tuple[int],
                    width_snake:float, height_snake:float):
    global height_window
    for position in body_snake:
        if (position[1] > height_window):
            rect = pygame.draw.rect(window, col_snake,
                            (position[0], 0, 
                            width_snake, height_snake)) 
        else:
            rect = pygame.draw.rect(window, col_snake,
                            (position[0], position[1], 
                            width_snake, height_snake)) 
    return rect

def control_snake_growth(body_snake:list[list[float]],
                         snake_length:int):
    if snake_length < len(body_snake):
        del body_snake[0]     
        
def control_snake_move(snake_positions:list[float], directions:list[int], body_snake:list[list[float]]):
    if directions[1]:
        snake_positions[1] += 20 * directions[1]
    elif directions[0]:
        snake_positions[0] += 20 * directions[0]
    if [snake_positions[0], snake_positions[1]] in body_snake[-1]:
        body_snake.pop()
    
    
def check_game_over(body_snake:list[list[float]]):
    if body_snake.count(body_snake[-1]) > 1:
        return True
    return False