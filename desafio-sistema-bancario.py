menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[a] Criar Usuario
[b] Criar conta
[q] Sair

=> """

saldo = 0
extrato = ""
numero_saques = 0
usuarios = []
contas = []
AGENCIA = "0001"
def saque(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    

    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    return(saldo, extrato)
def deposito(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    return(saldo,extrato)
def extrato (saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
def criar_usuario(nome,data_nascimento,cpf, endereco):
    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(novo_usuario)
    print("Usuário riado com sucesso!")
def existe_cpf(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return True
    return False
def criar_conta(agencia, n_conta, usuarios):
    cpf= input("Insira seu cpf: ")
    if existe_cpf(cpf, usuarios):
        conta = {
            "agencia": AGENCIA,
            "n_conta": n_conta,
            "cpf": cpf
        }
        contas.append(conta)
        print("Conta criada com sucesso")
    else:
        print("Usuario inexistente. Fluxo de criação de conta encerrado")


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo,valor=valor,extrato=extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=500, numero_saques=numero_saques, LIMITE_SAQUES=3)

    elif opcao == "e":
        extrato(saldo, extrato=extrato)

    elif opcao =="a":
        print("Por favor insira os dados a seguir:\n")
        cpf= str(input("CPF: "))
        cpf = cpf.replace(".","").replace("-","")
        if existe_cpf(cpf, usuarios):
            print("CPF existente")
            continue
        nome = input("Nome Completo: ")
        data_nascimento=input("Data Nascimento: ")
        endereco = input("Endereco (Formato: Rua, numero - bairro - cidade/estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)
    
    elif opcao == "b":
        n_conta = len(contas)+1
        criar_conta(AGENCIA, n_conta, usuarios)
    
    elif opcao == "mostrar":
        print(contas)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")