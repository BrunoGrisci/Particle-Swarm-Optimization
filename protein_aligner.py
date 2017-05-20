#Bruno Iochins Grisci
#MAY/2017

import math
import numpy as np
import copy

from PSO import PSO
from pdb_reader import PDB_reader

def align(transformation, mob_atoms):
    translation = np.matrix([transformation[0:3]]*len(mob_atoms))
    rot = transformation[3:6]
    
    rotX = np.matrix([[1.0, 0.0, 0.0], [0.0, math.cos(rot[0]), -math.sin(rot[0])], [0.0, math.sin(rot[0]), math.cos(rot[0])]])
    rotY = np.matrix([[math.cos(rot[1]), 0.0, math.sin(rot[1])], [0.0, 1.0, 0.0], [-math.sin(rot[1]), 0.0, math.cos(rot[1])]])
    rotZ = np.matrix([[math.cos(rot[2]), -math.sin(rot[2]), 0.0], [math.sin(rot[2]), math.cos(rot[2]), 0.0], [0.0, 0.0, 1.0]])
    rotXYZ = rotZ * rotY * rotX

    transformed_atoms = np.matrix(copy.deepcopy(mob_atoms))
    transformed_atoms = transformed_atoms + translation
    transformed_atoms = transformed_atoms * rotXYZ.transpose()
   
    transformed_atoms = np.matrix.tolist(transformed_atoms)
    return transformed_atoms

def rmsd(transformation, ref_atoms, mob_atoms):
    trans_atoms = align(transformation, mob_atoms)
    distance_sum = 0.0
    for coord in zip(ref_atoms, trans_atoms):
        distance_sum += (coord[0][0] - coord[1][0])**2
        distance_sum += (coord[0][1] - coord[1][1])**2 
        distance_sum += (coord[0][2] - coord[1][2])**2  
    score = math.sqrt(distance_sum / float(len(ref_atoms)))
    return score

def evaluator(solutions, ref_atoms, mob_atoms):
    scores = []
    for solution in solutions:
        score = rmsd(solution, ref_atoms, mob_atoms)
        scores.append(score)
    return scores

pop_size = 200
dim = 6
iterations = 10000  
    
pdb_ref = PDB_reader("material/reference.pdb")
pdb_mob = PDB_reader("material/1ACW-01.pdb")

#print rmsd([], pdb_ref.get_all_pos(), pdb_mob.get_all_pos())

latest_best_scores = []
    
pso = PSO(swarm_size=pop_size, dimensions=dim, lower_bounds=[-100.0, -100.0, -100.0, 0.0, 0.0, 0.0], upper_bounds=[100.0, 100.0, 100.0, 2.0*math.pi, 2.0*math.pi, 2.0*math.pi], minimization=True)
for i in xrange(iterations):
    locations = pso.get_locations()
    scores = evaluator(locations, pdb_ref.get_ca_pos(), pdb_ref.get_ca_pos())
    pso.run_step(scores, 0.1)
print(pso.get_best_location())
print(pso.get_best_score())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
