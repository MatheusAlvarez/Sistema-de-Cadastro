def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO!  Pro favor digite um número inteiro válido.')
            continue
        
        except (KeyboardInterrupt):
            print('O usuário preferiu não inserir os dados')
            return 0
        
        else:
            return n
        


def linha(tam = 42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'{c} - {i}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc