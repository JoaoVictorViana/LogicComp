''' Utils of the Atom and Formula '''
class Utils:

    count_of_repr = 0
    set_of_repr = ['P', 'Q', 'R', 'S']

    @staticmethod
    def repr_of_atom():
        if Utils.count_of_repr == 4:
            Utils.set_of_repr += Utils.increment_set_repr(Utils.set_of_repr)  
        Utils.count_of_repr += 1     
        return Utils.set_of_repr[Utils.count_of_repr - 1]

    @staticmethod
    def increment_set_repr(set_of_repr):
        return [_repr + str(i) for i in range(1,101) for _repr in set_of_repr]

    @staticmethod
    def verified_propositions(proposition):
        if not issubclass(proposition.__class__, Formula):
            raise FormulaArgumentError(proposition)
        else:
            return True
''' Exception of the Atom and Formula '''

class FormulaError(Exception):
    pass

class FormulaArgumentError(FormulaError):
    ''' Exception raised for erros in the arguments at Formulas '''
    
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return f"'{self.expression}' não é uma fórmula!"


''' Interface Formula'''

class Formula:
    pass
