from random import randint
#==============================================
import pygame
from pygame.locals import *
#==============================================
from modules.window_configs import height_window, width_window

pygame.init()
height_apple = 40
width_apple = 40
x_apple = randint(width_apple, width_window-width_apple)
y_apple = randint(height_apple, height_window-height_apple)
col_apple = (255, 0, 0)

font_score = pygame.font.Font("fonts\\Pixeboy.ttf", 72)
score = 0

apple_collision_song = pygame.mixer.Sound("audios\\moeda.wav")


def check_collide_snake_in_apple(snake:pygame.Rect, apple:pygame.Rect, 
                                 length_s:list[int], window:pygame.Surface):
    global x_apple, y_apple, score, font_score, width_window, height_apple
    if snake.colliderect(apple):
        x_apple = randint(width_apple, width_window-width_apple)
        y_apple = randint(height_apple, height_window-height_apple)
        length_s[0] += 1
        score += 1
        apple_collision_song.set_volume(1)
        apple_collision_song.play()
    
    score_view = font_score.render(f"Score: {score}", True, (255, 255, 255,))
    window.blit(score_view, (5, 5))

def draw_apple(window:pygame.Surface):
    global x_apple, y_apple, col_apple, height_apple, width_apple
    rect = pygame.draw.rect(window, col_apple, 
                     (x_apple, y_apple, width_apple, height_apple))
    return rect

def restart_apple():
    global x_apple, y_apple, score
    x_apple = randint(width_apple, width_window-width_apple)
    y_apple = randint(height_apple, height_window-height_apple)
    score = 0
    
def draw_score(screen_game_over:pygame.Surface):
    font_game_over = pygame.font.Font("fonts\\Pixeboy.ttf", 130)
    score_total = font_game_over.render(f"      {score}", True, (255, 255, 255))
    screen_game_over.blit(score_total, (270, 208))