
mtriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(0, 3):
    for j in range(0, 3):
        print(i,j)
        mtriz[i][j] = i+50

print(mtriz)

for m in mtriz:
    print(m)
