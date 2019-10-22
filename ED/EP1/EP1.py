## Arthur Barbero ; Leandro Lopes - Turma A ADS 3º semestre
import time
from random import randint
import timeit
import sys

sys.setrecursionlimit(99999)

#-----------Defs---------------
def seleção(x):
    i = 0
    a = 0
    while i< len(x): 
        for lista in range(len(x)-1):
            if x[a] < x[lista]:
                x[a], x[lista] = x[lista], x[a]
                

        i = i +1
        a = a +1

def merge(e, d):
    r = []
    i, j = 0, 0
    while i < len(e) and j < len(d):
        if e[i] <= d[j]:
            r.append(e[i])
            i += 1
        else:
            r.append(d[j])
            j += 1
    r += e[i:]
    r += d[j:]
    return r

def mergesort(v):
    if len(v) <= 1:
        return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)


def quicksort(lista):
    if len(lista)<=1:
        return lista

    pivô = lista[0]
    iguais = [x for x in lista if x == pivô]
    menores = [x for x in lista if x < pivô]
    maiores = [x for x in lista if x > pivô]
    return quicksort(menores) + iguais + quicksort(maiores)

def timer(x, sort):
    ini = time.perf_counter()
    sort(x)
    fim = time.perf_counter()
    result = float(fim-ini)
    return result

#-----------Main------------------
vetor = []
for x in range(22000):
    vetor.append(randint(1,22000))



print("\t\t\tTeste de velocidade Time's")
print("Número de elementos\tMergesort\tQuicksort\tSelection\tNative")
i = 5000
while i<=25000:
    print(f'{i}\t\t\t {timer(vetor[:i+1], mergesort):.6f}\t{timer(vetor[:i+1], quicksort):.6f}\t{timer(vetor[:i+1], seleção):.6f}\t {timer(vetor[:i+1],sorted):.6f}')
    i = i +5000
    

