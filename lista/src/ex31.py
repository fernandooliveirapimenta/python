
distancia = 33.4

# if distancia <= 200:
#     preco = distancia * 0.50
# else:
#     preco = distancia * 0.45


preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(preco)
