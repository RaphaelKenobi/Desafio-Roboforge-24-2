"""----------------------------------------------------Nivel 3 INSANO!----------------------------------------------------

Desafio de Codificação de Tipos

Regras:
1. Crie uma variável que receba os dados que você digitar e mostre o tipo dela na
    tela. Ex: você digita "2" e retorna que é int,"casa" e retorna que é string.
2. Printe na tela o tipo e a variável.
3. Crie uma lista que recebe os dados que você digitar e printe na tela.
4. Crie uma função que codifica essa lista em uma string EXATAMENTE nesse formato:
"(str: 'casa'), (float: 3.14,) list(str: 'Roboforge',bool: True]" e mostre na tela.
5. Crie uma função que decodifique e mostre na tela.

"""

def identificar_tipo(entrada):
    """
    Identifica o tipo de uma entrada e tenta convertê-la para o tipo mais apropriado
    """
    # Tenta converter para diferentes tipos em ordem
    try:
        # Tenta converter para int
        valor = int(entrada)
        return valor, 'int'
    except ValueError:
        try:
            # Tenta converter para float
            valor = float(entrada)
            return valor, 'float'
        except ValueError:
            # Verifica se é booleano
            if entrada.lower() in ['true', 'false']:
                valor = entrada.lower() == 'true'
                return valor, 'bool'
            # Se não for número nem booleano, é string
            return entrada, 'str'

def criar_lista_dados():
    """
    Cria uma lista com dados digitados pelo usuário
    """
    dados = []
    print("\nDigite os valores (Ctrl+D para finalizar):")
    
    while True:
        try:
            entrada = input("Digite um valor: ")
            valor, tipo = identificar_tipo(entrada)
            dados.append((valor, tipo))
            print(f"Tipo identificado: {tipo}, Valor: {valor}")
        except EOFError:
            break
    
    return dados

def codificar_lista(dados):
    """
    Codifica a lista de dados no formato especificado
    """
    partes = []
    for valor, tipo in dados:
        if tipo == 'str':
            parte = f"(str: '{valor}')"
        elif tipo == 'float':
            parte = f"(float: {valor})"
        elif tipo == 'bool':
            parte = f"(bool: {valor})"
        else:
            parte = f"(int: {valor})"
        partes.append(parte)
    
    return ", ".join(partes)

def decodificar_string(texto_codificado):
    """
    Decodifica a string formatada de volta para uma lista de tuplas (valor, tipo)
    """
    dados = []
    # Remove os colchetes e divide por vírgula
    partes = texto_codificado.split("), ")
    
    for parte in partes:
        # Limpa a formatação
        parte = parte.strip("()[]")
        if ': ' not in parte:
            raise ValueError("Formato inválido. Esperado '(tipo: valor)'.")

        tipo, valor = parte.split(": ", 1)
        
        # Converte o valor de acordo com o tipo
        if tipo == 'str':
            valor = valor.strip("'")
        elif tipo == 'float':
            valor = float(valor)
        elif tipo == 'bool':
            valor = valor == 'True'
        else:
            valor = int(valor)
            
        dados.append((valor, tipo))
    
    return dados

if __name__ == "__main__":

    while True:
        try:
            print("=== Codificador/Decodificador de Tipos ===")
            print("Digite Ctrl+D para sair a qualquer momento.")
            print("\nEscolha uma opção:")
            print("1 - Decodificar um tipo de variavel")
            print("2 - Criar nova lista de dados")
            print("3 - Sair")
            
            opcao = input("\nOpção (1, 2 ou 3): ")
            
            if opcao == "1":
                # Criar e codificar lista
                dados = criar_lista_dados()
                if dados:
                    print("\nLista criada:")
                    for valor, tipo in dados:
                        print(f"Valor: {valor}, Tipo: {tipo}")
                    
                    texto_codificado = codificar_lista(dados)
                    print("\nLista codificada:")
                    print(texto_codificado)
                    
            elif opcao == "2":
                # Decodificar string
                texto = input("\nDigite a string codificada: ")
                try:
                    dados_decodificados = decodificar_string(texto)
                    print("\nDados decodificados:")
                    for valor, tipo in dados_decodificados:
                        print(f"Valor: {valor}, Tipo: {tipo}")
                except ValueError as e:
                    print(f"Erro ao decodificar: {e}")
                    
            elif opcao == "3":
                print("\nPrograma finalizado!")
                break
                
            else:
                print("Opção inválida! Escolha 1, 2 ou 3.")
                
        except EOFError:
            print("\nPrograma finalizado!")
            break

"""----------------------------------------------------Nivel 3 INSANO!-------------------------------------------------"""
