# Programa que dá o resultado do item e da contagem separados para a formatação
# e colocação na planilha.

la = [] # lista do item 
lb = [] # lista da contagem 

while True:
    try:
        l = input().split(', ') # separa os valores
        a = l[0]
        b = l[1]
        la.append(a)
        lb.append(b)

    except:
        break
s = ''    
for i in range(len(la)): # imprime o item
    s = la[i]
    print(s)

for o in range(len(lb)): # imprime a contagem
    print(lb[o])
