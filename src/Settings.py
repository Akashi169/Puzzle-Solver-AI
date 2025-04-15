import pygame 
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))

screen_width = 1000
screen_height = 750
tile_size = 100

button_algorithm = pygame.sprite.Group()

img_tile = pygame.image.load(r"assets\images\title.png")
img_tile = pygame.transform.scale(img_tile,(screen_width, tile_size))


img_start = pygame.image.load(r"assets\images\start.png")
img_start = pygame.transform.scale(img_start, (tile_size*0.8, tile_size*0.2))

img_target = pygame.image.load(r"assets\images\target.png")
img_target = pygame.transform.scale(img_target, (tile_size*1.1, tile_size*0.2))