#Alunos = Arthur Barbero; Leandro Lopez - ADS 3° semestre turma A

def index(lista,valor):
    return [(lista.index(x), x.index(valor)) for x in lista if valor in x]  # Definição para retornar a localização dentro de uma lista a partir de um elemento
    

def transformar_matriz(string):
    m = []
    lista = string.split('\n')
    for a in lista:
        m.append(list(a))
    return m


entrada ='''0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110'''


matriz = transformar_matriz(entrada)


x = 0
y = 0
cont = 1

regiao = []

while x < len(matriz):  # Condição para saber o numero de linhas
    if y < len(matriz[0]):  # Condição para saber o numero de colunas
        if x >= 1 and y >= 1:  # Caso seja 1 e 1 
            if matriz[x][y] == '1':
                if matriz[x - 1][y] != '0' and matriz[x][y - 1] != '0':
                    local = index(regiao, (x-1,y))
                    for i in local:
                        for b in i:
                            emcima = b
                            break
                    local = index(regiao, (x,y-1))
                    for i in local:
                        for b in i:
                            dolado = b
                            break
                    if len(regiao[emcima]) < len(regiao[dolado]):
                        for a in regiao:
                            if (x,y-1) in a:
                                if (x-1, y) not in regiao[regiao.index(a)]:
                                    local = index(regiao,(x-1,y))
                                    for i in local:
                                        for b in i:
                                            teste = b
                                            break
    
                                    regiao[regiao.index(a)].extend(regiao[teste]) 
                                    regiao.remove(regiao[teste])
                                
                                if (x,y) not in regiao[regiao.index(a)]:
                                    a.append((x,y))
                    else:
                        for a in regiao:
                            if (x-1,y) in a:
                                if (x, y-1) not in regiao[regiao.index(a)]:
                                    local = index(regiao, (x, y-1))
                                    for i in local:
                                        for b in i:
                                            teste = b
                                            break
                                    regiao[regiao.index(a)].extend(regiao[teste]) 
                                    regiao.remove(regiao[teste])
                                if (x,y) not in regiao[regiao.index(a)]:
                                    a.append((x,y))

                elif matriz[x - 1][y] == '0' and matriz[x][y - 1] != '0':
                    for a in regiao:
                        if (x, y - 1) in a:
                            a.append((x, y))
                elif matriz[x - 1][y] != '0' and matriz[x][y - 1] == '0':
                    for a in regiao:
                        if (x - 1, y) in a:
                            a.append((x, y))
                else:
                    regiao.append([(x, y)])  

                    
        elif x == 0 and y >= 1:  # caso só a coordenada x seja 0 (0,1)
            if matriz[x][y] == '1':
                if matriz[x][y - 1] == '1':
                    for a in regiao:
                        if (x, y - 1) in a:
                            a.append((x, y))#  Adiciona a lista a esquerda
                else:
                    regiao.append([(x, y)])
        elif x >= 1 and y == 0:  # caso só a coordenada y seja 0 (1,0)
            if matriz[x][y] == '1':
                if matriz[x - 1][y] == '1':
                    for a in regiao:
                        if (x - 1, y) in a:
                            a.append((x, y))
                else:
                    regiao.append([(x, y)])
        else:  #caso seja 0 e 0
            if matriz[x][y] == '1':
                regiao.append([(x, y)])
            
                                                           
                                              
           
        y += 1
    else:
        y = 0
        x += 1
        

#  Impressão


m =[]

c = len(matriz)
l = len(matriz[0])
t = 1
for i in range(c):  #Preenchimento de matriz vazia
    m.append([])
    for y in range(l):
       m[i].append((0))
    


for i in range (c):  #Substituição das coordenadas 
    for y in range(l):
        for a in regiao:
            if (i,y) in a:
                m[i][y] = (regiao.index(a)+1)

    print(m[i])
