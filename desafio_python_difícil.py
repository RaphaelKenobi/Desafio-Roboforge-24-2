"""----------------------------------------------------Nivel 2 difícil----------------------------------------------------

Desafio do Triângulo

Regras:
1. Calcular os lados do triângulo a partir de 3 pontos cartesianos
2. Calcular os ângulos internos
3. Calcular perímetro e área
4. Classificar quanto aos lados
5. Classificar quanto aos ângulos
"""

from math import sqrt, acos, degrees


def calcular_lados(pontos):
    a = sqrt((pontos[1][0] - pontos[2][0]) ** 2 + (pontos[1][1] - pontos[2][1]) ** 2)
    b = sqrt((pontos[0][0] - pontos[2][0]) ** 2 + (pontos[0][1] - pontos[2][1]) ** 2)
    c = sqrt((pontos[0][0] - pontos[1][0]) ** 2 + (pontos[0][1] - pontos[1][1]) ** 2)
    return a, b, c


def calcular_angulos(a, b, c):
    angulo_a = degrees(acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))
    angulo_b = degrees(acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))
    angulo_c = degrees(acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)))
    return angulo_a, angulo_b, angulo_c


def tipo_triangulo_lados(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or b == c or a == c:
        return "Isósceles"
    else:
        return "Escaleno"


def tipo_triangulo_angulos(angulos):
    if 90 in angulos:
        return "Retângulo"
    elif any(angulo > 90 for angulo in angulos):
        return "Obtusângulo"
    else:
        return "Acutângulo"


def calcular_perimetro(a, b, c):
    return a + b + c


def calcular_area(a, b, c):
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))


def main():
    pontos = []
    print("Digite as coordenadas dos 3 pontos (x,y):")
    for i in range(3):
        x = float(input(f"Ponto {i + 1} - x: "))
        y = float(input(f"Ponto {i + 1} - y: "))
        pontos.append((x, y))

    a, b, c = calcular_lados(pontos)
    print(f"\nLados do triângulo:")
    print(f"Lado a: {a:.2f}")
    print(f"Lado b: {b:.2f}")
    print(f"Lado c: {c:.2f}")

    angulo_a, angulo_b, angulo_c = calcular_angulos(a, b, c)
    print(f"\nÂngulos do triângulo:")
    print(f"Ângulo A: {angulo_a:.2f}°")
    print(f"Ângulo B: {angulo_b:.2f}°")
    print(f"Ângulo C: {angulo_c:.2f}°")

    print(f"\nPerímetro: {calcular_perimetro(a, b, c):.2f}")
    print(f"Área: {calcular_area(a, b, c):.2f}")

    print(f"\nTipo quanto aos lados: {tipo_triangulo_lados(a, b, c)}")
    print(f"Tipo quanto aos ângulos: {tipo_triangulo_angulos([angulo_a, angulo_b, angulo_c])}")


if __name__ == "__main__":
    main()
"""----------------------------------------------------Nivel 2 difícil-------------------------------------------------"""
