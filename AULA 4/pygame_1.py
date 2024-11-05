import pygame
import sys

# Inicializa o PyGame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((800, 600))  # Largura x Altura
pygame.display.set_caption("Meu Primeiro Jogo com PyGame")

# Definir a cor da tela
background_color = (0, 0, 0)  # Preto

# Loop principal do jogo
while True:
    # Detecta eventos (como fechar a janela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preencher a tela com a cor de fundo
    screen.fill(background_color)

    # Atualiza a tela
    pygame.display.flip()