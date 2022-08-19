import psycopg2

lista = ["Cereias, pães e tubérculos",
"Hortaliças",
"Frutas",
"Leguminosas",
"Carnes e ovos",
"Leite e derivados",
"Óleos e gorduras",
"Açúcares e doces"]


con = psycopg2.connect(host='localhost', database='acomidadobebe',
user='postgres', password='12345')
cur = con.cursor()
for i in lista:
    sql = "insert into tb_grupo(nome_grupo) values ('%s')"%(i)
    cur.execute(sql)
    con.commit()

cur.execute('select * from tb_grupo')
recset = cur.fetchall()
for rec in recset:
    print (rec)
con.close()
