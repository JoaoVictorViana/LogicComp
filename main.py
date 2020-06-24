'''
Project: Implementações da cadeira de lógica para Ciência da Computação
@author: João Victor
Created: 25/04/2020
'''

from logic import *
from logic_function import *

def main():
    p = Atom("Está chovendo")
    q = Atom("A rua está molhado")
    r = Atom("Aqui é um teste")
    #p.value = True
    #q.value = False
    p_and_q = THEN(p, q)
    not_p_and_q = NOT(p_and_q)
    
    truth_table_generator(not_p_and_q)

if __name__ == "__main__":
    main()