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
spriteIninimigo.append(pygame.image.load('f1L.png'))
spriteIninimigo.append(pygame.image.load('f1R.png'))
spriteIninimigo.append(pygame.image.load('f1up.png'))
spriteIninimigo.append(pygame.image.load('f1down.png'))
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
        if(personagem.id != -1):
            if(personagem.rect.x < movimento[0][0]*passo):
                personagem.angle = 0
            if(personagem.rect.x > movimento[0][0]*passo):
                personagem.angle = 180
            if(personagem.rect.y > movimento[0][1]*passo):
                personagem.angle = -90
            if(personagem.rect.y > movimento[0][1]*passo):
                personagem.angle = 90
        elif(personagem.id == -1 and personagem.seguir == True):
            if(personagem.rect.x < movimento[0][0]*passo):
                personagem.angle = 0
                personagem.image = personagem.sprites[2]
            if(personagem.rect.x > movimento[0][0]*passo):
                personagem.angle = 0
                personagem.image = personagem.sprites[1]
            if(personagem.rect.y > movimento[0][1]*passo):
                personagem.angle = 0
                personagem.image = personagem.sprites[4]
            if(personagem.rect.y > movimento[0][1]*passo):
                personagem.angle = 0
                personagem.image = personagem.sprites[3]

            
        #print(personagem.movimento)
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


caminho[3][4] = -1
caminho[3][5] = -1
caminho[3][6] = -1
caminho[3][7] = -1
caminho[3][8] = -1
caminho[3][9] = -1
caminho[3][10] = -1
caminho[3][11] = -1
caminho[3][12] = -1
caminho[3][13] = -1
caminho[3][14] = -1
caminho[3][15] = -1
caminho[3][16] = -1
caminho[3][17] = -1
caminho[3][18] = -1
caminho[3][19] = -1
caminho[3][20] = -1
caminho[3][21] = -1
caminho[3][22] = -1
caminho[3][23] = -1
caminho[4][23] = -1
caminho[5][23] = -1
caminho[6][23] = -1
caminho[7][23] = -1
caminho[8][23] = -1
caminho[9][23] = -1
caminho[10][23] = -1
caminho[11][23] = -1
caminho[12][23] = -1
caminho[13][23] = -1
caminho[14][23] = -1
caminho[15][23] = -1
caminho[16][23] = -1
caminho[17][23] = -1
caminho[18][23] = -1
caminho[19][23] = -1
caminho[20][23] = -1
caminho[21][23] = -1
caminho[22][23] = -1
caminho[23][23] = -1
caminho[5][4] = -1
caminho[6][4] = -1
caminho[7][4] = -1
caminho[8][4] = -1
caminho[9][4] = -1
caminho[10][4] = -1
caminho[11][4] = -1
caminho[12][4] = -1
caminho[13][4] = -1
caminho[14][4] = -1
caminho[15][4] = -1
caminho[16][4] = -1
caminho[17][4] = -1
caminho[18][4] = -1
caminho[19][4] = -1
caminho[20][4] = -1
caminho[21][4] = -1
caminho[22][4] = -1
caminho[23][4] = -1
caminho[23][5] = -1
caminho[23][6] = -1
caminho[23][7] = -1
caminho[23][8] = -1
caminho[23][9] = -1
caminho[23][10] = -1
caminho[23][12] = -1
caminho[23][13] = -1
caminho[23][14] = -1
caminho[23][15] = -1
caminho[23][16] = -1
caminho[23][17] = -1
caminho[23][18] = -1
caminho[23][19] = -1
caminho[23][20] = -1
caminho[23][21] = -1
caminho[23][22] = -1
caminho[23][11] = -1
caminho[5][6] = -1
caminho[5][7] = -1
caminho[5][8] = -1
caminho[5][10] = -1
caminho[5][9] = -1
caminho[6][6] = -1
caminho[7][6] = -1
caminho[7][7] = -1
caminho[7][9] = -1
caminho[8][9] = -1
caminho[9][9] = -1
caminho[5][12] = -1
caminho[6][12] = -1
caminho[7][12] = -1
caminho[9][12] = -1
caminho[8][12] = -1
caminho[9][13] = -1
caminho[9][14] = -1
caminho[8][14] = -1
caminho[7][14] = -1
caminho[5][14] = -1
caminho[5][15] = -1
caminho[5][16] = -1
caminho[4][16] = -1
caminho[7][16] = -1
caminho[8][16] = -1
caminho[9][16] = -1
caminho[9][17] = -1
caminho[9][18] = -1
caminho[9][19] = -1
caminho[10][19] = -1
caminho[11][19] = -1
caminho[6][18] = -1
caminho[5][18] = -1
caminho[5][19] = -1
caminho[5][20] = -1
caminho[6][20] = -1
caminho[7][20] = -1
caminho[7][21] = -1
caminho[7][22] = -1
caminho[4][21] = -1
caminho[8][20] = -1
caminho[8][21] = -1
caminho[9][5] = -1
caminho[9][6] = -1
caminho[9][7] = -1
caminho[11][7] = -1
caminho[11][6] = -1
caminho[12][6] = -1
caminho[13][6] = -1
caminho[14][6] = -1
caminho[14][7] = -1
caminho[14][8] = -1
caminho[14][10] = -1
caminho[14][9] = -1
caminho[15][8] = -1
caminho[16][8] = -1
caminho[16][7] = -1
caminho[16][6] = -1
caminho[17][7] = -1
caminho[18][7] = -1
caminho[19][7] = -1
caminho[19][6] = -1
caminho[20][6] = -1
caminho[21][6] = -1
caminho[21][5] = -1
caminho[21][9] = -1
caminho[21][8] = -1
caminho[20][9] = -1
caminho[19][9] = -1
caminho[19][10] = -1
caminho[18][10] = -1
caminho[17][10] = -1
caminho[16][10] = -1
caminho[16][11] = -1
caminho[16][12] = -1
caminho[15][12] = -1
caminho[14][12] = -1
caminho[12][12] = -1
caminho[13][12] = -1
caminho[12][11] = -1
caminho[12][10] = -1
caminho[12][9] = -1
caminho[11][12] = -1
caminho[11][13] = -1
caminho[11][14] = -1
caminho[14][13] = -1
caminho[14][14] = -1
caminho[22][11] = -1
caminho[21][11] = -1
caminho[21][12] = -1
caminho[20][12] = -1
caminho[19][12] = -1
caminho[18][12] = -1
caminho[15][15] = -1
caminho[14][15] = -1
caminho[16][15] = -1
caminho[17][15] = -1
caminho[18][15] = -1
caminho[18][16] = -1
caminho[18][17] = -1
caminho[20][15] = -1
caminho[21][15] = -1
caminho[22][15] = -1
caminho[19][17] = -1
caminho[20][17] = -1
caminho[21][17] = -1
caminho[18][18] = -1
caminho[18][19] = -1
caminho[17][17] = -1
caminho[16][17] = -1
caminho[15][17] = -1
caminho[13][17] = -1
caminho[14][17] = -1
caminho[12][16] = -1
caminho[12][15] = -1
caminho[16][14] = -1
caminho[15][14] = -1
caminho[14][16] = -1
caminho[12][17] = -1
caminho[12][18] = -1
caminho[12][19] = -1
caminho[13][19] = -1
caminho[14][19] = -1
caminho[15][19] = -1
caminho[18][22] = -1
caminho[18][21] = -1
caminho[18][20] = -1
caminho[17][20] = -1
caminho[17][21] = -1
caminho[16][21] = -1
caminho[14][21] = -1
caminho[15][21] = -1
caminho[11][22] = -1
caminho[11][21] = -1
caminho[12][22] = -1
caminho[12][21] = -1
caminho[9][21] = -1

while True:

    for x in range(len(caminho)):
        for y in range(len(caminho)):
            if(caminho[x][y] == -1):
                e = -1
                for f in fantasma:
                    if(f.x == x and f.y == y):
                        e = 1
                        break
                if(e == -1):
                    i = Personagem.Personagem()
                    i.sprite(tamanhoTela,spriteIninimigo)
                    fantasma.append(i)
                    fantasma[len(fantasma)-1].x = x
                    fantasma[len(fantasma)-1].tamanho = 8
                    fantasma[len(fantasma)-1].caminhar = True
                    fantasma[len(fantasma)-1].y = y
                    fantasma[len(fantasma)-1].velocidade = 1
                    fantasma[len(fantasma)-1].rect.y = x*passo
                    fantasma[len(fantasma)-1].rect.x = y*passo
                    fantasma[len(fantasma)-1].id = -1
                    todas_as_sprites.add(fantasma[len(fantasma)-1])




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
                print("caminho["+str(xTemp)+"]["+str(yTemp)+"] = -1")
                i = Personagem.Personagem()
                i.sprite(tamanhoTela,spriteIninimigo)
                fantasma.append(i)
                fantasma[len(fantasma)-1].x = xTemp
                fantasma[len(fantasma)-1].tamanho = 8
                fantasma[len(fantasma)-1].caminhar = True
                fantasma[len(fantasma)-1].y = yTemp
                fantasma[len(fantasma)-1].velocidade = 1
                fantasma[len(fantasma)-1].rect.y = xTemp*passo
                fantasma[len(fantasma)-1].rect.x = yTemp*passo
                fantasma[len(fantasma)-1].id = -1
                todas_as_sprites.add(fantasma[len(fantasma)-1])
            else:
                i = 0
                while i < len(fantasma):
                    if(fantasma[i].rect.collidepoint(p)):
                        if(isinstance(fantasma[i], Personagem.Personagem)):
                            caminho[xTemp][yTemp] = 0
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
