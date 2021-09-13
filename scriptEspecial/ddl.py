import sqlite3

conn = sqlite3.connect('rpi.db')

cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE tb_rpi(
        id_registro INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        n_rpi INTEGER NOT NULL,
        ano_rpi TEXT,
        processo TEXT,
        titulo TEXT,
        titular TEXT,
        criador TEXT,
        linguagem TEXT,
        campo_aplicacao TEXT,
        tipo_programa TEXT,
        data INTEGER,
        qtd_criadores INTEGER
    );
""")
print('tabela tb_rpi criada com sucesso')

conn.close()