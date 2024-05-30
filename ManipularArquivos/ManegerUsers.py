import sys
sys.path.append('../PROJETOS-EM-PYTHON')

from Dicionarios.funcao import *

despesas = {}

op = perguntas()

while op == "I" or op == "P" or op == "E" or op == "L":
    if op == "I":     
      inserir_despesa(despesas)   
      op = perguntas()     