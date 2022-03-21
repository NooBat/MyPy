from Stack import Stack

def evaluate_postfix(expr):
    token_list = expr.split(' ')
    res_stack = Stack()

    for token in token_list:
        if token in '+-*/':
            operand_2 = int(res_stack.pop())
            operand_1 = int(res_stack.pop())
            result = None
            if token == '+':
                result = operand_1 + operand_2
            elif token == '-':
                result = operand_1 - operand_2
            elif token == '*':
                result = operand_1 * operand_2
            else:
                result = operand_1 / operand_2
            res_stack.push(result)
        else:
            assert type(token) == int, "Invalid type: %s" % type(token)
            res_stack.push(token)
    
    return res_stack.pop()

print(evaluate_postfix('A B +'))