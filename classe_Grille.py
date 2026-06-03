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
        if 0 <= colonne <= NB_COLONNES - 1 : # sécurité sur la colonne
            return False
        if 0 < joueur < 3 : # sécurité sur le numéro du joueur
            return False
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

    def valeur_case(ligne, colonne) :
        """ Retourne le nombre d'alignements de quatre cases contenant la case en entrée
        Entrée : coordonnées d'une case de la grille (int, int)
        Sortie : nombre d'alignements (int)"""
    score = 0
    # ici les appels aux fonctions qui calculent le nombre d'alignements (verticalement, horizontalement, diagonalement 1 et 2)
    return score

    def score(self):
        """ Retourne le score actuel de la grille pour le joueur 2
            Entrée : aucune
            Sortie : score de la grille (int)"""
        score_J2 = 0
        for i in range(NB_LIGNES) :
            for j in range(NB_COLONNES) :
                score_J2 += valeur_case(i,j)
        return score_J2
    
    
