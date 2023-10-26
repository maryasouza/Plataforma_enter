from inputData import menu


def login():
    decSenha = menu(cripto)
    num_tentativas = 0
    acertou = False
    while num_tentativas <= 3 and acertou == False:
        tentativa = input("DIGITE A SENHA DE ACESSO DESCRIPTOGRAFADA: ")
        # print(tentativa)

        num_tentativas = num_tentativas + 1
        # validacao da tentativa
        if tentativa == decSenha:
            print('')
            print('')
            print("========================================")
            print("== BEM VINDO A PLATAFOMA              ==")
            print("== SEU ACESSO FOI LIBERADO            ==")
            print("========================================")
            print("========================================")
            print('')
            print('')
            acertou = True
            exit(1)
        else:
            print('')
            print('')
            print('--- SENHA INVÁLIDA - NÚMERO DE TENTATIVAS: ', num_tentativas, ' ----')
            print('---- ACESSO NEGADO ----')
            print('')
            acertou = False
    print('')


def mostrar_menu():
    print('')
    print("========================================")
    print("=       LOGIN PLATAFORMA               =")
    print("========================================")
    print("===  Bem-vindo ao Sistema de Login   ===")
    print("= 1. Login                             =")
    print("= 2. Sair                              =")
    print("=                                      =")
    print("========================================")
    print("========================================")
# mensagem ao tentar ser acertada para ter o acesso liberado ao navio
def cripto():
    while True:
        print('')
        print('')
        print("========================================")
        print("=   DESEJA LOGAR NA PLATAFORMA?        =")
        print("========================================")
        print("= 1. SIM                               =")
        print("= 2. NAO                               =")
        print("=                                      =")
        print("========================================")
        print("========================================")
        acesso = input("Escolha uma opção de acesso: ")
        if acesso == "1":
            mostrar_menu()
            escolha = input("Escolha uma opção: ")
        elif acesso == "2":
            print('')
            print('')
            print("========================================")
            print("=          MUITO OBRIGADO!             =")
            print("========================================")
            print('')
            print('')
            break
        print()
        if escolha == "1":
            login()
        elif escolha == "2":
            print('')
            print('')
            print("========================================")
            print("=   SAINDO DO SISTEMA PLATAFORMA       =")
            print("========================================")
            print("========================================")
            print('')
            print('')
            break
        else:
            print("Opção inválida. Tente novamente.")
