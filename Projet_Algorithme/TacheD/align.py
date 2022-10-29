from operator import index
from typing import Tuple

def align_lettre_mot(x:list[str],y:list[str])->Tuple[list[str],list[str]]:
    u:list[str]=[]
    v:list[str]=[]
    index1:int=0
    index2:int=0

    #SUBSTITUTION
    if(len(x)==len(y)):
        u=x
        v=y

    #INSERTION
    if(len(x)<len(y)):
        for i in range(len(y)):
            #TANT QUE INDEX1 INDERIEUR A LA TAILLE DE X SINON ERROR INDEX1 POINTE VERS UNE MEMOIRE VIDE
            if(index1<len(x)):
                if(x[index1]!=y[i]):
                    u+='-'
                    v+=y[i]
                else:
                    u+=x[index1]
                    v+=y[i]
                    index1=index1+1
            #LA COMPARAISON ENTRE 2 LETTRES X ET Y EST FINI -> AJOUT DU RESTE DU MOT Y
            else:
                u+='-'
                v+=y[i]
        #CAS OU LES MOTS SONT DIFFERENTS ET RESTE DE X NON AJOUTER DANS L'ALIGNEMENT
        if(index1<len(x)):
            for i in range(index1,len(x)):
                u+=x[i]
                v+='-'
    
    #DELETION
    if(len(x)>len(y)):
        for i in range(len(x)):
            if(index2<len(y)):
                if(x[i]!=y[index2]):
                    u+=x[i]
                    v+='-'
                else:
                    u+=x[i]
                    v+=y[index2]
                    index2=index2+1
            else:
                u+=x[i]
                v+='-'

        if(index2<len(y)):
            for i in range(index2,len(y)):
                u+='-'
                v+=y[i]

    return (u,v)

