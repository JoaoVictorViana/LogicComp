from logic.logic import Atom, THEN
from logic.logic_function import logical_consequence, print_truth_table

def question_1():
    p = Atom("P")
    q = Atom("Q")
    r = Atom("R")

    premise = THEN(p, THEN(q, r))
    formula = THEN(p, THEN(r, p))

    is_consequence, truth_table = logical_consequence(formula, [premise])

    print(is_consequence)
    print_truth_table(truth_table)

question_1()
