rpi = int(input()) # a entrada da edição é apenas uma vez. Programar para ler a edição em um arquivo in
ano = int(input()) # ano da publicação da revista
listaResultado = [] # lista contendo todos os registros já filtrados
listaRegistro = [] # lista por registro

while True:
    n = input() # processo ou variável de teste

    if n == "parou": # condição de parada
        break
    else:
        listaRegistro.append(rpi) # adiciona a edição da RPI fixo de cada registro
        listaRegistro.append(ano) # adiciona o ano da edição da RPI fixo em cada registro

        for i in range(7): # para a entrada dos campos de processo, titulo, titular, criador, linguagem, campo, tipo e data.
            a = input()
            aux = ""
            for k in range(len(a)):
                if a[k] == ':': # faz a separação a partir dos dois pontos como delimitador.
                    aux = a[k+2:]

        
            listaRegistro.append(aux)
        listaResultado.append(listaRegistro)
        listaRegistro = []

    print(listaResultado) # modificar formato de saída 

# todos os arquivos de entrada deve conter cada campo em uma linha correspondente. 
# cada revista deve ser avaliada em um in e contida no out do ano
# pode complementar retirando os nomes repetidos 
# aprimorar fazendo a contagem geral dos campos, tipos de programa e linguagens, integrando com os outros algoritmos
# achar uma forma de formatar a saída de forma correta para apenas passar para a planilha
# estudar como fazer a saída ir direto para a planilha
# estudar como formatar datas em python e ver se existe biblioteca para tal
# até aqui, cada registro fica dentro de uma lista própria, diferenciando-se entre os outros. 