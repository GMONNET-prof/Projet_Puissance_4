# Les variables globales
NB_LIGNES = 6
NB_COLONNES = 7
NB_PIONS_ALIGNES = 4


# la classe
class Grille :
    """simule un jeu de puissance 4 avec une grille  de 6 lignes et 7 colonnes"""
    def __init__(self, grille = []) :
        """ Constructeur de la classe Grille
            un attribut : grille (tableau de 6 lignes et 7 colonnes)
            Entrée : aucune
            Sortie : aucune"""
        if grille != [] :
            self.grille = grille
        else :
            self.grille = []
            for i in range(NB_LIGNES) :
                ligne = []
                for j in range(NB_COLONNES) :
                    ligne.append(0)
                self.grille.append(ligne)

    def jouer(self, colonne, joueur) :
        """ Place le pion dans la colonne si le coup est possible
            Entrée : rang de la colonne (int), numéro du joueur (int)
            Sortie : booléen (bool)"""
        ligne = NB_LIGNES - 1 # dernière ligne de la grille
        while ligne != -1 and self.grille[ligne][colonne] != 0 :
            ligne = ligne - 1
        if ligne != -1 :
            self.grille[ligne][colonne] = joueur
            return True
        else :
            return False

    def __repr__(self):
        """ Retourne une chaine pour afficher la grille en console
            Entrée : aucune
            Sortie : chaine de caractères (str)"""
        chaine_finale = "|"
        for ligne in self.grille :
            for case in ligne :
                chaine_finale += str(case) + "|"
            chaine_finale += "\n" + "|"
        return chaine_finale[:-1]

    def score(self):
        """ Retourne le score actuel de la grille pour le joueur 2
            Entrée : aucune
            Sortie : score de la grille (int)"""
        score_J2 = 0
        for i in range(NB_LIGNES) :
            for j in range(NB_COLONNES) :
                score_J2 += valeur_case(i,j)

        return score_J2
    
    
    def est_pleine(self):
        """"retourne False si la grille n'est pas pleine et True si elle est pleine
        Entrer :  
        Sortie : booleen (bool) """
        
        for ligne in self.grille:
            for une_case in ligne:
                if une_case == 0:
                    return False
        return True
    
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
    
    
    def verif_diagonal1(self,joueur): # ici la fonction à récupérer
        """Vérifie les diagonales de haut-gauche vers bas-droite"""
        for x in range(NB_LIGNES):
            for y in range(NB_COLONNES):
                nb_jeton = 0
                # Vérifie la diagonale en partant de (x, y)
                i, j = x, y
                while i < NB_LIGNES and j < NB_COLONNES and self.grille[i][j] == joueur:
                    nb_jeton += 1
                    if nb_jeton == NB_PIONS_ALIGNES:
                        return True
                    i += 1
                    j += 1
        return False
    
    
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
    
    def horizonal_verification(self, player):
        for row in self.grid:
            for i, val in enumerate(row):
                hasWon = True
                if val == player and i <= len(row)-NB_PIONS_ALIGNES:
                    #print(f"la valeur parcourue est {val} ({row})")
                    for span in range(NB_PIONS_ALIGNES  ):
                        #print(f"l'écart calculé est {span}, ce qui equivaut à {row[i+span]}")
                        if row[i+span] != player:
                            hasWon = False
                    print(hasWon)
                    if hasWon: return hasWon
                hasWon = False
        return hasWon
    
    
    def a_gagner(self, joueur):
        if self.verif_vertical(joueur):
            return True
        if self.verif_horizontal(joueur):
            return True
        if self.verif_diagonal1(joueur):
            return True
        if self.verif_diagonal2(joueur):
            return True
        return False
        

    
  
# les tests
la_grille1 = Grille()
print(la_grille1)

# lancement de la partie
la_grille1.jouer(2,1)
la_grille1.jouer(3,2)
la_grille1.jouer(4,2)
la_grille1.jouer(5,2)
la_grille1.jouer(6,2)
print(la_grille1)
print(la_grille1.est_pleine())



grille_pleine = [[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]
la_grille2 = Grille(grille_pleine)
print(la_grille2.est_pleine())
print(la_grille2)  
















