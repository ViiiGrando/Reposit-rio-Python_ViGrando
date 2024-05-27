'''def imprimir_nome(nome=str, sobrenome=str):

  pass



imprimir_nome('Victor', '95')    
'''


#KWARDS
def imprimir_nome(**nomes):
    print(f'{nomes['nome']} {nomes['sobrenome']}')

imprimir_nome(nome = 'VI', sobrenome = 'GRA')

#KWARDS São basicamente um dicionário para um parametro, quando a gente não sabe quantos argumentos serão utilizados em uma função