from Stack import Stack

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        char = symbol_string[index]

        if char in '{[(':
            s.push(char)
        elif char in '}])':
            if not s.is_empty():
                top = s.pop()
                if not matches(top, char):
                    balanced = False
            else:
                balanced = False

        index += 1
    
    if s.is_empty() and balanced:
        return True
    else:
        return False

def matches(open, close):
    opens = '([{'
    closes = ')]}'

    return opens.index(open) == closes.index(close)

print(par_checker('{{()(}})'))