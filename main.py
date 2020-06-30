'''
Project: Implementações da cadeira de lógica para Ciência da Computação
@author: João Victor
Created: 25/04/2020
'''

from logic import *
from logic_function import *

def main():
    p = Atom("Está chovendo", True)
    q = Atom("A rua está molhada", True)
    r = Atom("Aqui é um teste")
    s = Atom("Aqui é outro teste")
    p1 = Atom("Aqui é mais um teste")

    p_q = AND(p, q)
    not_p_q = NOT(p_q)

    truth_table = truth_table_generator(not_p_q)

    print_truth_table(truth_table)

if __name__ == "__main__":
    main()