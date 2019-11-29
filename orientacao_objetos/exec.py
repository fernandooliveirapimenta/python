from conta import Conta

conta = Conta('123-4', 'João', 120.0, 1000)

conta.titular = "Joao"
conta.saldo = 120.0

print(conta.titular)
print(conta.saldo)
print(type(conta))

conta.deposita(500)

print(conta.saldo)

conta.extrato()