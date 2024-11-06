import pygame
import time
import random

def show_score(color, font, size):
    """
    Exibe a pontuação na tela do jogo.

    1. Cria um objeto de fonte (`score_font`) usando o nome da fonte e o tamanho especificado.
    2. Gera uma superfície de texto (`score_surface`) que renderiza o texto "Score : " seguido do valor da pontuação atual, usando a cor especificada.
    3. Obtém um objeto retangular (`score_rect`) que representa o texto renderizado, facilitando o posicionamento na tela.
    4. Desenha o texto da pontuação na `game_window` usando o `blit`, que exibe `score_surface` na posição definida pelo retângulo (`score_rect`).

    Esta função usa a variável global `score`, que deve ser definida em outro ponto do código.

    Parâmetros:
        
        color (tuple): Uma tupla RGB que define a cor do texto (ex: (255, 255, 255) para branco).
        
        font (str): O nome da fonte que será usada para exibir o texto da pontuação (ex: 'Arial', 'Comic Sans MS').

        size (int): O tamanho da fonte a ser usada para o texto da pontuação.
    
    """
    # Cria um objeto de fonte com a fonte e tamanho especificados
    score_font = pygame.font.SysFont(font, size)
    
    # Cria a superfície do texto que exibe a pontuação
    score_surface = score_font.render('Score : ' + str(score), True, color)
    
    # Obtém o retângulo para posicionar o texto na tela
    score_rect = score_surface.get_rect()
    
    # Exibe o texto na janela do jogo
    game_window.blit(score_surface, score_rect)


def game_over():
    """
    Exibe a tela de fim de jogo com a pontuação final e encerra o programa.

    1. Cria um objeto de fonte (`my_font`) com a fonte 'times new roman' e tamanho 50 para o texto da tela de fim de jogo.
    2. Renderiza o texto "Your Score is : [pontuação]" em vermelho na superfície `game_over_surface`, onde [pontuação] é o valor da variável global `score`.
    3. Obtém um retângulo (`game_over_rect`) associado ao texto renderizado, para facilitar o posicionamento.
    4. Define a posição do texto para o centro superior da tela (metade da largura da janela e um quarto da altura).
    5. Exibe o texto na `game_window` usando o `blit` e atualiza a tela com `pygame.display.flip()`.
    6. Pausa o jogo por 2 segundos para que o jogador possa ver a mensagem final.
    7. Encerra a biblioteca PyGame com `pygame.quit()` e o programa com `quit()`.

    Variáveis Globais Utilizadas:

        score (int): A pontuação final do jogador, que será exibida no texto de fim de jogo.
        window_x (int): A largura da janela do jogo, usada para centralizar o texto horizontalmente.
        window_y (int): A altura da janela do jogo, usada para definir a posição do texto na parte superior central da tela.
        red (tuple): Uma tupla RGB que define a cor vermelha usada para o texto (ex: (255, 0, 0)).
        game_window (pygame.Surface): A superfície da janela do jogo onde o texto de fim de jogo será exibido.
    """
    # Cria um objeto de fonte com a fonte e tamanho especificados
    my_font = pygame.font.SysFont('times new roman', 50)
    
    # Cria a superfície de texto com a pontuação final do jogador
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    
    # Obtém o retângulo para posicionar o texto na tela
    game_over_rect = game_over_surface.get_rect()
    
    # Define a posição do texto para o centro superior da tela
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    
    # Exibe o texto de fim de jogo na janela
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    
    # Pausa o programa por 2 segundos
    time.sleep(2)
    
    # Encerra o PyGame e o programa
    pygame.quit()
    quit()


snake_speed = 10

# tamanho da janela 
window_x = 720
window_y = 480

# definindo as cores
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Inicializando o PyGame
pygame.init()

# Inicializando a janela 
pygame.display.set_caption('Jogo da cobrinha')
game_window = pygame.display.set_mode((window_x, window_y))

# Define a taxa de atualização do jogo
fps = pygame.time.Clock()

# definindo a posição inicial da cobra 
snake_position = [100, 50]

# corpo da cobra 
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# posição das frutas
fruit_position = [random.randrange(1, (window_x//10)) * 10, 
                  random.randrange(1, (window_y//10)) * 10]

fruit_spawn = True

# direção inicial para a qual a cobra vai andar 
# para a direita 
direction = 'RIGHT'
change_to = direction

#  score inicial 
score = 0

# Main Function
while True:
    # Lidando com eventos de teclado
    for event in pygame.event.get():  # Percorre todos os eventos que ocorrem
        if event.type == pygame.KEYDOWN:  # Verifica se uma tecla foi pressionada
            # Se a tecla pressionada foi a seta para cima, define a direção como 'UP'
            if event.key == pygame.K_UP:
                change_to = 'UP'
            # Se a tecla pressionada foi a seta para baixo, define a direção como 'DOWN'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            # Se a tecla pressionada foi a seta para a esquerda, define a direção como 'LEFT'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            # Se a tecla pressionada foi a seta para a direita, define a direção como 'RIGHT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Evita que a cobra se mova em duas direções simultaneamente e também impede que ela se mova diretamente na direção oposta
    # (por exemplo, se estiver indo para cima, não pode ir direto para baixo)
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Movendo a cobra com base na direção atual
    if direction == 'UP':
        snake_position[1] -= 10  # Move para cima (subtrai da posição y)
    if direction == 'DOWN':
        snake_position[1] += 10  # Move para baixo (adiciona à posição y)
    if direction == 'LEFT':
        snake_position[0] -= 10  # Move para a esquerda (subtrai da posição x)
    if direction == 'RIGHT':
        snake_position[0] += 10  # Move para a direita (adiciona à posição x)

    # A cobra anda a partir de um mecanismo no qual acrescentamos uma posição na cabeça e removemos uma posição ao final: 
    # Mecanismo de crescimento do corpo da cobra Se a cobra colidir com a fruta, a pontuação será incrementada em 10 pontos
    snake_body.insert(0, list(snake_position))  # Adiciona a nova posição da cabeça da cobra ao corpo
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10  # Incrementa a pontuação
        fruit_spawn = False  # Indica que uma nova fruta precisa ser gerada
    else:
        snake_body.pop()  # Remove a última posição da cobra se não houver colisão com a fruta

    # Se uma nova fruta precisa ser gerada
    if not fruit_spawn:
        # Gera uma nova posição aleatória para a fruta dentro da tela
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, 
                          random.randrange(1, (window_y // 10)) * 10]
        
    # Define a variável para indicar que a fruta está presente na tela
    fruit_spawn = True

    # Preenche a janela do jogo com a cor preta (limpa a tela)
    game_window.fill(black)

    # Desenha cada segmento do corpo da cobra na tela
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    
    # Desenha a fruta na nova posição
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))


    # Condições de Game Over

    # Verifica se a cobra colidiu com as bordas da janela
    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()  # Chama a função de fim de jogo se a cobra sair pela esquerda ou direita
    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()  # Chama a função de fim de jogo se a cobra sair pela parte superior ou inferior

    # Colisão com o próprio corpo da cobra
    # Verifica se a cabeça da cobra colidiu com qualquer segmento do corpo
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()  # Chama a função de fim de jogo se houver colisão com o corpo

    # Exibindo a pontuação continuamente
    show_score(white, 'times new roman', 20)

    # Atualiza a tela do jogo
    pygame.display.update()

    # Define a taxa de atualização (frames por segundo)
    fps.tick(snake_speed)  # Controla a velocidade do jogo com base na variável `snake_speed`

