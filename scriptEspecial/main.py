import sqlite3

conn = sqlite3.connect('rpi_base.db')
cursor = conn.cursor()

# inseridos apenas uma vez no inicio do arquivo
rpi = int(input())  
ano = int(input()) 

listaResultado = [] # lista geral
listaRegistro = [] # lista por registro


while True:
    n = input() # processo ou variável de teste

    if n == "parou": # condição de parada
        break
    else:
        listaRegistro.append(rpi) # adiciona a edição da RPI fixo de cada registro
        listaRegistro.append(ano) # adiciona o ano da edição da RPI fixo em cada registro
        
        # apenas para o processo
        for k in range(len(n)): # faz a separação a partir dos dois pontos como delimitador.
            if n[k] == ':': 
                aux = n[k+2:]
        listaRegistro.append(aux)
        
        # titulo, titular, criador, linguagem, caplicacao, tprograma, data
        
        for i in range(7): 
            a = input()
            aux = ""
            for k in range(len(a)):
                if a[k] == ':': # faz a separação a partir dos dois pontos como delimitador.
                    aux = a[k+2:]

            # formatar e contar nomes NÃO FUNCIONA AINDA, REVER. 
            
            """if (i==2):
                contador = 0
                lista2 = []
                if(";" in aux):
                    novo = aux.split('; ')
                    for i in novo:
                        if (i not in lista2):
                            lista2 += i
                    aux = "; ".join(lista2)
                    contador = len(lista2)
                else:
                    contador = 1
            """    

            # formatar data para ir apenas o ano
            if (i==6):
                aux = int(aux[6:])
        
            listaRegistro.append(aux)

            #listaRegistro.append(contador) # contador de criadores
        listaResultado.append(tuple(listaRegistro)) # transforma em tupla
        listaRegistro = []

    print(listaResultado) 

# inserindo dados na tabela
cursor.executemany("""
    INSERT INTO tb_rpi(n_rpi, ano_rpi, processo, titulo, titular, criador, linguagem, campo_aplicacao, tipo_programa, data)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", listaResultado)

conn.commit()
print("dados inseridos com sucesso")

conn.close()
