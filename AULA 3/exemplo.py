import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def update(frame):
    line.set_data(t[:frame], z[:frame])  # Mostrar o progresso até o frame atual
    return line,

# Gerando o gráfico 

# Parâmetros
z0 = 100  # posição inicial em metros
v0 = 0    # velocidade inicial em m/s
g = 9.8   # aceleração da gravidade em m/s^2
t_max = 5 # tempo máximo de simulação em segundos

# Gerar pontos no tempo
t = np.linspace(0, t_max, num=500)
# Calcular a posição ao longo do tempo para dois objetos
z = z0 + v0 * t - 0.5 * g * t**2

fig, ax = plt.subplots()
line, = ax.plot(t, z)

plt.xlabel('Tempo (s)')
plt.ylabel('Altura (m)')
plt.title('Queda livre sem resistência do ar')


ax.set_xlim((0, 5))       # Limites do eixo x (tempo)
ax.set_ylim((-20, 120))     # Limites do eixo y (altura)

ani = FuncAnimation(fig, update, frames=1000, interval=50)
plt.show()