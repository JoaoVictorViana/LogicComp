from logic.logic import *
from logic.logic_function import *

def question_2():
    print("Questão 2")

    p = Atom('p')
    q = Atom('q')

    formula = NOT(THEN(q, NOT(p)))

    print(repr(formula))
    print(count_conec(formula))

def question_7():
    print("Questão 7")

    p = Atom('p')
    q = Atom('q')
    r = Atom('r')

    formula = THEN(OR(q, NOT(r)), NOT(p))

    print(repr(formula))
    print(get_atoms(formula))

def main():
    question_2()
    question_7()

    
if __name__ == "__main__":
    main()