arqv='''010
111
000
101
'''


arqv2='''
10101
10101
11111
'''

arqv='''0011001010
0110001010
0011001110
0000000000
0010001010
0010011111
1111100000
0010001110
0010001110
'''

matriz = []
matriz = arqv.split()
linhaLim = len(matriz)
colunaLim = len(matriz[0])
listaVet=[]



def verificar():
    linha = 0
    pivo=[]
    
    while linha <linhaLim:
        coluna = 0
        while coluna < colunaLim:
            
            if matriz [linha][coluna] == '1':
                
                    
                if (coluna-1) >= 0 and (linha-1)>= 0:
                    if matriz[linha][coluna - 1] == '1' and matriz [linha - 1][coluna] == '1':
                        pivo.append((linha,coluna))
                        pivo.append((linha,coluna-1))
                        pivo.append((linha-1,coluna))
                        listaVet.append(pivo)
                        pivo = []
                         

                    elif matriz[(linha-1)][coluna] == '1':
                        pivo.append((linha,coluna))
                        pivo.append((linha-1,coluna))
                        listaVet.append(pivo)
                        pivo = []
                    
                    elif matriz[linha][coluna-1] == '1':
                        pivo.append((linha,coluna))
                        pivo.append((linha,coluna-1))
                        listaVet.append(pivo)
                        pivo = []

                    
                    else:
                        listaVet.append([(linha,coluna)])
                
                elif (linha-1)>=0 and (coluna -1 )<0:
                    if matriz[(linha-1)][0] == '1':
                        pivo.append((linha,0))
                        pivo.append((linha-1,0))
                        listaVet.append(pivo)
                        pivo = []
                    else:
                        listaVet.append([(linha,coluna)])

                
                elif (coluna-1)>=0 and (linha -1 )<0:
                    if matriz[0][coluna-1] == '1':
                        pivo.append((0,coluna))
                        pivo.append((0,coluna-1))
                        listaVet.append(pivo)
                        pivo = []
                    else:
                        listaVet.append([(linha,coluna)])          
                else:
                    listaVet.append([(linha,coluna)])

    
            coluna = coluna + 1
        linha = linha + 1

  
def merge():

    i = 0
    limite = len(listaVet)
    while i < limite:
        y =  0
        while y < len (listaVet[i]):
            
            for z in listaVet[i+1:]:
                if listaVet[i][y] in z:
                    listaVet[i].extend(z)
                    listaVet.remove(z)
                    limite = len(listaVet)
                    break
                else: continue
            
            y = y+1
        i = i+1
    
    i = 0


    listaVet.sort()


verificar()
merge()

listaFinal = []

#Preecher matriz vazia sem os itens duplicados
t = 1
for i in range(linhaLim):  
    listaFinal.append([])
    for y in range(colunaLim):
       listaFinal[i].append((0))
    

#Imprimir com as cordenadas alteradas
for i in range (linhaLim):   
    for y in range(colunaLim):
        for a in listaVet:
            if (i,y) in a:
                listaFinal[i][y] = (listaVet.index(a)+1)

    print(listaFinal[i])
