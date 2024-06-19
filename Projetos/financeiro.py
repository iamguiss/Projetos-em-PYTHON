import sys
sys.path.append('../PROJETOS-EM-PYTHON')

from Dicionarios.funcaoFinanceiro import *

despesas = {}

op = perguntas()

while op == "I" or op == "C":
    if op == "I":     
      inserir_despesa(despesas)   
      op = perguntas()    
    elif op ==  "C":
      total = soma_despesas(despesas)
      print(f"somar dos valores é {total}")
      op = perguntas()
     
    