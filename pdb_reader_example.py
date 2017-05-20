#Bruno Iochins Grisci
#MAY/2017
#This code is a usage example of the PDB_reader class

from pdb_reader import PDB_reader

pdb_ref = PDB_reader("material/reference.pdb")
pdb_mob = PDB_reader("material/1ACW-01.pdb")
print(len(pdb_ref.get_atoms()), len(pdb_mob.get_atoms()))
print(len(pdb_ref.get_all_pos()), len(pdb_mob.get_all_pos()))
print(len(pdb_ref.get_backbone_pos()), len(pdb_mob.get_backbone_pos()))
print(len(pdb_ref.get_ca_pos()), len(pdb_mob.get_ca_pos()))

print(pdb_ref.get_ca_pos())
print(pdb_mob.get_ca_pos())
print(pdb_ref.get_atoms())
