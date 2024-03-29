menu = """
============ Menu ============
[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar Usuário
[r] Cadastrar Nova Conta Corrente
[0] Sair
==============================
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
clientes = []
contas = []
numero_conta = 0
LIMITE_SAQUES = 3
AGENCIA = "0001"

def saque(*, numero_saques):
    global extrato
    global saldo
    if  numero_saques >= LIMITE_SAQUES:
        return("\nLimite de saque diário atingido.")
    else:
        valor = float(input("Valor a ser sacado: "))
        if valor > 500:
            return("Limite do valor de R$500.00 excedido.")
        elif valor > saldo:
            return("Saldo  insuficiente.")
        else:
            saldo -= valor
            numero_saques += 1
            extrato += f"\nSaque de R$ {valor:.2f}"
            return(f"Saque realizado com sucesso.\nSaldo: {saldo}")


def deposito():
    global extrato
    global saldo
    valor = float(input("Valor a depositar: "))

    if valor < 0:
        return("Erro! Valor inválido.")
    else:
        saldo += valor
        extrato += f"\nDepósito de R$ {valor:.2f}"
        return(f"Deposito bem sucedido.\nSaldo: {saldo}")

def exibir_extrato (saldo, /, *, extrato):
    return(f"""
============= Extrato ============="
           
{extrato}

Saldo: {saldo}

===================================
""")


def cadastrar_usuario (nome, nascimento, cpf, endereco):
    global clientes
    for cliente in  clientes:
        if cliente["cpf"] == cpf:
            return("Usuário já cadastrado.")
    novo_cliente = {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": nascimento,
            "endereço": endereco,
        }
    clientes.append(novo_cliente)
    return("Usuário cadastrado com sucesso!")

def criar_conta_corrente(agencia, numero_conta, usuario):
    global contas
    global clientes
    cliente_existe = False
    for cliente in clientes:
        if cliente["cpf"] == usuario:
            cliente_existe = True
            break
    if cliente_existe == False:
        return("O usuário não existe!")
    else:
        novo_cliente = {
            "agencia": agencia,
            "conta": numero_conta,
            "usuario": usuario
        }
        contas.append(novo_cliente)
        return("Conta criada com sucesso!")

            


while True:

    opcao = input(menu)

    if opcao == "d":

        print(deposito())

    elif opcao == "s":

        print(saque(numero_saques=numero_saques))

    elif opcao == "e":
        print(exibir_extrato(saldo, extrato = extrato))
    elif opcao == "c":
        nome = input("Nome: ")
        nascimento = input("Data de Nascimento (dd/mm/aaaa): ")
        cpf = input("CPF: ")
        endereco = input("Endereco (logradouro, nro - bairro - cidade/sigla estado): ")
        print(cadastrar_usuario(nome, nascimento, cpf, endereco))
        print(clientes)
    elif opcao == "r":
        numero_conta += 1
        usuario = input("Usuário titular da conta (cpf): ")
        print(criar_conta_corrente(AGENCIA, numero_conta, usuario))
        print(contas)
    elif opcao == "0":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")



