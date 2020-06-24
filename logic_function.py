'''
Project: Implementações da cadeira de lógica para Ciência da Computação
@author: João Victor
Created: 24/06/2020
'''

''' Functions of Logic '''
from logic_utils import *
from logic import *
import collections

def truth_table_generator(formula):
    Utils.verified_propositions(formula)
    atoms = []
    formulas = []
    truth_table = collections.OrderedDict()
    for sub_formula in formula.sub_formula:
        if isinstance(sub_formula, Atom):
            atoms.append(sub_formula)
        else:
            formulas.append(sub_formula)

    num_rows = 2 ** len(atoms)
    array_of_count_for_change = []

    for count in range(len(atoms) - 1, -1, -1):
        array_of_count_for_change += [2 ** count]
    
    for index in range(len(atoms)):
        index_atom = repr(atoms[index]) 
        count_for_change = array_of_count_for_change[index]
        truth_table[index_atom] = _generate_values_of_atom_(num_rows, count_for_change)

    for formula in formulas:
        truth_table[repr(formula)] = _generate_values_of_formula_(formula, num_rows, atoms, truth_table)

    return truth_table

def _generate_values_of_atom_(num_rows, num_for_change):
    count_value = 0
    list_of_values = []
    value = True
    for row in range(num_rows):
        if count_value == num_for_change:
            value = not value
            count_value = 0

        count_value += 1
        list_of_values += [value]
    return list_of_values

def _generate_values_of_formula_(formula, num_rows, atoms, truth_table):
    list_of_values = []
    for row in range(num_rows):
        for index in range(len(atoms)):
            index_atom = repr(atoms[index])
            atoms[index].value = truth_table[index_atom][row]
        list_of_values += [formula.value]
    return list_of_values