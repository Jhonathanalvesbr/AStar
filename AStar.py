import math
import Estado

def inserir(lista, aux):
    j = 0
    while(len(lista) > 0 and j < len(lista) and aux.f >= lista[j].f):
        j += 1
    lista.insert(j, aux)

    return lista

def existe(lista, filho):
    if(len(lista) == 0):
        return -1
    for i in lista:
        if(i.x == filho.x and i.y == filho.y):
            return 1
    return -1

def custo(x, y, desX, desY):
    return math.sqrt(pow((x - desX), 2.0)+pow((y - desY), 2.0))

def criaEstado(self, iniX, iniY):
    # Baixo
    if(iniX+1 >= 0 and iniY >= 0 and iniX+1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX+1][iniY] == 0):
        # print("Baixo")
        return Estado.Estado(iniX+1, iniY)
        # Cima
    elif(iniX-1 >= 0 and iniY >= 0 and iniX-1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX-1][iniY] == 0):
        # print("Cima")
        return Estado.Estado(iniX-1, iniY)
        # Direita
    elif(iniX >= 0 and iniY+1 >= 0 and iniX < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX][iniY+1] == 0):
        # print("Direita")
        return Estado.Estado(iniX, iniY+1)
        # Esquerda
    elif(iniX >= 0 and iniY-1 >= 0 and iniX < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX][iniY-1] == 0):
        # print("Esquerda")
        return Estado.Estado(iniX, iniY-1)
        # 135
    elif(iniX+1 >= 0 and iniY+1 >= 0 and iniX+1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX+1][iniY+1] == 0):
        # print("135")
        return Estado.Estado(iniX+1, iniY+1)
        # 225
    elif(iniX+1 >= 0 and iniY-1 >= 0 and iniX+1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX+1][iniY-1] == 0):
        # print("225")
        return Estado.Estado(iniX+1, iniY-1)
        # 315
    elif(iniX-1 >= 0 and iniY-1 >= 0 and iniX-1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX-1][iniY-1] == 0):
        # print("315")
        return Estado.Estado(iniX-1, iniY-1)
        # 45
    elif(iniX-1 >= 0 and iniY+1 >= 0 and iniX-1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX-1][iniY+1] == 0):
        # print("45")
        return Estado.Estado(iniX-1, iniY+1)
    else:
        return -1

def getCaminho(filho):
    pai = filho.parente
    lista = []
    lista.append([filho.y, filho.x])
    while(pai.parente != []):
        lista.append([pai.y, pai.x])
        pai = pai.parente
    return list(reversed(lista))

class Astar():
    caminho = []
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def criarNo(self, q, i):
        if(q == -1):
            return
        iniX = q.x
        iniY = q.y
        # Baixo
        if(iniX+1 >= 0 and iniY >= 0 and iniX+1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX+1][iniY] == 0 and i == 0):
            # print("Baixo")
            return (Estado.Estado(iniX+1, iniY))
        # Cima
        elif(iniX-1 >= 0 and iniY >= 0 and iniX-1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX-1][iniY] == 0 and i == 1):
            # print("Cima")
            return (Estado.Estado(iniX-1, iniY))
        # Direita
        elif(iniX >= 0 and iniY+1 >= 0 and iniX < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX][iniY+1] == 0 and i == 2):
            # print("Direita")
            return (Estado.Estado(iniX, iniY+1))
        # Esquerda
        elif(iniX >= 0 and iniY-1 >= 0 and iniX < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX][iniY-1] == 0 and i == 3):
            # print("Esquerda")
            return (Estado.Estado(iniX, iniY-1))
        # 135
        elif(iniX+1 >= 0 and iniY+1 >= 0 and iniX+1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX+1][iniY+1] == 0 and i == 4):
            # print("135")
            return (Estado.Estado(iniX+1, iniY+1))
        # 225
        elif(iniX+1 >= 0 and iniY-1 >= 0 and iniX+1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX+1][iniY-1] == 0 and i == 5):
            # print("225")
            return (Estado.Estado(iniX+1, iniY-1))
        # 315
        elif(iniX-1 >= 0 and iniY-1 >= 0 and iniX-1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX-1][iniY-1] == 0 and i == 6):
            # print("315")
            return (Estado.Estado(iniX-1, iniY-1))
        # 45
        elif(iniX-1 >= 0 and iniY+1 >= 0 and iniX-1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX-1][iniY+1] == 0 and i == 7):
            # print("45")
            return (Estado.Estado(iniX-1, iniY+1))

    def win(self, e, target):
        if(e == -1):
            return -1
        iniX = e.x
        iniY = e.y
        # Baixo
        if(iniX+1 >= 0 and iniY >= 0 and iniX+1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX+1][iniY] == target):
            # print("Baixo")
            return Estado.Estado(iniX+1, iniY)
        # Cima
        elif(iniX-1 >= 0 and iniY >= 0 and iniX-1 < self.tamanho and iniY < self.tamanho and self.caminho[iniX-1][iniY] == target):
            # print("Cima")
            return Estado.Estado(iniX-1, iniY)
        # Direita
        elif(iniX >= 0 and iniY+1 >= 0 and iniX < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX][iniY+1] == target):
            # print("Direita")
            return Estado.Estado(iniX, iniY+1)
        # Esquerda
        elif(iniX >= 0 and iniY-1 >= 0 and iniX < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX][iniY-1] == target):
            # print("Esquerda")
            return Estado.Estado(iniX, iniY-1)
        # 135
        elif(iniX+1 >= 0 and iniY+1 >= 0 and iniX+1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX+1][iniY+1] == target):
            # print("135")
            return Estado.Estado(iniX+1, iniY+1)
        # 225
        elif(iniX+1 >= 0 and iniY-1 >= 0 and iniX+1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX+1][iniY-1] == target):
            # print("225")
            return Estado.Estado(iniX+1, iniY-1)
        # 315
        elif(iniX-1 >= 0 and iniY-1 >= 0 and iniX-1 < self.tamanho and iniY-1 < self.tamanho and self.caminho[iniX-1][iniY-1] == target):
            # print("315")
            return Estado.Estado(iniX-1, iniY-1)
        # 45
        elif(iniX-1 >= 0 and iniY+1 >= 0 and iniX-1 < self.tamanho and iniY+1 < self.tamanho and self.caminho[iniX-1][iniY+1] == target):
            # print("45")
            return Estado.Estado(iniX-1, iniY+1)
        else:
            return -1

    def imprimir(self, caminho):
        self.caminho = self.caminho
        for x in range(len(self.caminho)):
            for y in range(len(self.caminho)):
                print(self.caminho[x][y], end="")
                print("|", end="")
            print()
        print()

    def busca(self, caminho, pernosagemAtual, target):
        for x in range(len(caminho)):
            for y in range(len(caminho)):
                if(caminho[x][y] == pernosagemAtual):
                    print(caminho[x][y])
                    iniX = x
                    iniY = y
                elif(caminho[x][y] == target):
                    desX = x
                    desY = y
        listaAberta = []
        listaFechada = []
        self.caminho = caminho
        listaAberta.append(Estado.Estado(iniX, iniY))
        while(len(listaAberta) > 0):
            pai = listaAberta[0]
            listaFechada.append(pai)
            listaAberta.pop(0)
            w = self.win(pai,target)
            if(w != -1):
                #print("Win")
                w.parente = pai
                return getCaminho(w)
            for i in range(8):
                filho = self.criarNo(pai, i)
                if(filho != None and existe(listaAberta, filho) != 1 and existe(listaFechada, filho) != 1):
                    filho.g = pai.g + 1.0
                    filho.h = custo(filho.x, filho.y, desX, desY)
                    filho.f = filho.g + filho.h
                    filho.parente = pai
                    inserir(listaAberta, filho)

    def imprimirCaminho(self, e):
        a = e.parente
        while(a.parente != []):
            for x in range(self.tamanho):
                for y in range(self.tamanho):
                    if(a.x == x and a.y == y):
                        print("2", end="")
                    else:
                        print("0", end="")
                print()
            print()
            a = a.parente

    def CaminhoVazio(self, caminho):
        for x in range(len(self.caminho)):
            for y in range(len(self.caminho)):
                if(self.caminho[x][y] == target):
                    return 1
        return -1
