from funcoes import *

compromissos = {}
compromissos = lerArquivo(compromissos)
nome = nomeUsuario()
continua = True
while continua == True:
	opcaoAgenda = menuPrincipal(nome)
	if opcaoAgenda == 1:
		clear()
		consultarCompromissos(compromissos)
	elif opcaoAgenda == 2:
		clear()
		painelCadastro(compromissos)
	elif opcaoAgenda == 3:
		clear()
		editarCompromissos(compromissos)
	elif opcaoAgenda == 4:
		clear()
		excluirCompromissos(compromissos)
	elif opcaoAgenda == 5:
		clear()
		continua = encerrarPrograma(nome)
	else:
		print('Opção inválida')

	#sair do while
	if continua == True:
		continuaLoop = input('Nova consulta? (s/n)\n')
		continuaLoop = continuaLoop.lower()
		if continuaLoop == 's':
			pass
			clear()
		elif continuaLoop == 'n':
			clear()
			print('Até mais, %s! Saindo...'%nome)
			continua = False
		else:
			clear()
			print('Opção inválida, saindo...')
			continua = False