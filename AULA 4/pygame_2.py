import pygame
import sys

# Inicializa o PyGame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((800, 600))  # largura x altura
pygame.display.set_caption("Tutorial PyGame - Movimentação e Formas")

# Cores
background_color = (0, 0, 0)  # Preto
blue = (0, 0, 255)            # Azul para o retângulo

# Posição inicial do retângulo e velocidade de movimento
rect_x = 50
rect_y = 50
speed = 5

# Loop principal do jogo
running = True
while running:
    # Detecta eventos, incluindo o fechamento da janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Controle de movimentação com as setas do teclado
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect_x > 0: # Limita a movimentação à tela
        rect_x -= speed
    if keys[pygame.K_RIGHT] and rect_x < 700:
        rect_x += speed
    if keys[pygame.K_UP] and rect_y > 0:
        rect_y -= speed
    if keys[pygame.K_DOWN] and rect_y < 550:
        rect_y += speed

    # Preencher a tela com a cor de fundo
    screen.fill(background_color)

    # Desenha o retângulo azul na posição atualizada
    pygame.draw.rect(screen, blue, (rect_x, rect_y, 100, 50))

    # Atualiza a tela para exibir as mudanças
    pygame.display.flip()

    # Define a taxa de atualização do jogo
    pygame.time.Clock().tick(30)  # 30 FPS

# Encerra o PyGame
pygame.quit()
sys.exit()
