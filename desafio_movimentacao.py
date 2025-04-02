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

ev3 = EV3Brick()
motor_esquerdo = Motor(Port.B)
motor_direito = Motor(Port.C)
""""
variaveis de duracao,velocidade etc, seriam passadas como argumentos para as funcoes de acordo com a necessidade
"""
def mover_para_frente(velocidade, duracao):
    motor_esquerdo.run(velocidade)
    motor_direito.run(velocidade)
    wait(duracao)

def virar_90_graus():
    motor_direito.stop()
    motor_esquerdo.run_time(speed=400, time=2000)

def desenhar_quadrado():
    for i in range(4):
        mover_para_frente(velocidade=200, duracao=3000)
        virar_90_graus()

if __name__ == "__main__":
    while True:
        desenhar_quadrado()
