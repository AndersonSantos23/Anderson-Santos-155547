matricula = 542642

def apagar(matricula):
	arq = open('dados.csv','r')
	saida = ""
	for linha in arq:
		linha = linha.split(';')
		if int(linha[0]) != matricula:
			linha = linha[0]+";"+linha[1]
			saida+=linha
	arq.close()
	arq = open('dados.csv','w')
	arq.write(saida)
	arq.close
	return "feito!"

apagar(matricula)