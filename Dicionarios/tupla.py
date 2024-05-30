usuarios = {}
emails = ["teste@teste.com", "teste2@teste.com"]

tupla = list(enumerate(emails))

for chave in range(0,len(tupla)):
  print( "Email ", tupla[chave][1])
  usuarios[tupla[chave]] = [input("Digite o seu nome "), input("Dgite seu nível")]
  
for chave, dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...:", chave[0])
    print("Nome....:", chave[0])
    print("Nível...:", chave[1])