# lista de 6 nomes
nomes = ['Lucas','Isabela','Eladio','Marcia','Luiza','Pedro']

# usuário informa o indice que deseja alterar
indice = int(input('Informe o indice que deseja alterar: '))
indice -= 1

nomes [indice] = input('Informe o novo nome: ')


# exibe a lista
for nome in nomes:
    print(nome)
