#Bruno Iochins Grisci
#MAY/2017
#Usage: python protein_aligner.py reference_file mobile_file atoms_type

import math
import numpy as np
import copy
import sys

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

reference_file = sys.argv[1]
mobile_file = sys.argv[2]
atoms = sys.argv[3]

pop_size = 200
dim = 6
min_iterations = 1000
initial_lr = 1.0
lr = initial_lr
    
pdb_ref = PDB_reader(reference_file)
pdb_mob = PDB_reader(mobile_file)

pdb_mob.match_atoms(pdb_ref.get_atoms(), pdb_ref.get_amino_acids_index())
pdb_mob.remove_nones()    
pdb_ref.match_atoms(pdb_mob.get_atoms(), pdb_mob.get_amino_acids_index())
pdb_ref.remove_nones() 

latest_best_scores = []
    
pso = PSO(swarm_size=pop_size, dimensions=dim, lower_bounds=[-100.0, -100.0, -100.0, 0.0, 0.0, 0.0], upper_bounds=[100.0, 100.0, 100.0, 2.0*math.pi, 2.0*math.pi, 2.0*math.pi], movement_step=initial_lr, minimization=True)

#Start with regular loop 
for i in xrange(min_iterations):
    locations = pso.get_locations()
    if atoms == "ca":
        scores = evaluator(locations, pdb_ref.get_ca_pos(), pdb_mob.get_ca_pos())
    elif atoms == "backbone":
        scores = evaluator(locations, pdb_ref.get_backbone_pos(), pdb_mob.get_backbone_pos())
    elif atoms == "all":
        scores = evaluator(locations, pdb_ref.get_all_pos(), pdb_mob.get_all_pos())
    pso.run_step(scores, initial_lr)
print(pso.get_best_location())
print(pso.get_best_score())
print("Finished first run")

#Try to optimize the initial best solution reducing the "learning" or movement rate
little_i = 0    
while lr >= initial_lr/16.0:
    locations = pso.get_locations()
    if atoms == "ca":
        scores = evaluator(locations, pdb_ref.get_ca_pos(), pdb_mob.get_ca_pos())
    elif atoms == "backbone":
        scores = evaluator(locations, pdb_ref.get_backbone_pos(), pdb_mob.get_backbone_pos())
    elif atoms == "all":
        scores = evaluator(locations, pdb_ref.get_all_pos(), pdb_mob.get_all_pos())
    pso.run_step(scores, lr)
    
    latest_best_scores.append(pso.get_best_score())
    if len(latest_best_scores) > 100:
        latest_best_scores.pop(0)
        
    if little_i > 101:
        improvement = (latest_best_scores[0] - latest_best_scores[-1])/latest_best_scores[0]
        if improvement < 0.01 and lr >= initial_lr/16.0:
            print(little_i, lr) 
            print(pso.get_best_score())
            lr = lr/2.0
            latest_best_scores = []
            little_i = 0
    
    little_i += 1
    
print(pso.get_best_location())
print(pso.get_best_score())
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
