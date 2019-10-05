
# exp = '(50 + 5) - (3)'
exp = '((a+b) * c)'

def testaparenteses(expr):
    contador = 0
    for c in expr:
        if c == '(':
            contador += 1
        if c == ')':
            if contador > 0:
                contador -= 1
            else:
                return False

    return contador == 0

print(testaparenteses(exp))
