def iniciarVotacao(candidatos_urna, eleitores_urna ):
	local = input('UF onde está localizada a urna:')
	
	candidatos_local = []
	eleitor_local = []
	candidatos_votados = []

	for candidado in candidatos_urna:
		if candidado['estado'] == local or candidado['cargo'] == 'P' :
			candidatos_local.append(candidado)

	for eleitor in eleitores_urna:
		if eleitor['estado'] == local:
			eleitor_local.append(eleitor)

	# print(eleitor_local[0])
	titulo = input('Informe o título do eleitor:')
	
	for voto in eleitor_local:

		if voto['titulo'] == titulo:
			print('Eleitor: ', voto['nome'],'\nEstado: ', voto['estado'])

			voto_dep_fed = input('Informe o voto para deputado federal:')

			for deputado in candidatos_local:
				if deputado['numero'] == voto_dep_fed:
					print('Candidato: ', deputado['nome'],'|', deputado['partido'])
					confirma = input('Confirma (S ou N)?')
					if confirma == "S":
						candidatos_votados.append(deputado)

	print(candidatos_votados)



   
		