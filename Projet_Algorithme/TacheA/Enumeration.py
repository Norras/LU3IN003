import math

def factorielle(n):
    #CAS DE BASE   
    if (n == 0):
        return 1
    else:
        res = 1
        for i in range(1,n+1):
            res = res*i
    return res

def enumAlign(x,y):
    cpt = 0
    for k in range(y): #NOMBRE DE GAPS POSSIBLE DANS X
        #NOMBRE DE COMBINAISON POSSIBLE POUR X AVEC K GAPS
        nb_x = math.floor(factorielle(x+k)/(factorielle(k)*factorielle(x))) 
        for i in range(nb_x):
            #NOMBRE DE FACON D'INSERER K GAPS DANS Y PAR RAPPORT A X
            nb_y = math.floor(factorielle(x)/(factorielle(x+k-y)*factorielle(k-y)))
            for j in range(nb_y):
                cpt += 1
    return cpt