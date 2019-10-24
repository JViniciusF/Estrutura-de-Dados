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

arqv2 = open('cavaleiros no.txt','r')

for line in arqv2:
    mudar2 = line.split()
    regra2.append(mudar2[1:])
    
cavaleiros= dict(zip(cavaleiro,regra2))

Adriano = []
Bruno = []
Diogo = []
Eclis = []
Gabrie = []
Leandro = []
Walber = []

jaForam= []

for x in cavaleiros:
    for moco in cavaleiros[x]:

        if x == 'Adriano':
            Adriano.append(moco)
            
        if x == 'Bruno':
            Bruno.append(moco)

        if x == 'Diogo':
            Diogo.append(moco)
                

        if x == 'Eclis':
            Eclis.append(moco)

                
        if x == 'Gabriel':
            Gabriel.append(moco)
                

        if x == 'Leandro':
            Leandro.append(moco)
                

        if x == 'Walber':
            Walber.append(moco)
                
        else :
            continue


for y in cavaleiro:
    if y not in jaForam:
        jaForam.append(y)

    for moco in cavaleiros[y]:

        if moco in jaForam: 
            continue

        else:
            i = moco
            jaForam.append(moco)
            
            if moco in Adriano and 'Adriano' in moco:
                Adriano.remove(moco)
                moco.remove('Adriano')
                
            if moco in Bruno and 'Bruno' in moco:
                Bruno.remove(moco)
                cavaleiros[moco].remove('Bruno')

            if moco in Diogo and 'Diogo' in moco:
                Diogo.remove(moco)
                cavaleiros[moco].remove('Diogo')

            if moco in Eclis and 'Eclis' in moco:
                Eclis.remove(moco)
                cavaleiros[moco].remove('Eclis')
                    
            if moco in Gabriel and 'Gabriel' in moco:
                Gabriel.remove(moco)
                cavaleiros[moco].remove('Gabriel')

            if moco in Leandro and 'Leandro' in moco:
                Leandro.remove(moco)
                cavaleiros[moco].remove('Leandro')

            if moco in Walber and 'Welber' in moco:
                Walber.remove(moco)
                cavaleiros[moco].remove('Welber')
                    
            break
    y = i
    continue
