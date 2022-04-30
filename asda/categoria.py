import sqlite3

conn = sqlite3.connect('rpi.db')
cursor = conn.cursor()

def localiza_registro(id):
    r = cursor.execute(
        'SELECT id_registro, criador, sexo FROM tb_rpi WHERE id_registro = ?', (id,))
    return r.fetchone()

def atualiza_sexo(categoria, id):
    r = cursor.execute(
        'update tb_rpi set sexo=? where id_registro=?', (categoria, id))
    conn.commit()
    

indice = int(input("indice: "))
print(localiza_registro(indice))
print("1 para apenas homens")
print("2 para mulheres e homens")
print("3 para apenas mulheres")
print("4 para não é possível identificar")
print("5 para pessoa juridica")
categoria = int(input("digite categoria: "))
print()

if (categoria==1):
    atualiza_sexo("Apenas homens", indice)
elif (categoria==2):
    atualiza_sexo("Ao menos 1 mulher", indice)
elif (categoria==3):
    atualiza_sexo("Apenas mulheres", indice)
elif (categoria==4):
    atualiza_sexo("Não é possível identificar", indice)
elif (categoria==5):
    atualiza_sexo("Pessoa juridica", indice)
    
print(localiza_registro(indice))

while True:
    if (indice == 0):
        break
    else:
        continua = input("digite s para continuar: ")
        print()
        if (continua == 's'):
            indice+=1
            print(localiza_registro(indice))
            print("1 para apenas homens")
            print("2 para mulheres e homens")
            print("3 para apenas mulheres")
            print("4 para não é possível identificar")
            print("5 para pessoa juridica")
            categoria = int(input("digite categoria: "))
            print()

            if (categoria==1):
                atualiza_sexo("Apenas homens", indice)
            elif (categoria==2):
                atualiza_sexo("Ao menos 1 mulher", indice)
            elif (categoria==3):
                atualiza_sexo("Apenas mulheres", indice)
            elif (categoria==4):
                atualiza_sexo("Não é possível identificar", indice)
            elif (categoria==5):
                atualiza_sexo("Pessoa juridica", indice)

            print(localiza_registro(indice))
        else:
            conn.close()
            break




