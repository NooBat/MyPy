from par_checker import par_checker
from infix_to_postfix import infix_to_postfix
from evaluate_postfix import evaluate_postfix

class Calculator:
    def __init__(self, expression):
        self.exp = expression
    
    def 