from cec2013.cec2013 import *
import random 

# Sao 20 casos distintos. Abaixo segue 4 funcoes que usei para testes, mas ha outras 16 opcoes.
# Importante notar que cada caso possui dimensoes e intervalos diferentes.
# Todas as informacoes estao contidas no relatorio em pdf.

###### Case 20: Composition Function 4 - Dimension 20 ######
dimensao = 20
number_function = 20
min_val = -5
max_val = 5

###### Case 19: Composition Function 4 - Dimension 10 ######
#dimensao = 10
#number_function = 19
#min_val = -5
#max_val = 5

###### Case 18: Composition Function 3 - Dimension 10 ######
#dimensao = 10
#number_function = 18
#min_val = -5
#max_val = 5

###### Case 8: Shubert - Dimension 3 ######
# dimensao = 3
# number_function = 8
# min_val = -10
# max_val = 10

def criarIndividuo(scorefxn):
    global min_val
    global max_val
    global dimensao
    values = []
    for i in range(dimensao): # escolhendo valores aleatorios dentro do intervalo da funcao
        values.append(round(random.uniform(min_val, max_val), 5))
    score = scorefxn.evaluate(values) # avaliando o individuo
    return [values, score]
    
###################################################################

scorefxn = CEC2013(number_function) # inicializando a funcao de fitness
individuo = criarIndividuo(scorefxn) # criando um individuo
print "Individuo:", individuo[0]
print "Fitness:", individuo[1]

