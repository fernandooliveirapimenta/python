
produtos = ('Celular', 88, 'Garrafa', 8.3, 'Sapato', 87)

for i in range(0, len(produtos)):
    if i+1 <= len(produtos) - 1 and type(produtos[i]) == str:
        print(f'{produtos[i]} - {produtos[i+1]}')
