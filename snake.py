import pygame
import random

#inicia as fonts no pygame
pygame.font.init()

# tupla da cor de fundo
blue = (50, 100, 213)
orange = (205, 102, 0)
green = (0, 255, 0)

# tupla da dimensão da tela
size = (600, 600)

# posição do quadardo (cobrinha)
x = 300
y = 300

# tamanho do quadrado
d = 20

# posições da cobra
snakeList = [[x, y]]

# novas posições do corpo
dx = 0
dy = 0

#coordenada aleatória inicial do comida
xFood = round(random.randrange(0, 600 -d) / 20) * 20
yFood = round(random.randrange(0, 600 -d) / 20) * 20

# define a velocidade inicial da cobra
snakeSpeed = 5

#define a fonte usada na pontuação
font = pygame.font.SysFont("System Bols", 20)

# define o tamanho da tela
screen = pygame.display.set_mode((size))
# define o titulo da tela
pygame.display.set_caption('Snake do Ygor')

# define a cor azul para o fundo
screen.fill(blue)

#define a clock para controlar a quantidade de atualizações da screen
clock = pygame.time.Clock()

def drawSnake(snakeList):
    #limpa a tela (pinta as outras posições, sem ser a atual de azul)
    screen.fill(blue)
    for unity in snakeList:
        #define o posição e posição da cobra
        pygame.draw.rect(screen, orange, [unity[0], unity[1], d, d])

# função para movimentar, recebe a posição atual
def moveSnake(dx, dy, snakeList):
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
    xNew = snakeList[-1][0] + dx
    yNew = snakeList[-1][1] + dy
 
    snakeList.append([xNew, yNew])

    # apaga a ultima posição
    del snakeList[0]

    # retorna as novas coordenadas
    return dx, dy, snakeList

#verifica se ele comeu a comida
def verifyFood(dx, dy, xFood, yFood, snakeList, snakeSpeed):
    
    head = snakeList[-1]

    xNew = head[0] + dx
    yNew = head[1] + dy

    # se a cabeça da cobra estiver na posição da comida
    if head[0] == xFood and head[1] == yFood:
        snakeList.append([xNew, yNew])
        # gera uma nova posição aleatória para a comida
        xFood = round(random.randrange(0, 600 -d) / 20) * 20
        yFood = round(random.randrange(0, 600 -d) / 20) * 20
        snakeSpeed = snakeSpeed + 1

    #desenha a comida
    pygame.draw.rect(screen, green, [xFood, yFood, d, d])

    return xFood, yFood, snakeList, snakeSpeed

#verifica se bateu na parede
def verifyWall(snakeList):
    # define a cabeça como a primeira lista do snakeList
    head = snakeList[-1]
    # define o x e o y da cabeça
    x = head[0]
    y = head[1]

    # verifica se a cabeça não está no range da screen
    if x not in range(600) or y not in range (600):
        # raise interrompe a execução
        raise Exception

# verifica se houve colisão da cabeça com o corpo da cobra
def verifyCollision(snakeList):
    # define a cabeça como a primeira lista do snakeList
    head = snakeList[-1]
    #copia a lista da cobra
    snakeBody = snakeList.copy()
    #deleta a posição da cabeça
    del snakeBody[-1]

    #para as coordenadas do corpo
    for x, y in snakeBody:
        #se a cabeça estiver na mesma coordenada que o corpo
        if x == head[0] and y == head[1]:
            # raise interrompe a execução
            raise Exception

#atualiza e imprime a quantidade de pontos
def updatePoints(snakeList):
    #define os pontos como o tamanho do snakeList
    pts = str(len(snakeList))
    # define o que irá mostrar na pontuação
    score = font.render("Pontuação: " + pts, True, orange)
    # coloca a pontuação na tela
    screen.blit(score, [0,0])

#enquanto for verdadeiro
while True:
    #atualiza a tela
    pygame.display.update()
    clock.tick(snakeSpeed)
    # desenha a cobra
    drawSnake(snakeList)
    # manda a posição atual da cobra para a função, e com o retorno define a nova posição
    dx, dy, snakeList = moveSnake(dx, dy, snakeList)
    # manda a posição atual da comida para a função, quando pegamos retorna a nova posição
    xFood, yFood, snakeList, snakeSpeed = verifyFood(dx, dy, xFood, yFood, snakeList, snakeSpeed)
    # verifica se a cobra bateu na parede
    verifyWall(snakeList)
    # verifica se a cobra bateu nela mesma
    verifyCollision(snakeList)
    #atualiza a quantidade de pontos
    updatePoints(snakeList)
    # print para debug
    print(snakeList)