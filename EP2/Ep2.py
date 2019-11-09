print ('\tEp 2 \n Jose Vinicius Ferreira Santana 3 ADS B\n')
arqv = open('casamento.txt','r')

regra = []
regra2 = []

damas = ['Jessica','Fernanda','Pamela','Renata'] 
cavaleiro = ['Adriano','Bruno','Diogo','Eclis','Gabriel','Leandro','Walber']

Adriano1 = []
Bruno1 = []
Diogo1 = []
Eclis1 = []
Gabriel = []
Leandro1 = []
Walber1 = []

for line in arqv:
    mudar = line.split()
    regra.append(mudar[1:])
    
pretendente = dict(zip(damas,regra))

i = 0
y = 0
for x in pretendente:
    for moco in pretendente[(damas[i])]:

        if moco == 'Adriano':

            if len (Adriano1)== 0:
                Adriano1.append(damas[i])
                damas.pop(i)
                break
            else:
                continue

        if moco == 'Bruno':

            if len (Bruno1)== 0:
                Bruno1.append(damas[i])
                damas.pop(i)
                break
            else:
                continue

        if moco == 'Diogo':

            if len (Diogo1)== 0:
                Diogo1.append(damas[i])
                damas.pop(i)
                break
            else:
                continue

        if moco == 'Eclis':

            if len (Eclis1)== 0:
                Eclis1.append(damas[i])
                damas.pop(i)
                break
            else:
                continue

        if moco == 'Gabriel':

            if len (Gabriel1)== 0:
                Gabriel1.append(damas[i])
                damas.pop(i)
                break
            else:
                continue

        if moco == 'Leandro':

            if len (Leandro1)== 0:
                Leandro1.append(damas[i])
                damas.pop(i)
                break
            else:
                continue

        if moco == 'Walber':

            if len (Walber1)== 0:
                Walber1.append(damas[i])
                damas.pop(i)
                break
            else:
                continue


if len (damas) == 0:
    print("Casamento possivel")
else:
    print ("Casamento nao e possivel")
    for x in damas:
        print (x)
    print ("Nao tem preferencias sulficiente")


'''Segunda Parte do EP2'''

arqv2 = open('cavaleiros.txt','r')

for line in arqv2:
    mudar2 = line.split()
    regra2.append(mudar2[1:])
    
cavaleiros= dict(zip(cavaleiro,regra2))

lista = []
for t in cavaleiros:
    if t not in lista:
        lista.append(t)
    for u in cavaleiros[t]:
        if u not in lista:
            lista.append(u)
            for u in cavaleiros[u]:
                if u not in lista:
                    lista.append(u)
                    for u in cavaleiros[u]:
                        if u not in lista:
                            lista.append(u)
                            for u in cavaleiros[u]:
                                if u not in lista:
                                    lista.append(u)
                                    for u in cavaleiros[u]:
                                        if u not in lista:
                                            lista.append(u)
                                            for u in cavaleiros[u]:
                                                if u not in lista:
                                                    lista.append(u)
                                                    for u in cavaleiros[u]:
                                                        if u in t:
                                                            print(f"Será possível sentar os cavaleiros da seguinte forma:\n{lista}")
                                                            break
                                                        else:
                                                            print("Não é possivel arrumar os cavaleiros nos lugares com suas preferencias")
                                                            break
