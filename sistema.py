from lib.interface import *
from lib.arquivo import *
from time import sleep

# Variável para armazenar o arquivo txt
arq = 'cadastros.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resp == 1:
        # Opção de listar o conteúdo de um arquivo 
        lerArquivo(arq)
    
    elif resp == 2:
        # Opção de cadastrar um novo usuário
       cabecalho('NOVO CADASTRO')
       nome = str(input('Nome: '))
       idade = leiaInt('Idade: ')
       cadastrar(arq, nome, idade)
    
    elif resp == 3:
        cabecalho('Saindo do sistema... Até logo!')
        sleep(1)
        break

    else: 
        cabecalho('ERRO! Digite uma opção válida!')
        sleep(2)
