'''
Project: Implementações da cadeira de lógica para Ciência da Computação
@author: João Victor
Created: 24/06/2020
'''

''' Functions of Logic '''
from logic_utils import *
from logic import *
import collections


def logical_consequence(formula, premises):
    Utils.verified_propositions(formula)
    truth_table = collections.OrderedDict()
    atoms = get_atoms(formula)
    premises_values = []

    for premise in premises:
        if (Utils.verified_propositions(premise)
                and not isinstance(premise, Atom)):
            atoms = set(atoms)
            atoms.update(get_atoms(premise))
            atoms = sorted(atoms, key=repr)
            truth_table.update(truth_table_generator(premise, atoms))
            premises_values.append(truth_table[repr(premise)])
        else:
            raise FormulaArgumentError(premise)

    if premises_values:
        num_rows = len(premises_values[0])

    for sub_formula in get_formulas(formula, atoms):
        formula_values = (
            _generate_values_of_formula_(
                sub_formula,
                num_rows,
                atoms,
                truth_table
            )
        )
        truth_table[repr(sub_formula)] = formula_values

    indexes = []
    for row in range(num_rows):
        premises_values_trues = (
            [premise_value[row] for premise_value in premises_values]
        )
        if premises_values_trues == [True] * len(premises):
             indexes.append(row)

    is_logical_consequence = False
    
    if indexes:
        is_logical_consequence = (
            list(map(formula_values.__getitem__, indexes)) == [True] * len(indexes)
        )
    
    return is_logical_consequence, truth_table

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