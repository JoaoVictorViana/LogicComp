'''
Project: Implementações da cadeira de lógica para Ciência da Computação
@author: João Victor
Created: 24/06/2020
'''

''' Functions of Logic '''
from logic.logic_utils import Utils, FormulaArgumentError
from logic.logic import Atom, AND, NOT
import collections


def logical_consequence(formula, premises):
    Utils.verified_propositions(formula)
    if not isinstance(premises, list):
        raise FormulaArgumentError
    for index, premise in enumerate(premises):
        set_formula = AND(set_formula, premise) if index else premises[0]
    return not satisfiability_checking(AND(set_formula, NOT(formula)))

def satisfiability_checking(formula):
    Utils.verified_propositions(formula)
    truth_table = truth_table_generator(formula)
    return True in truth_table[repr(formula)]

def get_atoms(formula):
    Utils.verified_propositions(formula)
    return list(filter(lambda f: isinstance(f, Atom), formula.sub_formula))

def get_formulas(formula, atoms):
    Utils.verified_propositions(formula)
    return list(filter(lambda f: f not in atoms, formula.sub_formula))

def truth_table_generator(formula, atoms=None):
    Utils.verified_propositions(formula)
    atoms = get_atoms(formula) if atoms == None else atoms
    truth_table = collections.OrderedDict()

    num_rows = 2 ** len(atoms)
    count_for_change = [2 ** (i - 1) for i in range(len(atoms), 0, -1)]
    
    for index, atom in enumerate(atoms):
        truth_table[repr(atom)] = (
            _generate_values_of_atom_(num_rows, count_for_change[index])
        )

    for formula in get_formulas(formula, atoms):
        truth_table[repr(formula)] = (
            _generate_values_of_formula_(
                formula,
                num_rows,
                atoms,
                truth_table
            )
        )

    return truth_table

def print_truth_table(truth_table):
    if not truth_table:
        print('Não existe formulas para printar essa tabela-verdade')

    print(*list(truth_table.keys()), sep=" | ")

    if truth_table.values():
        num_rows = len(list(truth_table.values())[0])  
    
    for row in range(num_rows):
        values = [key[row] for key in truth_table.values()]
        print(*values, sep=" | ")

def _generate_values_of_atom_(num_rows, num_for_change):
    list_of_values = []
    value = True
    for row in range(0, num_rows, num_for_change):
        list_of_values[row:row+num_for_change] = [value] * num_for_change 
        value = not value
    return list_of_values

def _generate_values_of_formula_(formula, num_rows, atoms, truth_table):
    list_of_values = []
    for row in range(num_rows):
        for atom in atoms:
            atom.value = truth_table[repr(atom)][row]
        list_of_values.append(formula.value)
    return list_of_values