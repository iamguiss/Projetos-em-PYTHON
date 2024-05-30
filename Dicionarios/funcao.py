def preencher_despesa(lista):
    resp = "S"
    while resp == "S":
        despesa = [
            input("Descrição: "),
            float(input("Valor: ")),
            input("Mês: "),
            input("Status: ")
        ]
        lista.append(despesa)
        resp = input("Digite \"S\" para continuar: ").upper()

def exibir_despesas(lista):
    for elemento in lista:
        print("Descrição.....:", elemento[0])
        print("Valor.........:", elemento[1])
        print("Mês...........:", elemento[2])
        print("Status........:", elemento[3])

def localizar_despesa(lista):
    busca = input("\nDigite a despesa que deseja localizar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Despesa..: ", elemento[0])
            print("Mês......: ", elemento[2])
            print("Status...: ", elemento[3])

def perguntas():
    return input(
        "O que deseja realizar:\n" +
        "<I> - Para Inserir uma Despesa\n" +
        "<P> - Para Pesquisar uma despesa\n" +
        "<E> - Para Excluir uma despesa\n" +
        "<L> - Para Listar todas as despesas\n" +
        "\n" +
        "Digite a opção: "
    ).upper()

def inserir_despesa(despesas):
   despesas[input("Digite a despesa: ").upper()] = [input("Digite a Descrição: ").upper(),
                                                         float(input("Digite o valor: ")), 
                                                         input("Digite a data: "), 
                                                         input("Digite o status: ").upper()]

def salvar(despesas):
    with open("bd.txt", "a") as arquivo:
        for chave, valor in despesas.items():
            arquivo.write(chave + ":" + str(valor))