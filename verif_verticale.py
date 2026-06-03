def verif_vertical(grille,joueur):
    i = 3
    while i < NB_LIGNES :
            j = 0
            while j < NB_COLONNES:
                if grille[i][j] == grille[i-1][j] == grille[i-2][j] == grille[i-3][j] == joueur :
                    return True
                j+=1
            i+=1
    return False
