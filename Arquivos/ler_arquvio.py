arquivo = open("primeiro_arquivo.txt", "w" )

arquivo.write("Meu primeiro arquivo! Ai que festa")

arquivo.close()

with open ("primeiro_arquivo.txt" , "a") as arquivo:
  arquivo.write("\nTeste bomba")