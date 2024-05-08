import pygame 
import random
import time 
from pygame.locals import * 

screen_width = 900
screen_height = 800 


def change_background(image):
    image = pygame.image.load(image)
    bg = pygame.transform.scale(image, (screen_width, screen_height))
    screen.blit(bg, (0,0))



pygame.init()
pygame.display.set_caption("Tressure Hunt")
screen = pygame.display.set_mode([screen_width, screen_height])



