import pygame
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)+ "/.."))
from src.Settings import*
class Button( pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, image, button_algorithm): 
        super().__init__()

        self.x = x
        self.y = y
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(width,height))
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y
        self.pressed = False  
        button_algorithm.add(self) 
     
    def is_pressed(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos):
            if mouse_pressed[0] == 1 and self.pressed == False:
                self.pressed = True 
                return True 
        if not mouse_pressed[0]:
            self.pressed = False
            return False
