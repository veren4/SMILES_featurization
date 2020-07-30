import pandas as pd
import re

subset = pd.read_table('../datasets/sets_from_Chris/canonical_smiles_first_100.txt', header=None)
subset = subset.drop_duplicates()          # throw out duplicates

subset = subset.rename(columns={0: "canonical_SMILES"})




total_SMILES = "".join(subset.canonical_SMILES)
alphabet = set([])

two_letter_elements = re.findall("[A-Z][a-z]", total_SMILES)
two_letter_elements = sorted(set(two_letter_elements))
periodic_table_2_letter = ['He',
                           'Li', 'Be', 'Ne',
                           'Na', 'Mg', 'Al', 'Si', 'Cl', 'Ar',
                           'Ca', 'Sc', 'Ti', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
                           'Rb', 'Sr', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'Xe',
                           'Cs', 'Ba', 'Hf', 'Ta', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
                           'Fr', 'Ra', 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og',
                           'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
                           'Ac', 'Th', 'Pa', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
for element in two_letter_elements:
    if element in periodic_table_2_letter:
        
        # Add the 2-letter elements which are in the periodic table
        alphabet.add(element)
        
        # Take the added 2-letter elements out of my search string (SMILES)
        total_SMILES = re.sub(element, "", total_SMILES)

one_letter_elements = re.findall("[A-Z]|[a-z]", total_SMILES)
one_letter_elements = sorted(set(one_letter_elements))
alphabet.update(one_letter_elements)
for element in one_letter_elements:    
    total_SMILES = re.sub(element, "", total_SMILES)         

rest = set(list(total_SMILES))
alphabet.update(rest)

with open("alphabet_result.txt", "w") as output_file:
    output_file.writelines(list(alphabet))
