menu = """
============ Menu ============
[d] Depositar
[s] Sacar
[e] Extrato
[0] Sair
==============================
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":

        valor = float(input("Valor a depositar: "))

        if valor < 0:
            print("Erro! Valor inválido.")
            continue
        else:
            saldo += valor
            extrato += f"\nDepósito de R$ {valor:.2f}"
            print("Deposito bem sucedido.")

    elif opcao == "s":

        if  numero_saques >= LIMITE_SAQUES:
            print("\nLimite de saque diário atingido.")
            continue
        else:
            valor = float(input("Valor a ser sacado: "))
            if valor > 500:
                print("Limite do valor de R$500.00 excedido.")
                continue
            elif valor > saldo:
                print("Saldo  insuficiente.")
                continue
            else:
                saldo -= valor
                numero_saques += 1
                extrato += f"\nSaque de R$ {valor:.2f}"
                print("Saque realizado com sucesso.")

    elif opcao == "e":
        print("============= Extrato =============\n" + extrato)
    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
