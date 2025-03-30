"""----------------------------------------------------Desafio Movimentação-------------------------------------------------
Ao executar o código ao lado, o robô irá
fazer quadrados no chão para sempre:

Utilizando apenas os motores, o que você
faria para melhorar a lógica e a sintaxe
deste código?

"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Inicializa o EV3 e os motores
ev3 = EV3Brick()
motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)

def mover_para_frente(velocidade, duracao):
    """
    Move o robô para frente com a velocidade e duração especificadas.
    """
    motor_esquerdo.run(velocidade)
    motor_direito.run(velocidade)
    wait(duracao)

def virar_90_graus():
    """
    Faz o robô virar 90 graus à direita.
    """
    motor_direito.stop()
    motor_esquerdo.run_time(speed=400, time=2000)

def desenhar_quadrado():
    """
    Faz o robô desenhar um quadrado.
    """
    for _ in range(4):
        mover_para_frente(velocidade=200, duracao=3000)
        virar_90_graus()

if __name__ == "__main__":
    while True:
        desenhar_quadrado()
