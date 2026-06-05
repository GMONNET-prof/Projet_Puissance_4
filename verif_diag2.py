def verifie_diagonalement_bas_haut(self, joueur):
    """ Vérifie si il y a un alignement de 4 jetons de la même couleur sur la diagonale 
            (bas gauche - haut droit) de la case jouée
        Entrée : la case venant d'être jouée (tuple de int)
        Sortie : un booléen (bool) """
    for x in range(NB_PIONS_ALIGNES-1 ,NB_LIGNES):
        for z in range(NB_COLONNES-NB_PIONS_ALIGNES+1):
           gagner = True
           print((x,z))
           for i in range(NB_PIONS_ALIGNES):
               if self.grille[x-i][z+i] != joueur:
                   gagner = False
           if gagner :
                return True
    return False