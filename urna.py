print('1 - Ler aquivo de candidatos \n2 - Ler arquivo de eleitores \n3 - Iniciar votação \n4 - Apurar votos \n5 - Mostrar resultados \n6 - Fechar programa')



def lerEleitor():
	voterData = input('Informe a localização dos dados dos eleitores:')
	arq = open(voterData, 'r')
	linhas = arq.readlines()
	for linha in linhas:
         linhaProcessada = linha.strip().split(',')
         print(linhaProcessada)

def lerCanditato():
	candidateData = input('Informe a localização dos dados dos candidatos:')
	arq = open(candidateData, 'r')
	linhas = arq.readlines()
	for linha in linhas:
         linhaProcessada = linha.strip().split(',')
         print(linhaProcessada)
		 


def iniciarVotacao():
	local = input('UF onde está localizada a urna:')
	
    

def controleExecucao():
	option = int(input())
	if option == 1:
		lerCanditato()
	elif option == 2:
		lerEleitor()
	elif option == 3:
         iniciarVotacao()



controleExecucao()

# for linha in linhas:
# 	linhaProcessada = linha.strip().split(',')
# 	eleitor = linhaProcessada

# print(eleitor)
