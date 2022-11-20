import math
from GetTab_Dist1 import Tab_DIST_1

c_del:int=2
c_ins:int=2
c_sub:int=4
c_sub_conc:int=3

def coupure(x,y):
    tab = Tab_DIST_1(x,y)
    I = []
    i_prim = math.floor(len(x)/2)

    #INITIALISATION DE I
    for i in range(2):
        line = []
        for j in range(len(y)+1):
            line.append(0)
        I.append(line)
    
    for i in range(i_prim,len(x)+1):
        for j in range(1, len(y)+1):
            deletion = tab[i-1][j]+c_del
            insertion = tab[i][j-1]+c_ins
            substitution:int
            if(x[i-1] == y[j-1]):
                substitution = tab[i-1][j-1]
            elif (({x[i-1],y[j-1]}=={'A','T'}) or ({x[i-1],y[j-1]}=={'G','C'})):
                substitution = tab[i-1][j-1]+c_sub_conc
            else:
                substitution = tab[i-1][j-1]+c_sub

            if(i == i_prim):
                I[1][j] = j
            elif(tab[i][j] == deletion):
                I[1][j] = I[0][j]
            elif(tab[i][j] == insertion):
                I[1][j] = I[1][j-1]
            elif(tab[i][j] == substitution):
                I[1][j] = I[0][j-1]
                
            
        #AFFICHAGE DU TABLEAU I
        #print("Tableau de coupure")
        #for dist in I:
        #    print(dist)

        #REMPLACE LES VALEURS DE LA LIGNE D'INDICE 0 PAR CEUX DE LA LIGNE D'INDICE 1
        for k in range(len(y)+1):
            I[0][k] = I[1][k]
    
    return I[0][len(y)]

