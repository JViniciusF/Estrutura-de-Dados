arqv = open('casamento.txt','r')

regra = []

damas = ['Jessica','Fernanda','Pamela','Renata'] 

Adriano = []
Bruno = []
Diogo = []
Eclis = []
Gabriel = []
Leandro = []
Walber = []

for line in arqv:
    mudar = line.split()
    regra.append(mudar[1:])
    
pretendente = dict(zip(damas,regra))

i = 0
y = 0
for x in pretendente:
    for moco in pretendente[(damas[i])]:

        if moco == 'Adriano':

            if len (Adriano)== 0:
                Adriano.append(damas[i])
                break
            else:
                continue

        if moco == 'Bruno':

            if len (Bruno)== 0:
                Bruno.append(damas[i])
                break
            else:
                continue

        if moco == 'Diogo':

            if len (Diogo)== 0:
                Diogo.append(damas[i])
                break
            else:
                continue

        if moco == 'Eclis':

            if len (Eclis)== 0:
                Eclis.append(damas[i])
                break
            else:
                continue

        if moco == 'Gabriel':

            if len (Gabriel)== 0:
                Gabriel.append(damas[i])
                break
            else:
                continue

        if moco == 'Leandro':

            if len (Leandro)== 0:
                Leandro.append(damas[i])
                break
            else:
                continue

        if moco == 'Walber':

            if len (Walber)== 0:
                Walber.append(damas[i])
                break
            else:
                continue


    i= i+1
        
