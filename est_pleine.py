# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:59:41 2026

@author: celian.mludek
"""

def est_pleine(self):
    """"retourne False si la grille n'est pas pleine et True si elle est pleine
    Entrer :  
    Sortie : booleen (bool) """
    
    for ligne in self.grille:
        for une_case in ligne:
            if une_case == 0:
                return False
    return True
