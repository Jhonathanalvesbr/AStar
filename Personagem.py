import pygame
import time


class Personagem(pygame.sprite.Sprite):
    def sprite(self, tamanhoTela, sprite):
        self.tamanhoTela = tamanhoTela
        self.sprites = sprite
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = 100,100
        self.seguir = False
        self.mover = 0 
        self.movimento = []
        self.velocidade = 0.5
        self.x = 0
        self.y = 0
        self.ini = time.time()
        self.fim = time.time()
        self.tamanho = 0
        self.caminhar = False
        self.desX = None
        self.desY = None
        
        for i in range(len(self.sprites)):
            self.image = self.sprites[i]
            self.image = pygame.transform.rotate(self.image,200)
            
    def update(self):
        self.atual = self.atual + 0.005
        if self.atual >= len(self.sprites):
            self.atual = 0
        
        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image,(int(self.tamanhoTela/25)*3,int(self.tamanhoTela/25)*3))
        self.image = pygame.transform.rotate(self.image,self.angle)
        
    def angulo(self,angle):
        self.angle = angle
        
    def angulo(self,angle):
        self.angle = angle

    def cima(self):
        self.rect.move_ip(0,-100)

    def baixo(self):
        self.rect.move_ip(0,100)

    def esquerda(self):
        self.rect.move_ip(-100,0)

    def direita(self):
        self.rect.move_ip(100,0)