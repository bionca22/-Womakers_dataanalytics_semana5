import sqlite3

connection = sqlite3.connect('escola')
cursor = connection.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id
#(inteiro), nome (texto), idade (inteiro) e curso (texto)
""" 
cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100),idade INT, curso VARCHAR(100))') 
"""

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no
#exercício anterior.
""" 
cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(1,"Cleiton","17", "violão"),(2,"Nelson","19", "Vôlei"),(3,"Ana","16", "Vôlei"),(4,"Amanda","15", "pintura"),(5,"Ricardo","17", "costura")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(6,"Cláudia","32", "Saxofone")')
cursor.execute('INSERT INTO alunos(id,nome,idade,curso)VALUES(7,"Matheus","22", "engenharia"),(8,"Bianca","19", "engenharia")')
"""

#3. Consultas Básicas. Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos"
"""
date = cursor.execute('SELECT * FROM alunos')
for alunos in date:
    print(alunos)  """

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos
"""
date = cursor.execute('SELECT * FROM alunos WHERE idade > 20')
for alunos in date:
    print(alunos)  """

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética
""" 
date = cursor.execute('SELECT nome FROM alunos ORDER BY nome ')
for alunos in date:
    print(alunos) 
"""

#d) Contar o número total de alunos na tabela
""" 
date = cursor.execute('SELECT COUNT(*) FROM alunos')
for alunos in date:
    print(alunos)  """

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela
""" cursor.execute('UPDATE  alunos SET idade = 18 WHERE id = 1') 

"""

#b) Remova um aluno pelo seu ID
""" cursor.execute('DELETE FROM alunos where id = 6')
"""

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 
#Insira alguns registros de clientes na tabela.
""" cursor.execute('CREATE TABLE clientes (id INTEGER NOT NULL PRIMARY KEY, nome VARCHAR(100),idade INT, saldo FLOAT)') 
"""
""" cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1,"Anastácia", "40", "26353.00"),(2,"Paulo", "23", "6474.00"), (3,"Ana","19", "63721.00"),(4,"Fabiana","18", "3333.00"),(5,"Henrrique","55", "94339.00")') """
#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
""" date = cursor.execute('SELECT * FROM clientes WHERE idade > 30')
for cliente in date:
    print(cliente) """

#b) Calcule o saldo médio dos clientes
""" date = cursor.execute('SELECT AVG(saldo) FROM clientes ')
for clientes in date:
    print(clientes) """

#c) Encontre o cliente com o saldo máximo.
""" date = cursor.execute('SELECT MAX(saldo) FROM clientes ')
for clientes in date:
    print(clientes) """

#d) Conte quantos clientes têm saldo acima de 1000.
""" date = cursor.execute('SELECT * FROM clientes  WHERE saldo > 1000')
for clientes in date:
    print(clientes)  """

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico
""" cursor.execute('UPDATE clientes SET saldo = 1000 WHERE id = 2') 
"""

#b) Remova um cliente pelo seu ID.
""" cursor.execute('DELETE FROM clientes where id=1')

connection.commit()
connection.close """

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o
#valor de cada compra.

""" cursor.execute('CREATE TABLE compras (id SERIAL PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor INT, FOREIGN KEY (cliente_id) REFERENCES clientes(id))') 
"""
""" cursor.execute('INSERT INTO compras (cliente_id, produto, valor) VALUES (1, "batatas", "10.50"), (2, "azeite", "20.75"), (1, "Brusinha", "15.20"), (3, "Melancia", "30.00")')
 """
#código para debugg
""" cursor.execute('DROP TABLE compras') """

""" dates = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM compras JOIN clientes ON compras.cliente_id = clientes.id')
for clientes in dates:
    print(clientes)
 """

connection.commit()
connection.close
