# Programa que faz a contagem da frequência de um dos campos da tabela
# serve para Campo, Tipo e linguagem.

arquivo = open('saida1.txt', 'w')
freq_nums = {}


while True:
    n = input().split(',')
    contador = 0
    if n[0] == "parou":
        break
    else:
        contador += 1
        for k in n:
            if k in freq_nums:
                freq_nums[k] += 1
            else:
                freq_nums[k] = 1

for o in freq_nums:
    t = ((o, freq_nums[o]))
    print(t, file=arquivo)
arquivo.close()
