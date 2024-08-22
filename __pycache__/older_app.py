from flask import Flask,request,render_template
#from markupsafe import escape
#import urllib.request, json 

app = Flask(__name__)

def le_arquivo():
	arq = open('dados.csv','r')
	dados = arq.readlines()
	saida = {}
	for linha in dados:
		linha = linha[:-1].split(';')
		saida[linha[0]] = linha[1]
	return saida

def salva_dados(matricula,nome):
	arq = open('dados.csv','a')
	arq.write(f"{matricula};{nome}\n")	
	arq.close()

@app.route("/")
def alo_mundo():
	nome = "João"
	teste = ['a','b','c']
	return render_template('index.html',nome=nome,teste=teste)

@app.route("/cumprimenta/<nome>")
def diz_oi(nome):
	return("oi, " + nome)

@app.route("/apaga/<int:matricula>", methods=['POST','GET'])
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
	return render_template('apagar-matricula.html',matricula=matricula)
## REVER FUNÇÃO

@app.route("/variaveis", methods=['POST','GET'])
def usando_variaveis():
	matricula = request.form.get('nova_matricula')
	aluno = request.form.get('novo_aluno')
	'''
	print("---------------")
	print(matricula, aluno)
	print("---------------")
	'''
	chamada = le_arquivo()
	if request.method == 'POST' and len(matricula) > 0:
		#chamada[matricula] = aluno #adicionado no dicionario
		chamada[matricula] = aluno
		salva_dados(matricula,aluno)
		
	return render_template('variaveis.html',chamada=chamada)

@app.route("/sobre")
def sobre():
	saida = "<h1>OIOIOIOIOI</h1><br>" *100
	return(saida)
