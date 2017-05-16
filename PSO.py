#Bruno Iochins Grisci
#05/2017

import random
import numpy as np
import sys
import copy

class PSO:

    minimization = False # If false minimizes, if True maximizes

    swarm_size = 0 # Number of particles to be used.
    dimensions = 0 # Number of dimensions of each particle.
    number_informants = 0 # Number of particles to take into account.
    
    lower_bounds = [] # List -> dimensions x 1
    upper_bounds = [] # List -> dimensions x 1 
    
    movement_step = 0 # How fast the particle moves. If movement_step is large, the particles make big jumps towards the better areas—and can jump over them by accident. Thus a big movement_step allows the system to move quickly to best-known regions, but makes it hard to do fine-grained optimization. Just like in hill-climbing. Most commonly, movement_step is set to 1.
    
    momentum_coef = 0 # How much of the original velocity is retained.
    personal_coef = 0 # How much of the personal best is mixed in. If personal_coef is large, particles tend to move more towards their own personal bests rather than towards global bests. This breaks the swarm into a lot of separate hill-climbers rather than a joint searcher.
    informant_coef = 0 # How much of the informants’ best is mixed in. The effect here may be a mid-ground between personal_coef and global_coef. The number of informants is also a factor (assuming they’re picked at random): more informants is more like the global best and less like the particle’s local best.
    global_coef = 0 # How much of the global best is mixed in. If global_coef is large, particles tend to move more towards the best known region. This converts the algorithm into one large hill-climber rather than separate hill-climbers. Perhaps because this threatens to make the system highly exploitative, global_coef is often set to 0 in modern implementations.
    
    swarm_location = [] # List of lists: swarm_size x dimensions -> location of each particle
    swarm_velocity = [] # List of lists: swarm_size x dimensions -> velocity of each particle
    swarm_score = []    # List: swarm_size x 1 -> score of each particle
    
    swarm_best_location = [] # List of lists: swarm_size x dimensions -> best location found for each particle at any moment
    swarm_best_score = [] # List: swarm_size x 1 -> best score found for each particle at any moment
    
    best_location = [] # List: 1 x dimensions -> best location found globaly at any moment 
    best_score = None # Number -> best score found globaly at any moment
    
    def __init__(self):
        if not self.lower_bounds:
            for i in xrange(self.dimensions):
                self.lower_bounds.append(sys.float_info.min)
        if not self.upper_bounds:
            for i in xrange(self.dimensions):
                self.upper_bounds.append(sys.float_info.max)
        #blablabla
        self.create_swarm()
        
    def create_swarm(self):
        for p in xrange(self.swarm_size):
            new_location = []
            new_velocity = []
            for d in xrange(self.dimensions):
                lb = self.lower_bounds[d]
                ub = self.upper_bounds[d] 
                l = random.uniform(lb, ub)
                d = random.uniform(lb, ub)
                v = (d - l) / 2.0
                new_location.append(l)
                new_velocity.append(v)
            self.swarm_location.append(new_location)
            self.swarm_velocity.append(new_velocity)
    
    
    def update_scores(self, scores):
        self.swarm_score = copy.deepcopy(scores)
        
    def update_velocity(self):
        pass    
            
    def update_location(self):
        pass
            
    def update_best(self):
        for p in xrange(self.swarm_size):
            if self.is_better(self.swarm_score[p], self.swarm_best_score[p]):
                self.swarm_best_score[p] = self.swarm_score[p]
                self.swarm_best_location[p] = copy.deepcopy(self.swarm_location[p])
                if self.is_better(self.swarm_score[p], self.best_score):
                    self.best_score = self.swarm_score[p]
                    self.best_location = copy.deepcopy(self.swarm_location[p])
        
    def is_better(self, x, y):
        if self.minimization:
            return x < y
        else:
            return x > y
        
            
