import os

def perguntas():
    return input(
        "O que deseja realizar:\n" +
        "<I> - Para Inserir uma Despesa\n" +
        "<C> - Para somar as contas\n" +
        "<D> - Para inserir dinheiros\n" +
        "\n" +
        "Digite a opção: "
    ).upper()

def inserir_despesa(despesas):
    despesa = input("Digite a descrição da despesa: ").upper()
    Guardar = float(input("Digite o valor para guardar: "))
    Tim = float(input("Digite o valor da Tim: "))
    Fatura = float(input("Digite o valor da fatura do cartão: "))
    Roupa = float(input("Digite o valor de roupa/tenis: "))
    Icloud = float(input("Digite o valor do iCloud: "))
    Spotify = float(input("Digite o valor do Spotify: "))
    Cabeleleiro = float(input("Digite o valor do cabeleireiro: "))

    if despesa in despesas:
        # Atualiza os valores existentes
        despesas[despesa][1] += Guardar
        despesas[despesa][3] += Tim
        despesas[despesa][5] += Fatura
        despesas[despesa][7] += Roupa
        despesas[despesa][9] += Icloud
        despesas[despesa][11] += Spotify
        despesas[despesa][13] += Cabeleleiro
    else:
        # Cria uma nova entrada
        despesas[despesa] = [
            "Valor guardado", Guardar, 
            "Tim", Tim, 
            "Fatura do cartão", Fatura, 
            "Roupa/tenis", Roupa, 
            "iCloud", Icloud, 
            "Spotify", Spotify, 
            "Cabeleireiro", Cabeleleiro
        ]
    
    salvar(despesas)

def salvar(despesas):
    if not os.path.exists("Mes"):
        os.makedirs("Mes")
    
    with open("Mes/financeiro.txt", "a") as arquivo:
        chave = list(despesas.keys())[-1]
        valores = despesas[chave]
        arquivo.write(f"{chave}:\n")
        for i in range(0, len(valores), 2):
            arquivo.write(f"{valores[i]}: {valores[i + 1]}\n")
        arquivo.write("\n")

def soma_despesas(despesas):
    total = 0
    for valores in despesas.values():
        # Extraindo apenas os valores numéricos
        valores_numericos = [valores[i] for i in range(1, len(valores), 2) if isinstance(valores[i], (int, float))]
        total += sum(valores_numericos)
    return total

def remover_Despesas(despesas):
