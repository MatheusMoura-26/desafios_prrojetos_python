menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


====> Digite sua opção: """


opcao = input(menu)


saldo = 0
valor=0
limite=500
LIMITES_SAQUES=3
extrato = ""
numero_saques=0


while True:
    opcao = input(menu)

    
    if opcao == "d":
        print("Você selecionou deposito")
        valor = float(input("Digite o valor do deposito:"))
        if valor >0:
            saldo+=valor
            print(f"Depósito de {valor}  efetuado com sucesso")
            extrato+= f"Deposito: RS{valor:.2f}\n"
        else:
            print("Operação inválidaa") 

    elif opcao == "s":
       valor = float(input("Digite o valor do saque:"))
       execedeu_saldo = valor > saldo
       exedeu_limite = valor > limite
       execedeu_saques= numero_saques >= LIMITES_SAQUES


       if execedeu_saldo:
           print("OPeração falhou! Você não tem saldo o suficiente")


       elif exedeu_limite:
          print("Operação falhou! O valor de saque  execedeu o máxmo permitido")

       elif execedeu_saques:
          print("OPeração falhou! você execedeu o número de saques permitidos em um dia")
        
       elif valor >0:
          saldo-=valor
          extrato+= f"Saque: RS{valor:.2f}\n"
          numero_saques+=1


    
    elif opcao == "e":
        print("================EXTRATO==============================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("=============================================")
        

    elif opcao == "q":
        break


    else:

        print("Operação inválida")