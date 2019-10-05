from random import randint

tupla = ()
for i in range(1, 6):
    rand = str(randint(3,20))
    print(rand)
    tupla += tuple(rand)

print()
print(max(tupla))
print(min(tupla))

