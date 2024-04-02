import textwrap
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))




def depositar(saldo,valor, extrato,/):
   if valor >0:
       saldo += valor
       extrato += f"Deposito:\tR$ {valor:.2f}\n"
       print("Deposito realizado com sucesso!")
   else:
       print("OPeração inválida, Valor invalido")
   return saldo, extrato


def sacar(*,saldo,valor,extrato,limite,numero_saques,limite_saques):
    excedeu_saldo = valor >saldo
    execedeu_limite = valor >limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Você não tem saldo sufuciente para essa operação")
    elif execedeu_limite:
        print("Operação falhou, O valor de saque excede o limite.")
    elif excedeu_saques:
        print("operação falhou! Número máximo de saques execedido")

    elif valor > 0:
        saldo -= valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        numero_saques+=1
        print("Saque realizado com sucesso")
    else:
        print("Operação falhou! O valor informado é inválido")
    return saldo,extrato

def exibir_extrato(saldo,/,*,extrato):
    print("==============EXTRATO=====================")
    print("Não foram realizadas operações." if not extrato else extrato)
    print(f"\nSaldo:\t\tRS {saldo:.2f}")
    print("============================================")  

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero):")  
    ususario= filtrar_usuario(cpf,usuarios)

    if ususario:
        print("Já existe usuario com esse cpf!")
        return

    nome = input("Informe o nome completo:")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa):")
    endereco = input("Informe o enedereco(logadouro, nro - bairro - cidade/sigla estado):") 

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário cadastrado com sucesso!!!!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia,numero_conta,usuarios):
    cpf=input("INforme o número do cpf:")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuario não encontrado")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()