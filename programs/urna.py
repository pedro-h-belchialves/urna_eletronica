from read_candidatos import ler_candidatos
from read_eleitores import ler_eleitores
from voting import iniciarVotacao

candidatos_urna  = []
eleitores_urna = []

def lerEleitor():
	# voterData = input('Informe a localização dos dados dos eleitores:')
	eleitores = ler_eleitores('data\eleitor.txt')
	eleitores_urna.append(eleitores)
	controleExecucao()
	
def lerCanditato():
	# arquivo_candidatos = input('Informe a localização dos dados dos candidatos:')
	candidatos = ler_candidatos('data\candidato.txt') #'data\candidato.txt'
	candidatos_urna.append(candidatos)
	controleExecucao()
	  
# play_urna = True
# while play_urna == True:
def controleExecucao():
	print('\n\n\n1 - Ler aquivo de candidatos \n2 - Ler arquivo de eleitores \n3 - Iniciar votação \n4 - Apurar votos \n5 - Mostrar resultados \n6 - Fechar programa')
	option = int(input())
	if option == 1:
		lerCanditato()
	elif option == 2:
		lerEleitor()
	elif option == 3:
		iniciarVotacao(candidatos_urna[0], eleitores_urna[0])



controleExecucao()
