"""----------------------------------------------------Nivel 0 fácil----------------------------------------------------

Desafio FizzBuzz

Regras:
1. Escreva uma função que receba um número.
2. Se o número for divisível por 3, retorna "Fizz"
3. Se o número for divisível por 5, retorna "Buzz"
4. Se o número for divisível por 3 e por 5, retorna "FizzBuzz"
5. Se não for divisível por nenhum dos dois, retorna "#"
"""

def fizz_buzz(numero: int) -> str:
    """
    Implementa a lógica do FizzBuzz para um número dado.

    Args:
        numero (int): Número inteiro a ser verificado

    Returns:
        str: "FizzBuzz" se divisível por 3 e 5
             "Fizz" se divisível por 3
             "Buzz" se divisível por 5
             "#" se não for divisível por 3 nem por 5
    """

    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"

    elif numero % 3 == 0:
        return "Fizz"

    elif numero % 5 == 0:
        return "Buzz"

    else:
        return "#"

if __name__ == "__main__":


    while True:
        try:
            print("=== Desafio FizzBuzz ===")
            print("Digite números para verificar (Ctrl+D para sair)")
            numero = int(input("\nDigite um número: "))
            resultado = fizz_buzz(numero)
            print(f"Resultado: {resultado}")

        except ValueError:
            print("Por favor, digite um número inteiro válido!")

        except EOFError:
            print("\nPrograma finalizado!")
            break

"""----------------------------------------------------Nivel 0 fácil-------------------------------------------------"""
