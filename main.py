'''
Project: Implementações da cadeira de lógica para Ciência da Computação
@author: João Victor
Created: 25/04/2020
'''

from logic import *
from logic_function import *

def main():
    p = Atom("Está chovendo")
    q = Atom("A rua está molhada")
    r = Atom("Aqui é um teste")
    
    premise_1 = THEN(p, THEN(r, q))
    premise_2 = THEN(p, r)
    formula = THEN(p, q) 

    is_consequence, truth_table = logical_consequence(formula, [premise_1, premise_2])
    print(is_consequence)
    print_truth_table(truth_table)

if __name__ == "__main__":
    main()