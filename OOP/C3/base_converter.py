from Stack import Stack

def base_converter(dec_number, base=2):
    digits = '0123456789ABCDEF'

    rem_stack = Stack()

    while dec_number > 0:
        rem_stack.push(dec_number % base)
        dec_number //= base
    
    new_number = ''
    while not rem_stack.is_empty():
        top = rem_stack.pop()
        new_number += digits[top]
    
    return new_number

print(base_converter(25, 16))