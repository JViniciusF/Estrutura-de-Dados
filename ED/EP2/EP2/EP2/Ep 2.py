def enumerações(x):
    menor = 999999999999
    i=0
    casamentos=[]
    y = x
    pior=[]
    if len(x) <= 1:
        return print(f"Dá para casar {mulheres}")
    else:
        for t in y:
            for t in x:
                if menor > len(x[t]) and t not in pior:
                    w = t
                    menor = len(x[t])
            pior.append(w)
            for t in x:
                if t==pior[-1]:
                    casamentos.append(f"{t,x[t]}")
                if t != pior[-1]:
                    if len(x[t]) ==0:
                        return print(f"Não é possível casar todas as damas, retirando as possibilidades, a dama {t} ficará sem cavaleiro\ncasamentos encontrados: \n{casamentos}")
                    else:
                        for u in x[t]:
                            if u in x[pior[-1]]:
                                x[t].remove(u)
            
            menor = 999999999999
    print(f"Dá pra casar, seguinte maneira: {casamentos}")
                 
def permutações(x):
    lista = []
    for t in x:
        if t not in lista:
            lista.append(t)
        for u in x[t]:
            if u not in lista:
                lista.append(u)
                for u in x[u]:
                    if u not in lista:
                        lista.append(u)
                        for u in x[u]:
                            if u not in lista:
                                lista.append(u)
                                for u in x[u]:
                                    if u not in lista:
                                        lista.append(u)
                                        for u in x[u]:
                                            if u not in lista:
                                                lista.append(u)
                                                for u in x[u]:
                                                    if u not in lista:
                                                        lista.append(u)
                                                        for u in x[u]:
                                                            if u in t:
                                                                return print(f"Será possível sentar os cavaleiros da seguinte forma:\n{lista}")
                                                        return print("Não é possivel sentar todos os cavaleiros sem dar briga")
    
                
                    
                
        
        
print("Alunos: Arthur Barbero; Leandro Lopes - ADS 3º semestre Turma A\n\n")
mulheres= {}
z=[]
arq = open('casamento.txt','r')
x = arq.read().split("\n")


for t in x:
    z.append(t.split(" "))

for t in z:
    mulheres[t[0]] = t[1:]

  
enumerações(mulheres)
print("---------------------------------")
cavaleiros={}
z=[]
arq = open('cavaleiros.txt','r')
x = arq.read().split('\n')

for t in x:
    z.append(t.split(" "))

for t in z:
    cavaleiros[t[0]] = t[1:]

permutações(cavaleiros)
