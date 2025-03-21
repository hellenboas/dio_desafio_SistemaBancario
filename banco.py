menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        deposito = float(input("Digite o valor que deseja depósito:"))

        if deposito > 0:
            print("Deposito efetuado")

            saldo+=deposito
            extrato += f"Depósito: R$ {saldo:.2f}\n"
        else:
            print("Não é possivel realizar a operação")

    elif opcao == "s":
       
        print("Saque")
        saque = float(input("Digite o valor do saque: "))

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        excedeu_limite = saque > saldo

        if excedeu_saques:
            print("Não é possivel realizar a operação, quantidade de saques foi excedida")

        elif saque > 0 and saldo > saque :
            saldo = saldo - saque
            numero_saques += 1
            saque =+ saque
            extrato += f"Saque: R$ {saque:.2f}\n"

        elif excedeu_limite:
            print("Não foi possivel realizar a operação, saldo insuficiente")
        else:
            print("Não é possivel fazer a operação")

    elif opcao == "e":
        print("\n--EXTRATO--")
        print("Não houve movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("--------------------------------------------")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")