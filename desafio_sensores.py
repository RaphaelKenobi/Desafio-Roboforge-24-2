"""----------------------------------------------------Desafio Sensores-------------------------------------------------
1. Mova-se paralelamente à parede enquanto mantém uma distância fixa da mesma;
Caso encontre a cor vermelha no chão, faça uma curva de 90° e continue seguindo a
parede;

2. Caso encontre a cor vermelha no chão, faça uma curva de 90° e continue seguindo a
parede;

3. Caso encontre a cor amarela, espere que um usuário dê algum tipo de comando, e
então volte a rotina normal;

4. Enfim, se encontrar a cor verde, pare completamente.
"""

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.sensor import INPUT_1, INPUT_2
from ev3dev2.led import Leds
from time import sleep

# Configuração dos motores e sensores
motores = MoveTank(OUTPUT_A, OUTPUT_B)
sensor_cor = ColorSensor(INPUT_1)
sensor_distancia = UltrasonicSensor(INPUT_2)
leds = Leds()


def mover_para_frente():
    motores.on(SpeedPercent(30), SpeedPercent(30))


def virar_90_graus(direcao='direita'):
    if direcao == 'direita':
        motores.on_for_degrees(SpeedPercent(30), SpeedPercent(-30), 180)
    else:
        motores.on_for_degrees(SpeedPercent(-30), SpeedPercent(30), 180)


def parar():
    motores.off()


def esperar_comando_usuario():
    leds.set_color('LEFT', 'YELLOW')
    leds.set_color('RIGHT', 'YELLOW')
    input("Pressione Enter para continuar...")
    leds.set_color('LEFT', 'GREEN')
    leds.set_color('RIGHT', 'GREEN')


def manter_distancia_fixa(distancia_desejada):
    distancia_atual = sensor_distancia.distance_centimeters
    KP = 1.5
    erro = distancia_atual - distancia_desejada

    if abs(erro) > 2:
        correcao = KP * erro
        vel_esq = max(min(30 + correcao, 50), 10)
        vel_dir = max(min(30 - correcao, 50), 10)
        motores.on(SpeedPercent(vel_esq), SpeedPercent(vel_dir))
    else:
        mover_para_frente()


def rotina_principal():
    distancia_desejada = 20
    leds.set_color('LEFT', 'GREEN')
    leds.set_color('RIGHT', 'GREEN')

    while True:
        cor_detectada = sensor_cor.color
        distancia_atual = sensor_distancia.distance_centimeters


        if cor_detectada == ColorSensor.COLOR_RED:
            leds.set_color('LEFT', 'RED')
            leds.set_color('RIGHT', 'RED')
            virar_90_graus()
            sleep(1)  # Pausa após a curva
            leds.set_color('LEFT', 'GREEN')
            leds.set_color('RIGHT', 'GREEN')
        elif cor_detectada == ColorSensor.COLOR_YELLOW:
            parar()
            esperar_comando_usuario()
        elif cor_detectada == ColorSensor.COLOR_GREEN:
            leds.set_color('LEFT', 'GREEN')
            leds.set_color('RIGHT', 'GREEN')
            parar()
            break
        else:
            manter_distancia_fixa(distancia_desejada)


if __name__ == "__main__":
    try:
        rotina_principal()
    except KeyboardInterrupt:
        parar()
        leds.set_color('LEFT', 'BLACK')
        leds.set_color('RIGHT', 'BLACK')
"""----------------------------------------------------Desafio Sensores----------------------------------------------"""