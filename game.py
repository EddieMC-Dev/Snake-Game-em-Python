# AVISO: Esse código garante que o executável do Pyinstaller
# possa carregar recursos em um diretório temporário sem que
# tenha problemas com PATH de arquivos no pygame.
import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
        os.chdir(sys._MEIPASS)
#====================================
import pygame
#====================================
from modules.window_configs import *
from modules.events import *
from modules.snake import *
from modules.apple import *

window = window_init()
pos_snake = [x_snake, y_snake]
directions = [directionX, directionY]
length_s = [snake_length] 
game_on = True;
game_over_image = pygame.image.load("images\\gameover.png")

pygame.mixer.music.load("audios\\fundo.wav")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.6)

while True:
    restartGame = check_events(pos_snake, directions, game_on)
    
    if restartGame:
        pos_snake = [x_snake, y_snake]
        directions = [directionX, directionY]
        length_s = [snake_length] 
        body_snake = [[x_snake, y_snake]]
        restart_apple()
        game_on = True 
        game_over_image = pygame.image.load("images\\gameover.png")
    
    if game_on:
        control_snake_move(pos_snake, directions, body_snake)
        body_snake.append([pos_snake[0], pos_snake[1]])
        rect_s = draw_body_snake(body_snake, window, 
                                col_snake, width_snake, height_snake)
        rect_a = draw_apple(window)
        check_collide_snake_in_apple(rect_s, rect_a, length_s, window)
        control_snake_growth(body_snake, length_s[0])     
        game_on = not(check_game_over(body_snake))
        window_update(window)

    if not game_on: 
        window.blit(game_over_image, game_over_image.get_rect())
        draw_score(game_over_image)
        pygame.display.update()
        set_clock(30)
         