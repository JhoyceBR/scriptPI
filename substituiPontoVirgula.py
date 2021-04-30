# Programa que verifica se as linguagens estão separadas por ponto e vírgula 
# se sim, substitui para vírgula para estar pronto a passar no contador.

arquivo = open('saida.txt', 'w')
while True:
    nova = ""
    n = input()
    if n == 'parou':
        break
    else:
        for i in range(0, len(n)):
            if n[i] != ";":
                nova += n[i]
                
            else:
                nova += ","
        arquivo.write(nova)
        arquivo.write("\n")
        
arquivo.close()
