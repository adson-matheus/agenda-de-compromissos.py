from os import system, name
from time import strftime
from datetime import datetime

def menuPrincipal(nome):
	print("""
			=========== A G E N D A ============
			====================================
			1) Consultar agenda de compromissos;
			2) Cadastrar novo compromisso;
			3) Editar compromisso específico;
			4) Excluir compromisso específico;
			5) Encerrar programa
			====================================
	""")
	opcaoAgenda = ''
	while not opcaoAgenda.isdigit():
		try:
			opcaoAgenda = int(input('O que gostaria de fazer, %s? \n'%nome))
		except ValueError:
			clear()
			print('Digite um número válido!\n')
			print("""
			=========== A G E N D A ============
			====================================
			1) Consultar agenda de compromissos;
			2) Cadastrar novo compromisso;
			3) Editar compromisso específico;
			4) Excluir compromisso específico;
			5) Encerrar programa
			====================================
			""")
		opcaoAgenda = str(opcaoAgenda)
	opcaoAgenda = int(opcaoAgenda)
	return opcaoAgenda

def clear():
	# windows 
	if name == 'nt': 
		_ = system('cls') 

	# mac e linux
	else:
		_ = system('clear')

def novoUsuario():
	nome = input('Bem vindo, escreva seu nome para começar: ')
	nomeArq = open('nome.txt', 'w')
	nomeArq.write(nome)
	nomeArq.close()
	clear()
	return nome

def nomeUsuario():
	try:
		nomeArq = open("nome.txt", "r")
		nomeLinha = nomeArq.readline()
		nome = nomeLinha
	except IOError:
		nomeArq = open("nome.txt", "w")
		nome = novoUsuario()
	nomeArq.close()
	return nome

def consultarId():
	try:
		#limpa os id caso não haja nenhum compromisso.
		arq = open('compromissos.txt', 'r')
		linha = arq.readline()
		if linha == '':
			arqId = open('id.txt', 'w')
			arqId.close()
	except IOError:
		arq = open('compromissos.txt', 'w')
		arq.close()

	try:
		arqId = open('id.txt', 'r+')
		linhaId = arqId.readline()
		novoId = ''
		while linhaId != '':
			novoId = linhaId.rstrip()
			linhaId = arqId.readline()

		if novoId == '':
			novoId = 1
			novoId = str(novoId)
			arqId.write(novoId + '\n')
		else:
			novoId = int(novoId) + 1
			novoId = str(novoId)
			arqId.write(novoId + '\n')
		arqId.close()
		
	except IOError:
		arqId = open('id.txt', 'w')
		arqId.write('1'+ '\n')
		arqId.close()
		novoId = 1
		novoId = str(novoId)
	arqId.close()
	return (novoId)

def lerArquivo(compromissos):
	compromissos = {}
	try:
		arq = open("compromissos.txt", "r")
		idCompromisso = arq.readline()
	except IOError:
		arq = open("compromissos.txt", "w")
		idCompromisso = ''
		arq.close()
	while idCompromisso != '':
		idCompromisso = idCompromisso.rstrip()
		titulo = arq.readline()
		titulo = titulo.rstrip()

		assunto = arq.readline()
		assunto = assunto.rstrip()

		dataCompromisso = arq.readline()
		dataCompromisso = dataCompromisso.rstrip()

		horaCompromisso = arq.readline()
		horaCompromisso = horaCompromisso.rstrip()

		horaFimCompromisso = arq.readline()
		horaFimCompromisso = horaFimCompromisso.rstrip()

		dataCadastro = arq.readline()
		dataCadastro = dataCadastro.rstrip()

		lista = [titulo, assunto, dataCompromisso, horaCompromisso, horaFimCompromisso, dataCadastro]
		compromissos[idCompromisso] = lista
    	
    	#loop
		idCompromisso = arq.readline()
	arq.close()
	return compromissos

def gravarArquivo(compromissos):
	arq = open("compromissos.txt", "w")
	for compromisso in compromissos:
		arq.write(compromisso + '\n')
		lista = compromissos[compromisso]
		for item in lista:
			arq.write(item + '\n')
	arq.close()

def validaHora(horario, data):
	lista = horario.split(':')
	if len(lista) != 2:
		return False
	for x in lista:
		if not x.isdigit():
	  		return False

	hora = int(lista[0])
	minuto = int(lista[1])

	d = datetime.now()
	dataAtual = d.strftime('%d/%m/%Y')
	horaAtual = d.strftime('%H')
	horaAtual = int(horaAtual)
	minutoAtual = d.strftime('%M')
	minutoAtual = int(minutoAtual)

	if hora < 0 or hora > 23:
		return False

	if minuto < 0 or minuto > 59:
		return False

	if hora < horaAtual and data == dataAtual:
		#se a hora for menor que a hora atual
		# e a data fornecida for igual a data de hoje
		return False
	elif hora == horaAtual and data == dataAtual:
		if minuto > minutoAtual:
			return True
		else:
			return False
	else:
		return True

def validaHoraFinal(inicio, fim):
	horaInicio = inicio.split(':')
	horaI = int(horaInicio[0])
	minutoI = int(horaInicio[1])

	horaFim = fim.split(':')
	horaF = int(horaFim[0])
	minutoF = int(horaFim[1])
	if horaI == horaF:
		if minutoI >= minutoF:
			return False
		else:
			return True
	elif horaI > horaF:
		return False
	else:
		return True

def validaData(data):
	lista = data.split('/')
	if len(lista) != 3:
		return False
	for x in lista:
		if not x.isdigit():
	  		return False
	dia = int(lista[0])
	mes = int(lista[1])
	ano = int(lista[2])
	
	d = datetime.now()
	mesAtual = d.strftime('%m')
	mesAtual = int(mesAtual)
	anoAtual = d.strftime('%Y')
	anoAtual = int(anoAtual)
	diaAtual = d.strftime('%d')
	diaAtual = int(diaAtual)

	if mes < 1 or mes > 12:
		return False

	maxDia = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if bissexto(ano):
		maxDia[1] = 29

	if (dia < 1) or (dia > maxDia[mes-1]):
		return False

	if ano < anoAtual:
		return False
	elif ano == anoAtual:
		if mes == mesAtual:
			if dia >= diaAtual:
				return True
			else:
				return False
		elif mes > mesAtual:
			return True
		else:
			return False
	else:
		return True

def bissexto(ano):
	if ((ano % 4 == 0) and (ano % 100 != 0)) or (ano % 400 == 0):
		return True
	else:
		return False

def consultarCompromissos(compromissos):
	for consulta in compromissos:
		print('Título: %s \nAssunto: %s \nData do compromisso: %s \nHora do compromisso: %s \nHora do fim do compromisso: %s \nCadastrado em: %s' %(compromissos[consulta][0], compromissos[consulta][1], compromissos[consulta][2], compromissos[consulta][3], compromissos[consulta][4], compromissos[consulta][5]))
		print('-'*45 + '\n')

def cadastroBasico(compromissos):
	idCompromisso = consultarId()
	titulo = input('Título do compromisso  : ')
	assunto = input('Assunto do compromisso: ')
	d = datetime.now()
	dataCadastro = d.strftime('%d/%m/%Y - %H:%M:%S')
	valData = False
	while valData == False:
		dataCompromisso = input('Data (dd/mm/aaaa) do compromisso: ')
		valData = validaData(dataCompromisso)
		if valData == False:
			print('Digite uma data válida e utilize o formato dd/mm/aaaa.\n')
	
	#verifica a hora de inicio
	valHora = False	
	while valHora == False:
		horaCompromisso = input('Horário do compromisso (hh:mm): ')
		valHora = validaHora(horaCompromisso, dataCompromisso)
		if valHora == False:
			print('Digite uma data válida para a data informada e utilize o formato hh:mm\n')

	#verifica a hora de fim
	valHora = False
	while valHora == False:
		horaFimCompromisso = input('Horário do fim do compromisso (hh:mm): ')
		valHora = validaHora(horaFimCompromisso, dataCompromisso)
		if valHora == False:
			print('Digite uma hora válida para a data informada e utilize o formato hh:mm\n')
		else:
			valHoraFinal = validaHoraFinal(horaCompromisso, horaFimCompromisso)
			if valHoraFinal == False:
				print('Um compromisso não pode acabar antes que inicie, não acha? Tente novamente.\n')
				valHora = False

	#add no dicionario
	lista = [titulo, assunto, dataCompromisso, horaCompromisso, horaFimCompromisso, dataCadastro]
	compromissos[idCompromisso] = lista

	#add no .txt
	gravarArquivo(compromissos)
	print('\nAgenda atualizada!\n')
	return idCompromisso

def cadastrarCompromisso(compromissos):
	cadastroBasico(compromissos)

def dataNova(compromissos, idGerador, qteSemanas):
	for idGerador in compromissos:
		dataCompromisso = compromissos[idGerador][2]
	lista = dataCompromisso.split('/')
	dia = int(lista[0]) + 7
	mes = int(lista[1])
	ano = int(lista[2])
	maxDia = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	if bissexto(ano):
		maxDia[1] = 29
	if dia > maxDia[mes-1]:
		dia -= maxDia[mes-1]
		mes += 1
		if mes > 12:
			mes -= 12
			ano += 1

	lista[0] = str(dia)
	lista[1] = str(mes)
	lista[2] = str(ano)
	dataCompromisso = lista[0]+'/'+lista[1]+'/'+lista[2]

	return dataCompromisso

def geradorDeCompromissos(compromissos, idGerador, qteSemanas):
	#qteSemanas-1 pois já foi cadastrado um compromisso simples!!
	i = 1
	while i <= (qteSemanas-1):
		i += 1
		idCompromisso = consultarId()
		for idGerador in compromissos:
			titulo = compromissos[idGerador][0]
			assunto = compromissos[idGerador][1]
			dataCompromisso = dataNova(compromissos, idGerador, qteSemanas)
			horaCompromisso = compromissos[idGerador][3]
			horaFimCompromisso = compromissos[idGerador][4]
			dataCadastro = compromissos[idGerador][5]
		#add no dicionario
		lista = [titulo, assunto, dataCompromisso, horaCompromisso, horaFimCompromisso, dataCadastro]
		compromissos[idCompromisso] = lista

		#add no .txt
		gravarArquivo(compromissos)
	return idCompromisso

def painelCadastro(compromissos):
	print('1. Compromisso isolado \t2. Compromisso semanal\n')
	tipoCadastro = int(input('Como você deseja cadastrar seu compromisso?\n'))
	if tipoCadastro == 1:
		clear()
		cadastrarCompromisso(compromissos)
	elif tipoCadastro == 2:
		clear()
		qteSemanas = ''
		while not qteSemanas.isdigit():
			try:
				qteSemanas = int(input('Durante quantas semanas deseja repetir?\n'))
			except ValueError:
				clear()
				print('Digite um número de semanas!')
			qteSemanas = str(qteSemanas)
		qteSemanas = int(qteSemanas)
		idGerado = cadastroBasico(compromissos)
		geradorDeCompromissos(compromissos, idGerado, qteSemanas)
		print('\nEste compromisso irá se repetir durante %s semanas.'%qteSemanas)
	else:
		print('Inválido')
	

def editarCompromissos(compromissos):
	for consulta in compromissos:
		print('%s)' %consulta, compromissos[consulta][0], '-', compromissos[consulta][2])
	print('\n' * 2)
	opcaoEditar = input('Escolha o número do compromisso que deseja editar: ')

	if opcaoEditar in compromissos:
		clear()
		print('Ok, atualize os dados de %s' %compromissos[opcaoEditar][0])
		titulo = input('Título do compromisso  : ')
		assunto = input('Assunto do compromisso: ')
		d = datetime.now()
		dataCadastro = d.strftime('%d/%m/%Y - %H:%M:%S')
		valData = False
		while valData == False:
			dataCompromisso = input('Data (dd/mm/aaaa) do compromisso: ')
			valData = validaData(dataCompromisso)
			if valData == False:
				print('Digite uma data válida e utilize o formato dd/mm/aaaa.\n')

		#verifica a hora de inicio
		valHora = False	
		while valHora == False:
			horaCompromisso = input('Horário do compromisso (hh:mm): ')
			valHora = validaHora(horaCompromisso, dataCompromisso)
			if valHora == False:
				print('Digite uma data válida para a data informada e utilize o formato hh:mm\n')

		#verifica a hora de fim
		valHora = False
		while valHora == False:
			horaFimCompromisso = input('Horário do fim do compromisso (hh:mm): ')
			valHora = validaHora(horaFimCompromisso, dataCompromisso)
			if valHora == False:
				print('Digite uma hora válida para a data informada e utilize o formato hh:mm\n')
			else:
				valHoraFinal = validaHoraFinal(horaCompromisso, horaFimCompromisso)
				if valHoraFinal == False:
					print('Um compromisso não pode acabar antes que inicie, não acha? Tente novamente.\n')
					valHora = False

		#add no dicionario
		lista = [titulo, assunto, dataCompromisso, horaCompromisso, horaFimCompromisso, dataCadastro]
		compromissos[opcaoEditar] = lista
		print('\n' * 2)
		gravarArquivo(compromissos)
		print('Agenda atualizada!\n')
	else:
		print('Número do compromisso não encontrado.\n')

def excluirCompromissos(compromissos):
	for consulta in compromissos:
		#print id e titulo
		print('%s)' %consulta, compromissos[consulta][0], '-', compromissos[consulta][2])
	print('\n' * 2)
	opcaoExcluir = input('Escolha o nº do compromisso que deseja excluir: ')
	print()
	if opcaoExcluir in compromissos:
		confirma = input('Você realmente deseja EXCLUIR o compromisso "%s"? (s/n)\n'%compromissos[opcaoExcluir][0])
		confirma = confirma.lower()
		clear()
		if confirma == 's':
			print('Excluindo o compromisso "%s"...' %compromissos[opcaoExcluir][0])
			del compromissos[opcaoExcluir]
			gravarArquivo(compromissos)
			print('\nAgenda atualizada!\n')
		elif confirma == 'n':
			print('Ok, cancelando...\n')
			pass
		else:
			print('Opção inválida!\n')
	else:
		print('Número do compromisso não encontrado.\n')

def encerrarPrograma(nome):
		print('Até mais, %s! Saindo...'%nome)
		continua = False
		return continua
