import pygame
import random

#inicia as fontes no pygame
pygame.font.init()

# tupla da cor de fundo
azul = (50, 100, 213)
laranja = (205, 102, 0)
verde = (0, 255, 0)

# tupla da dimensão da tela
dimensoes = (600, 600)

# posição do quadardo (cobrinha)
x = 300
y = 300

# tamanho do quadrado
d = 20

# posições da cobra
lista_cobra = [[x, y]]

# novas posições do corpo
dx = 0
dy = 0

#coordenada aleatória inicial do comida
x_comida = round(random.randrange(0, 600 -d) / 20) * 20
y_comida = round(random.randrange(0, 600 -d) / 20) * 20

# define a velocidade inicial da cobra
velocidade_cobra = 5

#define a fonte usada na pontuação
fonte = pygame.font.SysFont("System Bols", 20)

# define o tamanho da tela
tela = pygame.display.set_mode((dimensoes))
# define o titulo da tela
pygame.display.set_caption('Snake do Ygor')

# define a cor azul para o fundo
tela.fill(azul)

#define a clock para controlar a quantidade de atualizações da tela
clock = pygame.time.Clock()

def desenha_cobra(lista_cobra):
    #limpa a tela (pinta as outras posições, sem ser a atual de azul)
    tela.fill(azul)
    for unidade in lista_cobra:
        #define o posição e posição da cobra
        pygame.draw.rect(tela, laranja, [unidade[0], unidade[1], d, d])

# função para movimentar, recebe a posição atual
def mover_cobra(dx, dy, lista_cobra):
    # para escutar as teclas
    for event in pygame.event.get():
        #se apertar a tecla
        if event.type == pygame.KEYDOWN:
            #se apertar seta pra esquerda
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d

    # adiciona o movimento a posição anterior
    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy
 
    lista_cobra.append([x_novo, y_novo])

    # apaga a ultima posição
    del lista_cobra[0]

    # adiciona o movimento a posição anterior
    # x = x + delta_xs
    # y = y + delta_y

    # retorna as novas coordenadas
    return dx, dy, lista_cobra

#verifica se ele comeu a comida
def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra, velocidade_cobra):
    
    head = lista_cobra[-1]

    x_novo = head[0] + dx
    y_novo = head[1] + dy

    # se a cabeça da cobra estiver na posição da comida
    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])
        # gera uma nova posição aleatória para a comida
        x_comida = round(random.randrange(0, 600 -d) / 20) * 20
        y_comida = round(random.randrange(0, 600 -d) / 20) * 20
        velocidade_cobra = velocidade_cobra + 1

    #desenha a comida
    pygame.draw.rect(tela, verde, [x_comida, y_comida, d, d])

    return x_comida, y_comida, lista_cobra, velocidade_cobra

#verifica se bateu na parede
def verifica_parede(lista_cobra):
    # define a cabeça como a primeira lista do lista_cobra
    head = lista_cobra[-1]
    # define o x e o y da cabeça
    x = head[0]
    y = head[1]

    # verifica se a cabeça não está no range da tela
    if x not in range(600) or y not in range (600):
        # raise interrompe a execução
        raise Exception

# verifica se houve colisão da cabeça com o corpo da cobra
def verifica_colisao(lista_cobra):
    # define a cabeça como a primeira lista do lista_cobra
    head = lista_cobra[-1]
    #copia a lista da cobra
    corpo_cobra = lista_cobra.copy()
    #deleta a posição da cabeça
    del corpo_cobra[-1]

    #para as coordenadas do corpo
    for x, y in corpo_cobra:
        #se a cabeça estiver na mesma coordenada que o corpo
        if x == head[0] and y == head[1]:
            # raise interrompe a execução
            raise Exception

#atualiza e imprime a quantidade de pontos
def atualizar_pontos(lista_cobra):
    #define os pontos como o tamanho do lista_cobra
    pts = str(len(lista_cobra))
    # define o que irá mostrar na pontuação
    score = fonte.render("Pontuação: " + pts, True, laranja)
    # coloca a pontuação na tela
    tela.blit(score, [0,0])

#enquanto for verdadeiro
while True:
    #atualiza a tela
    pygame.display.update()
    clock.tick(velocidade_cobra)
    # desenha a cobra
    desenha_cobra(lista_cobra)
    # manda a posição atual da cobra para a função, e com o retorno define a nova posição
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    # manda a posição atual da comida para a função, quando pegamos retorna a nova posição
    x_comida, y_comida, lista_cobra, velocidade_cobra = verifica_comida(dx, dy, x_comida, y_comida, lista_cobra, velocidade_cobra)
    # verifica se a cobra bateu na parede
    verifica_parede(lista_cobra)
    # verifica se a cobra bateu nela mesma
    verifica_colisao(lista_cobra)
    #atualiza a quantidade de pontos
    atualizar_pontos(lista_cobra)
    # print para debug
    print(lista_cobra)