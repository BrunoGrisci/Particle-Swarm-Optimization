#Bruno Iochins Grisci
#MAY/2017

from cec2013.cec2013 import *
from PSO import PSO

###### Case 15: Composition Function 4 - Dimension 3 ######
dimension = 3
number_function = 15
min_val = -5
max_val = 5

pop_size = 200
iterations = 2000

def evaluator(solutions, scorefxn):
    scores = []
    for solution in solutions:
        score = scorefxn.evaluate(solution)
        scores.append(score)
    return scores
    
###################################################################

scorefxn = CEC2013(number_function) # inicializando a funcao de fitness
pso = PSO(swarm_size=pop_size, dimensions=dimension, lower_bounds=-5.0, upper_bounds=5.0, minimization=False)

#Start the regular loop 
for i in xrange(iterations):
    locations = pso.get_locations()
    scores = evaluator(locations, scorefxn)
    pso.run_step(scores)
print(pso.get_best_location())
print(pso.get_best_score())
print("Finished run")

