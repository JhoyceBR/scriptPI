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

            # formatar data para ir apenas o ano
            if (i==6):
                try:
                    avaliar = aux[6:]
                    avaliar = int(avaliar)
                    aux = aux[6:]
                except:
                    aux = "Não informado"

            listaRegistro.append(aux)

            
        # contador de nomes e corretor de repetição
        listafrequencia = []
        nomes = listaRegistro[5]

        if (';' not in nomes):
            contador = 1
        else:
            nomes = nomes.split('; ')
            for N in nomes:
                if (N not in listafrequencia):
                    listafrequencia.append(N)
                else:
                    pass
            contador = len(listafrequencia)
            listaRegistro[5] = "; ".join(listafrequencia) # substitui na lista caso haja repetição
        
        listaRegistro.append(contador)

        listaResultado.append(tuple(listaRegistro)) # transforma em tupla
        listaRegistro = []

    print(listaResultado) 

# inserindo dados na tabela
cursor.executemany("""
    INSERT INTO tb_rpi(n_rpi, ano_rpi, processo, titulo, titular, criador, linguagem, campo_aplicacao, tipo_programa, data, qtd_criadores)
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", listaResultado)

conn.commit()
print("dados inseridos com sucesso")

conn.close()
