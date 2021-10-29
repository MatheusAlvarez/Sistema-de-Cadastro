from lib.interface import  *


#Função utilizada para verificar o arquivo 
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else: 
        return True


# Função utilizada para criar o arquivo   
def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')
    
  
# Função utilizada para ler o arquivo
def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Houve um erro ao abrir o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close


# Função utilizada para fazer o cadastro    
def cadastrar(arq, nome = 'desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    
    except:
        print('Houve um erro ao abrir o arquivo!')

    else: 
        try:
            a.write(f'{nome};{idade}\n')

        except:
            print('Houve um erro na hora de escrever os dados!')
        
        else: 
            print(f'Novo registro de {nome} adicionado.')
            a.close()
