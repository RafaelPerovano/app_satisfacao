import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

alunos, professores, outros = {}, {}, {}

def verifica_arquivo(arq1, arq2, arq3):
    return all(os.path.isfile(arq) for arq in [arq1, arq2, arq3])

def alunos_add(satisfacao):
    global alunos
    alunos[satisfacao] += 1
    salvar_arquivo('alunos.txt', alunos)

def professores_add(satisfacao):
    global professores
    professores[satisfacao] += 1
    salvar_arquivo('professores.txt', professores)

def outros_add(satisfacao):
    global outros
    outros[satisfacao] += 1
    salvar_arquivo('outros.txt', outros)

def salvar_arquivo(nome_arquivo, dados):
    with open(os.path.join(DATA_DIR, nome_arquivo), 'w') as arquivo:
        for nome, valor in dados.items():
            arquivo.write(f'{nome}: {valor}\n')

def le_arquivo(nome_arquivo):
    var = {}
    with open(os.path.join(DATA_DIR, nome_arquivo), 'r') as arquivo:
        for linha in arquivo:
            nome, valor = linha.strip().split(': ')
            var[nome] = int(valor)
    return var

def cria_bd():
    os.makedirs(DATA_DIR, exist_ok=True)
    salvar_arquivo('alunos.txt', alunos)
    salvar_arquivo('professores.txt', professores)
    salvar_arquivo('outros.txt', outros)

def alunos_default():
    return {'satisfacao1': 0,
            'satisfacao2': 0,
            'satisfacao3': 0,
            'satisfacao4': 0,
            'satisfacao5': 0}

def professores_default():
    return {'satisfacao1': 0,
            'satisfacao2': 0,
            'satisfacao3': 0,
            'satisfacao4': 0,
            'satisfacao5': 0}

def outros_default():
    return {'satisfacao1': 0,
            'satisfacao2': 0,
            'satisfacao3': 0,
            'satisfacao4': 0,
            'satisfacao5': 0}

def verifica(satisfacao, usuario):
    if usuario == 'aluno':
        alunos_add(satisfacao)
    elif usuario == 'professor':
        professores_add(satisfacao)
    elif usuario == 'outros':
        outros_add(satisfacao)

def main():
    global alunos, professores, outros

    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    alunos_arquivo = os.path.join(DATA_DIR, 'alunos.txt')
    professores_arquivo = os.path.join(DATA_DIR, 'professores.txt')
    outros_arquivo = os.path.join(DATA_DIR, 'outros.txt')

    if verifica_arquivo(alunos_arquivo, professores_arquivo, outros_arquivo):
        alunos = le_arquivo('alunos.txt')
        professores = le_arquivo('professores.txt')
        outros = le_arquivo('outros.txt')
    else:
        alunos = alunos_default()   
        professores = professores_default() 
        outros = outros_default() 
        cria_bd()

if __name__ == '__main__':
    main()
