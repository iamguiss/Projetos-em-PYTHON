# - Criando arquivo , usando o W cria um novo arquivo-
# arquivo = open("primeiro_arquivo.txt", "w" )

# arquivo.write("Primeiro teste")

# arquivo.close()
# ----------------------------------------------- #


# -------------------------------------------------------------- #
# - Criando novo arquivo , usnado A ele inseri um novo arquivo -
# with open ("primeiro_arquivo.txt" , "a") as arquivo:
#   arquivo.write("\nTeste bomba")
# -------------------------------------------------------------- #
 
  
with open("primeiro_arquivo.txt", "r") as arquivo:
  conteudo = arquivo.readline()
  for linha in arquivo.readlines():
    print (linha)