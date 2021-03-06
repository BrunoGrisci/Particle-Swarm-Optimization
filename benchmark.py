#Bruno Iochins Grisci
#MAY/2017

import os
import time
import numpy as np
import matplotlib.pyplot as plt

from cec2013.cec2013 import *
from PSO import PSO

###### Case 15: Composition Function 4 - Dimension 3 ######
dimension = 3
number_function = 15
min_val = -5
max_val = 5

pop_size = 200
iterations = 600
runs = 30

animation = False
analysys = True

def save_file(solutions, scores, run, iteration):
    filename = 'animation/' + str(run) + '/step' + str(iteration) + '.dat'
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(filename, "w") as f:
        for i in xrange(len(solutions)):
            line = str(solutions[i][0]) + ', ' + str(solutions[i][1]) + ', ' + str(solutions[i][2]) + ', ' + str(scores[i]) + '\n'
            f.write(line)
        f.close()
    
def evaluator(solutions, scorefxn):
    scores = []
    for solution in solutions:
        score = scorefxn.evaluate(solution)
        scores.append(score)
    return scores
    
###################################################################

scorefxn = CEC2013(number_function) # inicializando a funcao de fitness

runscore = []
runscore_star = []
runtime = []
for r in xrange(runs):
    #Start the regular loop
    time0 = time.time()
    best_scores = []
    pso = PSO(swarm_size=pop_size, dimensions=dimension, lower_bounds=-5.0, upper_bounds=5.0, movement_step=1.0, minimization=False)     
    
    for i in xrange(iterations): 
        locations = pso.get_locations()
        scores = evaluator(locations, scorefxn)
        
        if animation:
            save_file(locations, scores, r, i)
        
        pso.run_step(scores)
        best_scores.append(pso.get_best_score())
        
    time1 = time.time()
    timeT = time1 - time0
    runtime.append(timeT)    
    runscore.append(best_scores)
    runscore_star.append(pso.get_best_score())
    print(pso.get_best_location())
    print(pso.get_best_score())
    print(timeT)
    del pso
    print("Finished run " + str(r))
    
print(runscore)
print(runtime)
print(runscore_star)

if analysys:
    average_score = sum(runscore_star) / float(len(runscore_star))
    std_score = np.std(runscore_star)
    average_time = sum(runtime) / float(len(runtime))
    std_time = np.std(runtime)
    print("Average score: " + str(average_score) + ' (' + str(std_score) + ')')
    print("Average time: " + str(average_time) + ' (' + str(std_time) + ')')
    print("Best score: " + str(max(runscore_star)))
    print("Worst score: " + str(min(runscore_star)))

    for r in runscore:
        plt.plot(r)
    plt.xlabel('Iteration')
    plt.ylabel('Score')
    plt.show()    

