"""----------------------------------------------------Nivel 1 médio----------------------------------------------------

Desafio Números Primos

Regras:
1. Escreva uma função que recebe um número e retorna True se ele for primo e
False se não for primo.
2. Criar função que verifica se um número é primo
3. Criar função que gera lista de 10 números aleatórios ou permite entrada manual
4. Multiplicar todos os números primos da lista
"""

from random import randint

def is_primo(numero):
    """
    Verifica se um número é primo.

    Returns:
        bool: True se o número for primo, False caso contrário
    """
    if numero < 2:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def gerar_lista_numeros():
    """
    Gera uma lista de 10 números aleatórios entre 1 e 100.

    Returns:
        list: Lista com 10 números aleatórios
    """
    return [randint(1, 100) for _ in range(10)]

def criar_lista_manual():
    """
    Permite ao usuário criar uma lista de 10 números manualmente.

    Returns:
        list: Lista com 10 números inseridos pelo usuário
    """
    numeros = []
    print("\nDigite 10 números inteiros:")
    
    while len(numeros) < 10:
        try:
            num = int(input(f"Digite o {len(numeros) + 1}º número: "))
            numeros.append(num)
        except ValueError:
            print("Por favor, digite um número inteiro válido!")
    
    return numeros

def multiplicar_primos(numeros):
    """
    Multiplica todos os números primos da lista.

    Args:
        numeros: Lista de números para verificar

    Returns:
        int: Produto dos números primos encontrados

    Raises:
        ValueError: Se não houver números primos na lista
    """
    primos = [num for num in numeros if is_primo(num)]
    if not primos:
        raise ValueError("Nenhum número primo encontrado na lista!")

    resultado = 1
    for primo in primos:
        resultado *= primo
    return resultado

def validar_numero():
    """
    Valida se um único número digitado pelo usuário é primo.

    Returns:
        None
    """
    try:
        numero = int(input("\nDigite um número para verificar se é primo: "))
        if is_primo(numero):
            print(f"\nO número {numero} É primo!")
        else:
            print(f"\nO número {numero} NÃO é primo!")
    except ValueError:
        print("Por favor, digite um número inteiro válido!")

if __name__ == "__main__":

    
    while True:
        try:
            print("=== Desafio Números Primos ===")
            print("Digite números para verificar (Ctrl+D para sair)")
            print("\nEscolha uma opção:")
            print("1 - Gerar lista automática")
            print("2 - Criar lista manualmente")
            print("3 - Verificar se um número é primo")
            
            opcao = input("\nOpção (1, 2 ou 3): ")

            if opcao not in ['1', '2', '3']:
                print("Opção inválida! Escolha 1, 2 ou 3.")
                continue

            if opcao == '3':
                validar_numero()
            else:
                numeros = gerar_lista_numeros() if opcao == '1' else criar_lista_manual()
                print(f"\nLista de números: {numeros}")

                primos = [num for num in numeros if is_primo(num)]
                print(f"Números primos encontrados: {primos}")

                resultado = multiplicar_primos(numeros)
                print(f"Produto dos números primos: {resultado}")

        except ValueError as e:
            print(f"Erro: {e}")
        except EOFError:
            print("\nPrograma finalizado!")
            break

"""----------------------------------------------------Nivel 1 médio-------------------------------------------------"""