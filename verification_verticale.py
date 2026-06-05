def verif_vertical(self,grille, joueur):

    i = NB_PIONS_ALIGNES - 1

    while i < NB_LIGNES:

        j = 0

        while j < NB_COLONNES:

            z = 0

            while z < NB_PIONS_ALIGNES and grille[i - z][j] == joueur:
                z += 1

            if z == NB_PIONS_ALIGNES:
                return True

            j += 1

        i += 1

    return False
