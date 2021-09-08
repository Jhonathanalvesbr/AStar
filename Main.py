import Personagem
import AStar
import pygame
import time
import pygame
from pygame.locals import *
from sys import exit
import time

tamanhoTela = 800
tamanho = 8
caminho = []
movimento = []
busca = AStar.Astar(tamanho)
ini = fim = time.time()
for y in range(tamanho):
    linha = []
    for x in range(tamanho):
        linha.append(0)
    caminho.append(linha)

spriteIninimigo = []
spritePacMan = []
spriteComida = []
inimigo = []
comida = []
spritePacMan.append(pygame.image.load('1.png'))
spritePacMan.append(pygame.image.load('2.png'))
spritePacMan.append(pygame.image.load('3.png'))
spriteIninimigo.append(pygame.image.load('i1.png'))
spriteComida.append(pygame.image.load('c1.png'))
pacMan = Personagem.Personagem()
pacMan.sprite(tamanhoTela,spritePacMan)

todas_as_sprites = pygame.sprite.Group()
todas_as_sprites.add(pacMan)
fantasma = []

pygame.init()
janela = pygame.display.set_mode((tamanhoTela,tamanhoTela))

def caminhoVazio():
    for x in range(len(caminho)):
        for y in range(len(caminho)):
            if(caminho[x][y] == 3):
                return 1
    return -1
    
while True:
    fim = time.time()
    if(fim-ini  > 0.5 and len(movimento) > 0):
        if(pacMan.rect.x < movimento[0][0]*100):
            pacMan.angle = 0
        if(pacMan.rect.x > movimento[0][0]*100):
            pacMan.angle = 180
        if(pacMan.rect.y > movimento[0][1]*100):
            pacMan.angle = -90
        if(pacMan.rect.y > movimento[0][1]*100):
            pacMan.angle = 90
        
        ini = time.time()
        pacMan.rect.x = movimento[0][0]*100
        pacMan.rect.y =  movimento[0][1]*100
        p = []
        p.append(pacMan.rect.x)
        p.append(pacMan.rect.y)
        
        
        for i in comida:
            if(i.rect.collidepoint(p)):
                if(isinstance(i, Personagem.Personagem)):
                    todas_as_sprites.remove(i)
                    caminho[movimento[0][0]][movimento[0][1]] = 0
                    
        movimento.pop(0)
        if(len(movimento) == 0):
            if(caminhoVazio() == 1):
                xTemp = iniY = int(pacMan.rect.x/100)
                yTemp = iniX = int(pacMan.rect.y/100)
                desX = int(xTemp)
                desY = int(yTemp)
                caminho[iniX][iniY] = 1
                if(caminhoVazio() == 1):
                    movimento = busca.busca(caminho)
                    caminho[yTemp][xTemp] = 0
                    
    
    for event in pygame.event.get():
        teclado = pygame.key.get_pressed()
        if(teclado[pygame.K_LEFT]):
            if(pacMan.rect.x > 0):
                if(caminho[int(pacMan.rect.y/100)][int(pacMan.rect.x/100)-1] != -1):
                    pacMan.esquerda()
                    p = []
                    p.append(pacMan.rect.x)
                    p.append(pacMan.rect.y)
                    pacMan.angulo(180)
                    for i in comida:
                        if(i.rect.collidepoint(p)):
                            if(isinstance(i, Personagem.Personagem)):
                                todas_as_sprites.remove(i)
                                caminho[int(p[1]/100)][int(p[0]/100)] = 0
        if(teclado[pygame.K_RIGHT]):
            if(pacMan.rect.x < 700):
                if(caminho[int(pacMan.rect.y/100)][int(pacMan.rect.x/100)+1] != -1):
                    pacMan.direita()
                    p = []
                    p.append(pacMan.rect.x)
                    p.append(pacMan.rect.y)
                    pacMan.angulo(0)
                    for i in comida:
                        if(i.rect.collidepoint(p)):
                            if(isinstance(i, Personagem.Personagem)):
                                todas_as_sprites.remove(i)
                                caminho[int(p[1]/100)][int(p[0]/100)] = 0
        if(teclado[pygame.K_UP]):
            if(pacMan.rect.y > 0):
                if(caminho[int(pacMan.rect.y/100)-1][int(pacMan.rect.x/100)] != -1):
                    pacMan.cima()
                    p = []
                    p.append(pacMan.rect.x)
                    p.append(pacMan.rect.y)
                    pacMan.angulo(90)
                    for i in comida:
                        if(i.rect.collidepoint(p)):
                            if(isinstance(i, Personagem.Personagem)):
                                todas_as_sprites.remove(i)
                                caminho[int(p[1]/100)][int(p[0]/100)] = 0
        if(teclado[pygame.K_DOWN]):
            if(pacMan.rect.y < 700):
                if(caminho[int(pacMan.rect.y/100)+1][int(pacMan.rect.x/100)] != -1):
                    pacMan.baixo()
                    p = []
                    p.append(pacMan.rect.x)
                    p.append(pacMan.rect.y)
                    pacMan.angulo(-90)
                    for i in comida:
                        if(i.rect.collidepoint(p)):
                            if(isinstance(i, Personagem.Personagem)):
                                todas_as_sprites.remove(i)
                                caminho[int(p[1]/100)][int(p[0]/100)] = 0
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if(teclado[pygame.K_F5]):
            if(caminhoVazio() == 1):
                time.sleep(0.05)
                xTemp = iniY = int(pacMan.rect.x/100)
                yTemp = iniX = int(pacMan.rect.y/100)
                desX = int(xTemp)
                desY = int(yTemp)
                caminho[desY][desX] = 1
                for x in range(len(caminho)):
                    for y in range(len(caminho)):
                        if(caminho[x][y] == 3):
                            desX = x
                            desY = y
                            break

                movimento = busca.busca(caminho)
                caminho[yTemp][xTemp] = 0
                caminho[desX][desY] = 0
                ini = time.time()
                
    

   
        if(pygame.mouse.get_pressed()[0] == True):
            pos = pygame.mouse.get_pos()
            xTemp = int(pos[1]/100)
            yTemp = int(pos[0]/100)
            p = []
            p.append(yTemp*100)
            p.append(xTemp*100)
            if(caminho[xTemp][yTemp] == 0):
                i = Personagem.Personagem()
                i.sprite(tamanhoTela,spriteIninimigo)
                fantasma.append(i)
                fantasma[len(fantasma)-1].rect.y = xTemp*100
                fantasma[len(fantasma)-1].rect.x = yTemp*100
                todas_as_sprites.add(fantasma[len(fantasma)-1])
                while(caminho[xTemp][yTemp] == 0):
                    caminho[xTemp][yTemp] = -1
                time.sleep(0.01)
            else:
                for i in fantasma:
                    if(i.rect.collidepoint(p)):
                        if(isinstance(i, Personagem.Personagem)):
                            todas_as_sprites.remove(i)
                            while(caminho[xTemp][yTemp] == -1):
                                caminho[xTemp][yTemp] = 0
                            time.sleep(0.01)
                            

        if(pygame.mouse.get_pressed()[2] == True):
            pos = pygame.mouse.get_pos()
            xTemp = int(pos[1]/100)
            yTemp = int(pos[0]/100)
            p = []
            p.append(yTemp*100)
            p.append(xTemp*100)
            if(caminho[xTemp][yTemp] == 0):
                c = Personagem.Personagem()
                c.sprite(tamanhoTela,spriteComida)
                comida.append(c)
                comida[len(comida)-1].rect.y = xTemp*100
                comida[len(comida)-1].rect.x = yTemp*100
                todas_as_sprites.add(comida[len(comida)-1])
                while(caminho[xTemp][yTemp] == 0):
                    caminho[xTemp][yTemp] = 3
                time.sleep(0.01)
            else:
                for i in comida:
                    if(i.rect.collidepoint(p)):
                        if(isinstance(i, Personagem.Personagem)):
                            todas_as_sprites.remove(i)
                            while(caminho[xTemp][yTemp] == 3):
                                caminho[xTemp][yTemp] = 0
                            time.sleep(0.01)
    
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 700), (800, 700), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 600), (800, 600), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 500), (800, 500), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 400), (800, 400), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 300), (800, 300), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 200), (800, 200), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (0, 100), (800, 100), 1)

  


    pygame.draw.line(janela, pygame.Color(255,255,255), (100, 0), (100, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (200, 0), (200, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (300, 0), (300, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (400, 0), (400, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (500, 0), (500, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (600, 0), (600, 800), 1)
    pygame.draw.line(janela, pygame.Color(255,255,255), (700, 0), (700, 800), 1)
    
    
    todas_as_sprites.draw(janela)
    todas_as_sprites.update()
    
    pygame.display.update()
    janela.fill((0,0,0))