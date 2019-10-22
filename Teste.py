  
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

v = list(range(10000))
from random import randint
print (busca_binaria(randint(1, 10000), v))
print (cont)