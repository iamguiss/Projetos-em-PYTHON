import json
# - Criando arquivo , usando o W cria um novo arquivo-
# arquivo = open("primeiro_arquivo.txt", "w" )

# arquivo.write("Primeiro teste")

# arquivo.close()
# ----------------------------------------------- #


# -------------------------------------------------------------- #
# - Criando novo arquivo , usando A ele inseri um novo arquivo -
# with open ("primeiro_arquivo.txt" , "a") as arquivo:
#   arquivo.write("\nTeste bomba")
# -------------------------------------------------------------- #
 
 
# -------------------------------------------------------------- # 
# lendo as arquivos com head e headlines

# with open("primeiro_arquivo.txt", "r") as arquivo:
#   conteudo = arquivo.read()
#   for linha in arquivo.read():
#     print (linha)
    
# with open("primeiro_arquivo.txt", "r") as arquivo:
#   conteudo = arquivo.readline()
#   for linha in arquivo.readlines():
#     print (linha)

# -------------------------------------------------------------- #
# lendo arquivo JSON com "R"
# with open("bd.json", "r") as arq_json:
#     dic = json.load(arq_json)
#     for chave, dados in dic.items():
#         print(chave + " " + str(dados))

# -------------------------------------------------------------- 

# Criando json
dic = {
    "chaves":["chave do 8", "14/07/2014", "Entrou"],
    "quico":["quico", "15/07/2014", "Saiu"]
}
with open("bd1,json", "w") as json_file:
    json.dump(dic, json_file)