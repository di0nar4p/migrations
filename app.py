from Controller.conexao import connect


conexao= connect()

conn= conexao.cursor()

idade = 29
query = (f"INSERT INTO Alunos (nome, idade) VALUES('Glauco',{idade})")
#query = (f'''''')
conn.execute(query)
conexao.commit()
conn.execute("SELECT * FROM Alunos")
registros= conn.fetchall()
request=[]
for row in registros:
    print(row)