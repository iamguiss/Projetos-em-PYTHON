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

def exibir_despesas(despesas):
    for elemento in despesas:
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
        "<C> - Para somar as contas\n" +
        "\n" +
        "Digite a opção: "
    ).upper()

def inserir_despesa(despesas):
    despesa = input("Digite a despesa: ").upper()
    descricao = input("Digite a Descrição: ").upper()
    valor = float(input("Digite o valor: "))
    data = input("Digite a data: ")
    status = input("Digite o status: ").upper()

    despesas[despesa] = [descricao, valor, data, status]
    salvar(despesas)


def salvar(despesas):
    with open("banco.txt", "w") as arquivo:
        for chave, valor in despesas.items():
            arquivo.write(chave + ":" + str(valor)+"\n")

def ver(despesas):
    with open("banco.json", "r") as arquivo:
        despesas = arquivo.readline()
        for linha in arquivo.readlines():
         print (linha)

