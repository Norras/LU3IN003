from mot_gaps import mot_gaps

def align_lettre_mot(x,y):
    for i in range(len(y)):
        #SI x MOT DE TAILLE 1, EST EGAL A y A L'INDICE i OU EST UNE PAIRE CONCORDANTE 
        if(y[i] == x) or ({x,y[i]}=={'A','T'}) or ({x,y[i]}=={'G','C'}):
            return mot_gaps(i-1)+x+mot_gaps(len(y)-i-1)
    #SI x NE VERIFIE PAS LA CONDITION PRECEDENTE ALORS ON INSERE |y| GAPS 
    return mot_gaps(len(y))+x
