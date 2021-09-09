import Personagem
import AStar
import pygame
import time
import pygame
from pygame.locals import *
from sys import exit
import time

targetPacMan = 1
targetFantasma = -1
targetComida = 3
tamanhoTela = 800
tamanho = 8
caminho = []
movimentoPacMan = []
fantasmaMovimento = []
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
spriteIninimigo.append(pygame.image.load('f1.png'))
spriteComida.append(pygame.image.load('c1.png'))
pacMan = Personagem.Personagem()
pacMan.sprite(tamanhoTela,spritePacMan)

todas_as_sprites = pygame.sprite.Group()
todas_as_sprites.add(pacMan)
fantasma = []

pygame.init()
janela = pygame.display.set_mode((tamanhoTela,tamanhoTela))

def caminhoVazio(target):
    for x in range(len(caminho)):
        for y in range(len(caminho)):
            if(caminho[x][y] == target):
                return 1
    return -1
    

def caminhoPrint():
    for i in range(len(caminho)):
        print(caminho[i])
    print()


def moverInimigo(personagem, movimento, target, player):
    global pp
    global ini
    global fim
    if(fim-ini  > 0.5 and len(movimento) > 0):
        iniY = int(player.rect.x/100)
        iniX = int(player.rect.y/100)
        pp = 0
        if(personagem.rect.x < movimento[0][0]*100):
            personagem.angle = 0
        if(personagem.rect.x > movimento[0][0]*100):
            personagem.angle = 180
        if(personagem.rect.y > movimento[0][1]*100):
            personagem.angle = -90
        if(personagem.rect.y > movimento[0][1]*100):
            personagem.angle = 90
        
        ini = time.time()
        personagem.rect.x = movimento[0][0]*100
        personagem.rect.y =  movimento[0][1]*100
        p = []
        p.append(personagem.rect.x)
        p.append(personagem.rect.y)
        movimento.pop(0)
        if(len(movimento) == 0):
            
            encosta(pacMan,comida) 
            for x in range(len(caminho)):
                for y in range(len(caminho)):
                    caminho[x][y] = 0
            if(len(fantasma) > 0):
                for f in fantasma:
                    caminho[int(f.rect.y/100)][int(f.rect.x/100)] = -1
            if(len(comida) > 0):
                for c in comida:
                    caminho[int(c.rect.y/100)][int(c.rect.x/100)] = 3

            caminho[int(pacMan.rect.y/100)][int(pacMan.rect.x/100)] = 1
            
            
            if(len(comida) > 0):
                mov = getCaminho(pacMan,1,-1)
                for i in mov:
                    movimento.append(i)
        


def mover(personagem, movimento,target):
    global ini
    global fim
    if(movimento != None and fim-ini  > 0.5 and len(movimento) > 0):
        if(personagem.rect.x < movimento[0][0]*100):
            personagem.angle = 0
        if(personagem.rect.x > movimento[0][0]*100):
            personagem.angle = 180
        if(personagem.rect.y > movimento[0][1]*100):
            personagem.angle = -90
        if(personagem.rect.y > movimento[0][1]*100):
            personagem.angle = 90
        
        
        personagem.rect.x = movimento[0][0]*100
        personagem.rect.y =  movimento[0][1]*100
       
        p = []
        p.append(personagem.rect.x)
        p.append(personagem.rect.y)
        movimento.pop(0)
        print(movimento)
        if(len(movimento) == 0):
            
            encosta(pacMan,comida) 
            for x in range(len(caminho)):
                for y in range(len(caminho)):
                    caminho[x][y] = 0
            if(len(fantasma) > 0):
                for f in fantasma:
                    caminho[int(f.rect.y/100)][int(f.rect.x/100)] = -1
            if(len(comida) > 0):
                for c in comida:
                    caminho[int(c.rect.y/100)][int(c.rect.x/100)] = 3

            caminho[int(pacMan.rect.y/100)][int(pacMan.rect.x/100)] = 1
            
            
            if(len(comida) > 0):
                mov = getCaminho(pacMan,1,target)
                for i in mov:
                    movimento.append(i)
                
        ini = time.time()




def encosta(personagem,encosta):
    p = []
    p.append(personagem.rect.x)
    p.append(personagem.rect.y)
    i = 0
    while i in range(len(encosta)):
        if(encosta[i].rect.collidepoint(p)):
            if(isinstance(encosta[i], Personagem.Personagem)):
                todas_as_sprites.remove(encosta[i])
                encosta.pop(i)
                break
        i += 1

def getCaminho(personagem,pernosagemAtual,pernosagemAlvo):
    movimento = []
    global ini
    time.sleep(0.05)
    x = int(personagem.rect.x/100)
    y = int(personagem.rect.y/100)
    caminho[y][x] = pernosagemAtual
    movimento = busca.busca(caminho,pernosagemAtual,pernosagemAlvo)
    #print(movimento)
    caminho[y][x] = 0
    ini = time.time()
    
    return movimento

pp = 0
while True:
    fim = time.time()
    if(len(fantasma) > 0 and pp == 0):
        pp += 1
        fantasmaMovimento = getCaminho(fantasma[0],targetFantasma,targetPacMan)

    if(len(fantasma)>0):
        moverInimigo(fantasma[0],fantasmaMovimento,-1,pacMan)
        

    mover(pacMan,movimentoPacMan,targetComida)
    encosta(pacMan,comida)        
    
    for x in range(len(caminho)):
        for y in range(len(caminho)):
            caminho[x][y] = 0
    if(len(fantasma) > 0):
        for f in fantasma:
            caminho[int(f.rect.y/100)][int(f.rect.x/100)] = -1
    if(len(comida) > 0):
        for c in comida:
            caminho[int(c.rect.y/100)][int(c.rect.x/100)] = 3
    caminho[int(pacMan.rect.y/100)][int(pacMan.rect.x/100)] = 1

    for event in pygame.event.get():
        teclado = pygame.key.get_pressed()
        if(teclado[pygame.K_LEFT]):
            if(pacMan.rect.x > 0):
                if(caminho[int(pacMan.rect.y/100)][int(pacMan.rect.x/100)-1] != -1):
                    pacMan.esquerda()
                    pacMan.angulo(180)
    
        if(teclado[pygame.K_RIGHT]):
            if(pacMan.rect.x < 700):
                if(caminho[int(pacMan.rect.y/100)][int(pacMan.rect.x/100)+1] != -1):
                    pacMan.direita()
                    pacMan.angulo(0)

        if(teclado[pygame.K_UP]):
            if(pacMan.rect.y > 0):
                if(caminho[int(pacMan.rect.y/100)-1][int(pacMan.rect.x/100)] != -1):
                    pacMan.cima()
                    pacMan.angulo(90)

        if(teclado[pygame.K_DOWN]):
            if(pacMan.rect.y < 700):
                if(caminho[int(pacMan.rect.y/100)+1][int(pacMan.rect.x/100)] != -1):
                    pacMan.baixo()
                    pacMan.angulo(-90)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if(teclado[pygame.K_F5]):
            if(caminhoVazio(targetComida) == 1):
                movimentoPacMan = getCaminho(pacMan,targetPacMan,targetComida)

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
            else:
                i = 0
                while i < len(fantasma):
                    if(fantasma[i].rect.collidepoint(p)):
                        if(isinstance(fantasma[i], Personagem.Personagem)):
                            todas_as_sprites.remove(fantasma[i])
                            fantasma.pop(i)
                            break
                    i += 1
                
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
                time.sleep(0.01)
            else:
                i = 0
                while i < len(comida):
                    if(comida[i].rect.collidepoint(p)):
                        if(isinstance(comida[i], Personagem.Personagem)):
                            todas_as_sprites.remove(comida[i])
                            comida.pop(i)
                            break
                    i += 1

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