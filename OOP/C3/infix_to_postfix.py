from Stack import Stack

def precedence(operand_1, operand_2):
    if (operand_1 in '*/' and operand_2 in '*/') \
        or (operand_1 in '+-' and operand_2 in '+-'):
        return 0
    elif operand_1 in '*/' and operand_2 in '+-':
        return 1
    else:
        return -1

def infix_to_postfix(expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    token_list = expr.split(' ')
    op_stack = Stack()
    result = []

    for token in token_list:
        if token in '+-*/':
            while not op_stack.is_empty():
                if prec[op_stack.peek()] >= prec[token]:
                    result.append(op_stack.pop())
                else:   
                    break
            op_stack.push(token)
        elif token in '()':
            if token == '(':
                op_stack.push(token)
            else:
                while not op_stack.is_empty() and op_stack.peek() != '(':
                    result.append(op_stack.pop())     
                op_stack.pop()
        else:
            result.append(token)

    while not op_stack.is_empty():
        result.append(op_stack.pop())
    
    return ' '.join(result)

print(infix_to_postfix('( A - B + C + ( E / F + D ) ) * D'))        