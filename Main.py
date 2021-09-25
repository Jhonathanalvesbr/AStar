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
tamanhoTela = 600
passo = 25
tamanho = int(tamanhoTela/passo)
caminho = []
movimentoPacMan = []
fantasmaMovimento = []
busca = AStar.Astar(tamanho)

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
pacMan.tamanho = tamanho
pacMan.id = 1
todas_as_sprites = pygame.sprite.Group()
todas_as_sprites.add(pacMan)
fantasma = []

pygame.init()
janela = pygame.display.set_mode((tamanhoTela,tamanhoTela))
pygame.display.set_caption('Game IA')

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


def mover(personagem, movimento):
    if(personagem.fim-personagem.ini  > personagem.velocidade and len(movimento) > 0):
        for f in fantasma:
            if(f.mover == 1):
                f.mover = 0
        if(personagem.rect.x < movimento[0][0]*passo):
            personagem.angle = 0
        if(personagem.rect.x > movimento[0][0]*passo):
            personagem.angle = 180
        if(personagem.rect.y > movimento[0][1]*passo):
            personagem.angle = -90
        if(personagem.rect.y > movimento[0][1]*passo):
            personagem.angle = 90
            
        print(personagem.movimento)
        personagem.ini = time.time()
        personagem.rect.x = movimento[0][0]*passo
        personagem.rect.y =  movimento[0][1]*passo
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
                    caminho[int(f.rect.y/passo)][int(f.rect.x/passo)] = -1
            if(len(comida) > 0):
                for c in comida:
                    caminho[int(c.rect.y/passo)][int(c.rect.x/passo)] = 3

            caminho[int(pacMan.rect.y/passo)][int(pacMan.rect.x/passo)] = 1
            
            
            if(len(comida) > 0):
                for f in fantasma:
                    if(f.mover == 0 and f.seguir == True):
                        mov = getCaminho(pacMan,1,-1)
                        if(mov != None):
                            for i in mov:
                                movimento.append(i)
                            f.movimento = mov
            if(len(comida) > 0):
                mov = getCaminho(pacMan,1,3)
                if(mov != None):
                    for i in mov:
                        movimento.append(i)
                    pacMan.movimento = mov
            if(len(comida) == 0):
                pacMan.mover = 0
                pacMan.seguir = False
        personagem.ini = time.time()


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
    
    x = int(personagem.rect.x/passo)
    y = int(personagem.rect.y/passo)
    caminho[y][x] = pernosagemAtual
    movimento = busca.busca(caminho,[y,x],pernosagemAlvo,x,y,personagem)
    if(movimento == None):
        return None
    #print(movimento)
    caminho[y][x] = 0
    return movimento

while True:
    if(len(fantasma) > 0):
        for f in fantasma:
            if(f.mover == 0 and f.seguir == True):
                temp = getCaminho(f,-1,targetPacMan)
                if(temp != None):
                    f.movimento = temp
                    f.mover += 1
                else:
                    f.mover = 0
                    f.seguir = False

    if(len(fantasma)>0):
        for f in fantasma:
            if(f.mover == 1 and f.seguir == True):
                mover(f,f.movimento)
        
    if(pacMan.mover == 0 and pacMan.seguir == True):
        temp = getCaminho(pacMan,1,targetComida)
        if(temp != None):
            pacMan.movimento = temp
            pacMan.mover += 1
        else:
            pacMan.mover = 0
            pacMan.seguir = False
    elif(pacMan.mover == 1 and pacMan.seguir == True):
        mover(pacMan,pacMan.movimento)
    

        
    encosta(pacMan,comida)        
    
    for x in range(len(caminho)):
        for y in range(len(caminho)):
            caminho[x][y] = 0
    if(len(fantasma) > 0):
        for f in fantasma:
            caminho[int(f.rect.y/passo)][int(f.rect.x/passo)] = -1
            f.x = f.rect.y/passo
            f.y = f.rect.x/passo
            f.fim= time.time()
    if(len(comida) > 0):
        for c in comida:
            caminho[int(c.rect.y/passo)][int(c.rect.x/passo)] = 3
            c.fim = time.time()

    caminho[int(pacMan.rect.y/passo)][int(pacMan.rect.x/passo)] = 1
    pacMan.x = pacMan.rect.y/passo
    pacMan.y = pacMan.rect.x/passo
    pacMan.fim = time.time()
    for event in pygame.event.get():
        teclado = pygame.key.get_pressed()
        if(teclado[pygame.K_LEFT]):
            if(pacMan.rect.x > 0):
                if(caminho[int(pacMan.rect.y/passo)][int(pacMan.rect.x/passo)-1] != -1):
                    pacMan.esquerda(passo)
                    pacMan.angulo(180)
    
        if(teclado[pygame.K_RIGHT]):
            if(pacMan.rect.x < tamanhoTela-passo):
                if(caminho[int(pacMan.rect.y/passo)][int(pacMan.rect.x/passo)+1] != -1):
                    pacMan.direita(passo)
                    pacMan.angulo(0)

        if(teclado[pygame.K_UP]):
            if(pacMan.rect.y > 0):
                if(caminho[int(pacMan.rect.y/passo)-1][int(pacMan.rect.x/passo)] != -1):
                    pacMan.cima(passo)
                    pacMan.angulo(90)

        if(teclado[pygame.K_DOWN]):
            if(pacMan.rect.y < tamanhoTela-passo):
                if(caminho[int(pacMan.rect.y/passo)+1][int(pacMan.rect.x/passo)] != -1):
                    pacMan.baixo(passo)
                    pacMan.angulo(-90)

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if(teclado[pygame.K_F5]):
            if(pacMan.seguir == False and caminhoVazio(targetComida) == 1):
                pacMan.seguir = True
            elif(pacMan.seguir == True):
                pacMan.seguir = False

        if(pygame.mouse.get_pressed()[0] == True):
            pos = pygame.mouse.get_pos()
            xTemp = int(pos[1]/passo)
            yTemp = int(pos[0]/passo)
            p = []
            p.append(yTemp*passo)
            p.append(xTemp*passo)
            if(caminho[xTemp][yTemp] == 0):
                i = Personagem.Personagem()
                i.sprite(tamanhoTela,spriteIninimigo)
                fantasma.append(i)
                fantasma[len(fantasma)-1].x = xTemp
                fantasma[len(fantasma)-1].tamanho = 6
                fantasma[len(fantasma)-1].caminhar = True
                fantasma[len(fantasma)-1].y = yTemp
                fantasma[len(fantasma)-1].velocidade = 1
                fantasma[len(fantasma)-1].rect.y = xTemp*passo
                fantasma[len(fantasma)-1].rect.x = yTemp*passo
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
            xTemp = int(pos[1]/passo)
            yTemp = int(pos[0]/passo)
            p = []
            p.append(yTemp*passo)
            p.append(xTemp*passo)
            if(caminho[xTemp][yTemp] == 0):
                c = Personagem.Personagem()
                c.sprite(tamanhoTela,spriteComida)
                comida.append(c)
                comida[len(comida)-1].rect.y = xTemp*passo
                comida[len(comida)-1].rect.x = yTemp*passo
                todas_as_sprites.add(comida[len(comida)-1])
                
            else:
                i = 0
                while i < len(comida):
                    if(comida[i].rect.collidepoint(p)):
                        if(isinstance(comida[i], Personagem.Personagem)):
                            todas_as_sprites.remove(comida[i])
                            comida.pop(i)
                            break
                    i += 1

        if(pygame.mouse.get_pressed()[1] == True):
            
            pos = pygame.mouse.get_pos()
            xTemp = int(pos[1]/passo)
            yTemp = int(pos[0]/passo)
            p = []
            p.append(yTemp*passo)
            p.append(xTemp*passo)
            
            if(caminho[xTemp][yTemp] == -1):
                i = 0
                while i < len(fantasma):
                    if(fantasma[i].rect.collidepoint(p)):
                        if(isinstance(fantasma[i], Personagem.Personagem)):
                            if(fantasma[i].seguir == False):
                                fantasma[i].seguir = True
                            else:
                                fantasma[i].seguir = False
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