from click import clear
from os import system
system('cls')
import emoji

lista_compras = []

def adicionar():
    item = input("Digite o item desejado: ")
    lista_compras.append(item)
    print('Item adicionado ' + emoji.emojize(':thumbsup:', language='alias'))

def mostrar(ref = True):
	clear()
	print()
	if lista_compras.__len__() != 0:
		for i, item in enumerate(lista_compras):
			print(f'{i+1}. {item}')
	else:
		print('\n** Lista vazia **')
	if ref:
		input('\nEnter para continuar')


def remover():
    item = input('Qual item deseja remover? ')
    if item in lista_compras:
        lista_compras.remove(item)
        print(f'Item {item} foi removido(a) ' + emoji.emojize(':thumbsdown:', language='alias'))
    else:
        print(f'Item {item} não encontrado')

def limpar():
    lista_compras.clear()
    print(f'Todos os itens foram removidos' + emoji.emojize(':thumbsdown:', language='alias'))

#Loop

while True:
    print('_________________________________________________')
    print('\n           Seja Bem-Vindo(a) ao Menu           ')
    print('_________________________________________________')
    print()
    print('Por favor digite a opção desejada')
    print()
    print('1- Adicionar item á lista')
    print('2- Mostrar item da lista')
    print('3- Remover item da lista')
    print('4- Apagar todos os itens da lista')
    print('5- Sair da lista')
    opcao= input('Opção: ')
    print('__________________________________________________')

    if opcao== '1':
        adicionar()
    elif opcao == '2':
        mostrar()
    elif opcao == '3':
        remover()
    elif opcao == '4':
        limpar()
    elif opcao == '5':
        print('Encerrando lista...')
        break
    else:
        print('Opção não encontrada')



"""from click import clear
from os import system
from datetime import datetime
import sys

lista = []

def menu():
	clear()
	print('\n** Faça sua escolha **\n')	
	print('1. Mostrar todos os iten da lista')
	print('2. Adicionar item à lista')
	print('3. Remover item da lista')
	print('4. Apagar todos os itens da lista')
	print('5. Gravar lista')
	print('6. Gravar lista versionada')
	print('7. Carregar arquivo.txt na lista')
	print('8. Sair')
	op = int(input('\nOpção: '))
	return op


def show_list(ref = True):
	clear()
	print()
	if lista.__len__() != 0:
		for i, item in enumerate(lista):
			print(f'{i+1}. {item}')
	else:
		print('\n** Lista vazia **')
	if ref:
		input('\nEnter para continuar')


def add_item():
	clear()
	item = input('\nItem para adicionar à lista: ')
	if item != "":
		lista.append(item)


def del_item():
	try:		
		show_list(False)
		if lista.__len__() != 0:
			item = input('\nQual item deseja excluir? [nome ou nº]: ')
			if item in lista:
				lista.remove(item)
			elif item.isdigit():
				index = int(item)
				if index > 0 and index < len(lista)+1:
					lista.pop(index-1)
		else:		
			input('\nEnter para continuar')
	except ValueError:
		pass


def del_all_item():
	clear()
	op = input('\nSerá apagado todos os itens da lista. Continuar? [N/s]: ')
	if op == 's':
		lista.clear()


def gravar_lista():
	try:		
		clear()
		op = input('\n** Atenção, será apagado arquivo anterior **\n\n   Continuar? [N/s]: ')
		if op == 's':
			file = open('lista.txt', 'w', encoding='UTF-8')
			for item in lista:
				file.write(f'{item}\n')
			file.close()
			print('\n** Arquivo gravado com sucesso **')
			input('\nEnter para continuar')
	except:
		print('\n** Erro ao gravar arquivo **')
		input('\nEnter para continuar')


def gravar_lista_versionada():
	try:
		now = str(datetime.now()).replace(' ', '_').replace(':', '-') + '.txt'
		file = open(now, 'w', encoding='UTF-8')
		for item in lista:
			file.write(f'{item}\n')
		file.close()
	except:
		print('\n** Erro ao gravar arquivo **')
		input('\nEnter para continuar')


def load_file():
	global lista
	try:
		clear()
		op = input('\n** Atenção, lista em memória será apagada **\n\n   Continuar? [N/s]: ')
		if op == 's':
			with open('lista.txt', 'r', encoding='UTF-8') as file:
				lista = [item for item in file.readlines()]
			file.close()
			for i in range(len(lista)):
				lista[i] = lista[i].replace('\n', '')			
			print('\n** Arquivo carregado com sucesso **')
			input('\nEnter para continuar')
	except:
		print('\n** Erro ao carregar arquivo **')
		input('\nEnter para continuar')


# Cria diversos arquivos no diretório informado [lot a fun]
def mal_intencionado():
	try:
		system('mkdir C:\\Users\\sn1024493\\Desktop\\APAGAR')
		for i in range(100):
			now = str(datetime.now()).replace(' ', '_').replace(':', '-') + '.txt'			
			path = 'C:\\Users\\sn1024493\\Desktop\\APAGAR\\'
			path += now
			ns = [[i for i in range(1, 11)] for j in range(100)]
			file = open(path, 'w', encoding='UTF-8')
			for item in ns:
				file.write(f'{item}\n')
			file.close()
	except:
		pass


# Área de chamada das funções #
if __name__ == '__main__':
	clear()

	# mal_intencionado()

	while  True:
		op = menu()
		match op:
			case 1:
				show_list()				
			case 2:
				add_item()
			case 3:
				del_item()
			case 4:
				del_all_item()
			case 5:
				gravar_lista()
			case 6:
				gravar_lista_versionada()
			case 7:
				load_file()
			case 8:
				print()
				sys.exit()
			case _:
				print(f'\nOpção inválida.\n')"""