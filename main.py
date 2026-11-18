try:
    saldo = 100000
    divida = 0
    print(f"Seu saldo é: {saldo}")
    print(f"Suas dívidas são: {divida}")
    print(f"Seu saldo final é: {saldo - divida}")
    transacao = int(input("Digite quanto você quer transferir: "))
    saldo -= transacao
    if saldo < 0:
        divida = abs(saldo)
        print(f"Você está com uma dívida de: {divida}")
    else:
        print(f"Seu saldo restante é: {saldo}")
    print(f"Seu saldo final é: {saldo}")
except Exception as e:
    print(e)