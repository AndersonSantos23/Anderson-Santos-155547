import sqlite3
import re
# from random import randomint

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        return True 
 
    else:
        return False

Conexao = sqlite3.connect("Banco_de_Dados.db")

Cursor = Conexao.cursor()
# cria tabela
# Cursor.execute("""CREATE TABLE Livros (
#                ID integer, 
#                Title text, 
#                Author text
#                )""")



# Cursor.execute(' INSERT INTO Livros VALUES (1, "Dune", "Frank Herbert")')
# Cursor.execute(' INSERT INTO Livros VALUES (2, "The Lord of the Rings", "J.R.R. Tolkien")')
# Cursor.execute(' INSERT INTO Livros VALUES (3, "Foundation", "Isaac Asimov")')
# Cursor.execute(' INSERT INTO Livros VALUES (4, "The Mists of Avalon", "Marion Zimmer Bradley")')
# Cursor.execute(' INSERT INTO Livros VALUES (5, "The Hobbit", "J.R.R. Tolkien")')
# Cursor.execute(' INSERT INTO Livros VALUES (6, "The Chronicles of Arthur", "Bernard Cornwell")')

# Conexão.commit() salva as modificações
# Conexao.commit()

# Consulta = Cursor.execute('SELECT * FROM Livros').fetchall()
# print(Consulta)

# for linha in Consulta:
#     print(linha)

# print(Cursor.execute('SELECT * FROM Livros WHERE Author="J.R.R. Tolkien"').fetchall())



Cursor.execute("""CREATE TABLE IF NOT EXISTS Usuarios (
               ID integer, 
               Name text, 
               Password text,
               Email text
               )""")
Conexao.commit()
Cursor.execute(' INSERT INTO Usuarios VALUES (1, "Joãozinho", "123", "joaozinho@gmail.com")')
# print(Cursor.execute('SELECT * FROM Usuarios').fetchone())

def new_user():
    nome = input("insira nome: ")
    senha = input("insira senha: ")
    email = input("insira email: ")
    # Conexao.execute()
    print(check(email))
    if nome != '' and senha != '' and check(email):
        verificar_nome = Cursor.execute("SELECT Name FROM Usuarios WHERE Name = ?", (nome,)).fetchone()
        verificar_email = Cursor.execute("SELECT Email FROM Usuarios WHERE Email = ?", (email,)).fetchone()
        print(f"usuario {verificar_nome}\nemail {verificar_email}\n")
        if verificar_nome is not None:
            print("nome de usuário já existe!")
        elif verificar_email is not None:
            print('email de usuário já está em uso!')
        else:
            # Insert the new user into the database
            Cursor.execute('INSERT INTO Usuarios (Name, Password, Email) VALUES (?, ?, ?)', 
                            (nome, senha, email))
            Conexao.commit()
            print("Novo usuário adicionado com sucesso!")            

    # Conexao.close()

# new_user()
#print(check('andersonsantos@google.com')) # funciona
print("Usuarios",Cursor.execute('SELECT * FROM Usuarios').fetchall())
print("Livros",Cursor.execute('SELECT * FROM Livros').fetchall())

Conexao.close()