import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('Game IA')
janela = pygame.display.set_mode((800,800))

todas_as_sprites = pygame.sprite.Group()