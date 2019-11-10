def soma(a, b):
    return a + b


def contador(* num):
    print(num)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


a = 4
b= 5
s = a + b

print(soma(5, 3))
contador(3,2,1)
contador(1,4)

valores = [3, 2, 6, 0, 2]
dobra(valores)
print(valores)