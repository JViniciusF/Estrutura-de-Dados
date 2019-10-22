#Imports
import time
import timeit
from random import randint
from copy import deepcopy

#Definicoes de funcoes
def insercao(v):

  for j in range(1, len(v)):
    x = v[j]
    i = j - 1
    while i >= 0 and v[i] > x:
      v[i+1] = v[i]
      i = i - 1
    v[i + 1] = x
  return v

    
def selecao(v):
      r = []
      while v:
        m = min(v)
        r.append(m)
        v.remove(m)
      return r


        
def mergesort(v):
    if len(v) <= 1: return v
    else:
        m = len(v) // 2
        e = mergesort(v[:m])
        d = mergesort(v[m:])
        return merge(e, d)


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


def quicksort(v):
        if len(v) <= 1: return v
        
        pivô = v[0]
        iguais  = [x for x in v if x == pivô]
        menores = [x for x in v if x <  pivô]
        maiores = [x for x in v if x >  pivô]
        return quicksort(menores) + iguais + quicksort(maiores)

def Tempo(funcao , v):

    inicio = timeit.default_timer()
    funcao(v) 
    fim = timeit.default_timer()
    resultado = fim - inicio
    return resultado


def busca_sequencial(x, v):
    for i in range(len(v)):
        if v[i] == x:
            return i
    return -1

def tempo_sequencial(x,v):
    inicio = timeit.default_timer()
    busca_sequencial(x,v) 
    fim = timeit.default_timer()
    resultado_seq = fim - inicio
    return resultado_seq

cont = 0
def busca_binaria(x, v):
  global cont
  e = -1
  d = len(v)
  while e < d-1:
    m = (e + d) // 2
    cont = cont + 1
    if v[m] < x:
      e = m
    else:
      d = m
  return d

def tempo_binario(x,v):
    inicio = timeit.default_timer()
    busca_binaria(x,v) 
    fim = timeit.default_timer()
    resultado_binario = fim - inicio
    return resultado_binario


#Menu
print("""
|-------------------------[EP1 - Vale a pena ordenar?]--------------------------------------------|
|             Algoritmo escolhido: todos  Duracao dos testes: 30.00                               |
|                                                                                                 |
|         Alunos: Jose Vinicius Ferreira Santana
|                                                                                                 |
|               Tempos de Ordenacao               Numero de Buscas                                |
|-------------------------------------------------------------------------------------------------|
|                                                                                                 |
|         Insercao Selecao  Merge. Quick. Sort Nativo | Insercao Selecao Merge. Quick. Sort Nativo|
|-------|-----------------------------------------------------------------------------------------|""")


#Iniciando vetores
vetor = []
for x in range (5000):
  vetor.append(randint(1,5000))

VetIns = deepcopy (vetor)
VetSel = deepcopy(vetor)
VetMerg = deepcopy(vetor)
VetQuick = deepcopy(vetor)
VetNative = deepcopy(vetor)


contador = 5000

#Main
while (True):    
  
  #insercao
  tI = Tempo(insercao,VetIns)
  cont_I = 0
  tempo_I = 0

  while tempo_I <= tI :
    cont_I += 1
    randomico = randint(1,contador)
    tsI = tempo_sequencial(randomico , VetIns)
    tbI = tempo_binario(randomico, VetIns)
    tempo_I = tempo_I + (tsI-tbI)


  #Selecao
  tS = Tempo(selecao , VetSel)
  cont_S = 0
  tempo_S = 0
  
  while tempo_S <= tS :
    cont_S += 1
    randomico = randint(1,contador)
    tsS = tempo_sequencial(randomico , vetor[:])
    tbS = tempo_binario(randomico, vetor[:])
    tempo_S = tempo_S + (tsS-tbS)

  #MergeSort
  tM = Tempo(mergesort , VetMerg)
  cont_M = 0
  tempo_M = 0
  
  while tempo_M <= tM :
    cont_M += 1
    randomico = randint(1,contador)
    tsM = tempo_sequencial(randomico , VetMerg)
    tbM = tempo_binario(randomico, VetMerg)
    tempo_M = tempo_M + (tsM-tbM)
    

  #QuickSort
  tQ = Tempo(quicksort , VetQuick)
  cont_Q = 0
  tempo_Q = 0
  
  while tempo_Q <= tQ :
    cont_Q += 1
    randomico = randint(1,contador)
    tsQ = tempo_sequencial(randomico , VetQuick)
    tbQ = tempo_binario(randomico, VetQuick)
    tempo_Q = tempo_Q + (tsQ-tbQ)

  #Sort Nativo
  tSN = Tempo (sorted , vetor[:])
  cont_N = 0
  tempo_N = 0

  while tempo_N <= tSN:
    cont_N += 1
    randomico = randint(1,contador)
    tsN = tempo_sequencial(randomico , vetor[:])
    tbN = tempo_binario(randomico, vetor[:])
    tempo_N = tempo_N + (tsN-tbN)

  print (f"  %i  |  %.2f  |  %.2f  |  %.2f  |  %.2f  |  %.2f  ||  %i | %i | %i | %i  | %i" %(contador,tI,tS,tM,tQ,tSN,cont_I,cont_S,cont_M,cont_Q,cont_N))
  contador = contador + 5000
  for x in range (5000):
    vetor.append(randint(1,contador))
  VetIns = deepcopy (vetor)
  VetSel = deepcopy(vetor)
  VetMerg = deepcopy(vetor)
  VetQuick = deepcopy(vetor)
  VetNative = deepcopy(vetor)
  
  if (tI > 30 or tS > 30 ):
    break
