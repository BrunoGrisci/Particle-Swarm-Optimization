#Bruno Iochins Grisci
#MAY/2017
#This code gets the atoms positions from a .pdb file

import copy

class PDB_reader:

    ATOM_TAG = "ATOM"
    END_TAG = "TER"
    ALPHA_CARBON = "CA"
    BACKBONE_ATOMS = ("N", "CA", "C", "O")
    
    file_name = ""
    atoms = []
    atoms_pos = []
    amino_acids_number = []
    
    def __init__(self, file_name):
        self.file_name = file_name
        self.read_pdb()
        
    def read_pdb(self):
    
        self.atoms = []
        self.atoms_pos = []
        self.amino_acids_number = []
    
        stop = False
        pdb = open(self.file_name, "r")
        
        while not stop:
            line = pdb.readline()
            if not line:
                stop = True
            else:
                line = line.split()
                if line[0] == self.END_TAG:
                    stop = True
                elif line[0] == self.ATOM_TAG:
                    atom = line[2]
                    if self.is_number(line[4]):
                        amino_acid = int(line[4])
                    elif self.is_number(line[5]):
                        amino_acid = int(line[5])
                    pos_init = 0
                    for i in xrange(len(line)):
                        if "." in line[i]:
                            pos_init = i
                            break
                    pos  = map(float, line[pos_init:pos_init+3])
                    self.atoms.append(atom)
                    self.atoms_pos.append(pos)
                    self.amino_acids_number.append(amino_acid)                  
        pdb.close()
    
    def get_atoms(self):
        return copy.deepcopy(self.atoms)
        
    def get_amino_acids(self):
        return copy.deepcopy(self.amino_acids_number)
        
    def get_all_pos(self):
        return copy.deepcopy(self.atoms_pos)
    
    def get_backbone_pos(self):
        backbone_pos = []
        for a in xrange(len(self.atoms)):
            if self.atoms[a] in self.BACKBONE_ATOMS:
                backbone_pos.append(self.atoms_pos[a])
        return copy.deepcopy(backbone_pos) 
        
    def get_ca_pos(self):
        ca_pos = []
        for a in xrange(len(self.atoms)):
            if self.atoms[a] == self.ALPHA_CARBON:
                ca_pos.append(self.atoms_pos[a])
        return copy.deepcopy(ca_pos)
        
    def match_atoms(self, ref_atoms, ref_amino_acids):
        aux_atoms = []
        aux_pos = []
        aux_aa = []
        for a in xrange(len(ref_atoms)):  
            #print(ref_atoms[a], ref_amino_acids[a])      
            if (ref_atoms[a], ref_amino_acids[a]) in zip(self.atoms, self.amino_acids_number):
                i = zip(self.atoms, self.amino_acids_number).index((ref_atoms[a], ref_amino_acids[a]))
                aux_atoms.append(self.atoms.pop(i))
                aux_pos.append(self.atoms_pos.pop(i))
                aux_aa.append(self.amino_acids_number.pop(i))
            else:
                aux_atoms.append(None)
                aux_pos.append(None)
                aux_aa.append(None)
                #print(ref_atoms[a])
        #print(zip(self.atoms, self.amino_acids_number))
        self.atoms = copy.deepcopy(aux_atoms)
        self.atoms_pos = copy.deepcopy(aux_pos)
        self.amino_acids_number = copy.deepcopy(aux_aa)
        
    def is_number(self, s):
        try:
            int(s)
            return True
        except ValueError:
            return False
                
                
       
    
