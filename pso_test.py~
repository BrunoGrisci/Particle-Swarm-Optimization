#Bruno Iochins Grisci
#MAY/2017
#This code is a usage example of the PSO class

from PSO import PSO

pop_size = 10
d = 3
iterations = 200

def evaluator(locations):
    scores = []
    for l in locations:
        s = sum(l)
        scores.append(s)
    return scores

pso = PSO(swarm_size=pop_size, dimensions=d, lower_bounds=0, upper_bounds=1, minimization=False)
for i in xrange(iterations):
    locations = pso.get_locations()
    scores = evaluator(locations)
    pso.run_step(scores)
    print(pso.get_best_location())
    print(pso.get_best_score())

    
