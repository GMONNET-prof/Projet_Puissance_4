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
    
    
    
    def verif_diagonal1(self,joueur):
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
        
        
        
        
# les tests
la_grille1 = Grille()
print(la_grille1)

# lancement de la partie
la_grille1.jouer(5,1)
la_grille1.jouer(4,2)
la_grille1.jouer(4,1)
la_grille1.jouer(2,2)
la_grille1.jouer(3,2)
la_grille1.jouer(3,2)
la_grille1.jouer(3,1)
la_grille1.jouer(2,2)
la_grille1.jouer(2,2)
print(la_grille1)
print(la_grille1.verif_diagonal1(1)) 

la_grille1.jouer(2,1)
print(la_grille1)
print(la_grille1.verif_diagonal1(1)) 

