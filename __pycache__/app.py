from flask import Flask,request,render_template, session
#from markupsafe import escape
#import urllib.request, json 
import sqlite3
import re
# from random import randomint

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):
 
	# pass the regular expression
	# and the string into the fullmatch() method
	if(re.fullmatch(regex, str(email))):
		return True 
 
	else:
		return False

app = Flask(__name__)
app.secret_key = 'nao sei'

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

@app.route("/apagar/", methods=['POST','GET'])

def apagar():

	matricula_del = request.form.get('matricula_del')


	if request.method == 'POST' and matricula_del and len(matricula_del) > 0:
		matricula_del = int(matricula_del)
		arq = open('dados.csv','r')
		saida = ""
		for linha in arq:
			linha = linha.split(';')
			if int(linha[0]) != matricula_del:
				linha = linha[0]+";"+linha[1]
				saida+=linha
		arq.close()
		arq = open('dados.csv','w')
		arq.write(saida)
		arq.close
		return render_template('apagada.html',matricula_del=matricula_del)
	
	return render_template('apagar-matricula.html',matricula_del=matricula_del)
	
# @app.route("/apagar/", methods=['POST', 'GET'])
# def apagar():
#     matricula_del = request.form.get('matricula_del')

#     if request.method == 'POST' and matricula_del and len(matricula_del) > 0:
#         matricula_del = int(matricula_del)
#         saida = ""
		
#         # Using 'with' to ensure the file is closed properly
#         with open('dados.csv', 'r') as arq:
#             for linha in arq:
#                 linha = linha.strip().split(';')
#                 if int(linha[0]) != matricula_del:
#                     saida += linha[0] + ";" + linha[1] + "\n"

#         with open('dados.csv', 'w') as arq:
#             arq.write(saida)
		
#         return render_template('apagada.html', matricula_del=matricula_del)
	
#     return render_template('apagar-matricula.html', matricula_del=matricula_del)


# @app.route("/variaveis", methods=['POST','GET'])
# def usando_variaveis():
# 	matricula = request.form.get('nova_matricula')
# 	aluno = request.form.get('novo_aluno')
# 	'''
# 	print("---------------")
# 	print(matricula, aluno)
# 	print("---------------")
# 	'''
# 	chamada = le_arquivo()
# 	if request.method == 'POST' and len(matricula) > 0:
# 		#chamada[matricula] = aluno #adicionado no dicionario
# 		chamada[matricula] = aluno
# 		salva_dados(matricula,aluno)
		
# 	return render_template('variaveis.html',chamada=chamada)

@app.route("/cadastro", methods=['POST', 'GET'])
def cadastrar():
	print("request.form",request.form)
	nome = email = senha = None
	nome = request.form.get("novo_usuario")
	email = request.form.get("novo_email")
	senha = request.form.get("nova_senha")
	if request.method == 'POST':
		# Verifica se os campos estão preenchidos
		if not nome or not email or not senha:
		# if len(nome) == 0 or len(email) == 0 or len(senha) == 0:
			mensagem_cadastro = "Todos os campos são obrigatórios!"
			return render_template('cadastro.html', mensagem=mensagem_cadastro)

		# Verifica se o email é válido
		if not check(email):
			mensagem_cadastro = "E-mail inválido!"
			return render_template('cadastro.html', mensagem=mensagem_cadastro)

		# Conecta ao banco de dados
		Conexao = sqlite3.connect("Banco_de_Dados.db")
		Cursor = Conexao.cursor()
		
		# Cria a tabela se não existir
		Cursor.execute("""CREATE TABLE IF NOT EXISTS Usuarios (
							ID INTEGER PRIMARY KEY AUTOINCREMENT, 
							Name TEXT NOT NULL, 
							Password TEXT NOT NULL,
							Email TEXT NOT NULL UNIQUE
						)""")

		# Verifica se o nome de usuário ou o email já existem no banco de dados
		verificar_nome = Cursor.execute("SELECT Name FROM Usuarios WHERE Name = ?", (nome,)).fetchone()
		verificar_email = Cursor.execute("SELECT Email FROM Usuarios WHERE Email = ?", (email,)).fetchone()

		if verificar_nome is not None:
			mensagem_cadastro = "Nome de Usuário já existe!"
			Conexao.close()
			return render_template('cadastro.html', mensagem=mensagem_cadastro)

		elif verificar_email is not None:
			mensagem_cadastro = "Email de usuário já está em uso!"
			Conexao.close()
			return render_template('cadastro.html', mensagem=mensagem_cadastro)

		else:
			# Insere o novo usuário no banco de dados
			Cursor.execute('INSERT INTO Usuarios (Name, Password, Email) VALUES (?, ?, ?)', (nome, senha, email))
			Conexao.commit()
			mensagem_cadastro = "Novo usuário adicionado com sucesso!"
		
		# Fecha a conexão com o banco de dados
		Conexao.close()
	else:
		mensagem_cadastro =''
	return render_template('cadastro.html', mensagem=mensagem_cadastro)

@app.route("/login", methods=['POST', 'GET'])
def logar():
	# email = request.form.get("login_email")
	nome = request.form.get("login_usuario")
	senha = request.form.get("login_senha")	
	if request.method == 'POST': # and len(nome) > 0 and len(senha) > 0:
		print("dentro do if")
		Conexao = sqlite3.connect("Banco_de_Dados.db")
		Cursor = Conexao.cursor()
		Cursor.execute("""CREATE TABLE IF NOT EXISTS Usuarios (
							ID INTEGER PRIMARY KEY AUTOINCREMENT, 
							Name TEXT NOT NULL, 
							Password TEXT NOT NULL,
							Email TEXT NOT NULL UNIQUE
						)""")
		verificar_nome = Cursor.execute("SELECT Name FROM Usuarios WHERE Name = ?", (nome,)).fetchone()
		verificar_senha = Cursor.execute("SELECT Password FROM Usuarios WHERE Password = ?", (senha,)).fetchone()
		# if verificar_nome a
		print("verificar nome e senha", verificar_nome, verificar_senha)
	# else:
	# 	print(request.method)

#AULA DO PRISCO
	# session['nome'] = "Aluno"
	# return(f"oi {session['nome']}")


	return render_template('login.html')

@app.route("/sobre")
def sobre():
	saida = "<h1>OIOIOIOIOI</h1><br>" *100
	return(saida)
