#--- HDR ---#
class Noeud:
    """
    Classe implémentant un nœud d'arbre disposant de 3 attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre à gauche.
    - droite : le sous-arbre à droite.
    Par défaut les nœuds gauche et droit sont initialisés à None. 
    """
    def __init__(self, valeur, gauche = None, droite = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite
#--- HDR ---#

def sélectionne(r, x):
    """ Renvoie le noeud d'étiquette x dans l'arbre de racine r. 
    Renvoie None si x n'est pas présent dans l'arbre de racine r."""
    if r is None:
        return None
    else:
        if r.valeur == x:
            return r
        else:
            à_gauche = sélectionne(r.gauche, x)
            if à_gauche is not None:
                return à_gauche
            else:
                return sélectionne(r.droit, x)

def compte_éléments(r):
    """ Détermine le nombre d'éléments de l'arbre de racine r. """
    if r is None:
        return 0
    else:
        return 1 + compte_éléments(r.gauche) + compte_éléments(r.droit)

def est_gagnable(r, n, x):
    """ Détermine s'il est possible de gagner la partie avec 
    l'arbre de racine r, de taille n, le premier joueur ayant joué x. """
    # On sélectionne le nœud choisit par le joueur 1.
    noeud = sélectionne(r, x)
    # On compte le nombre de nœuds présents dans le sous-arbre gauche
    # du nœud choisit par le joueur 1. 
    noeud_taille_gauche = compte_éléments(noeud.gauche)
    # On compte le nombre de nœuds présents dans le sous-arbre droit
    # du nœud choisit par le joueur 1. 
    noeud_taille_droit = compte_éléments(noeud.droit)
    # On compte le nombre de nœuds qui ne sont pas dans l'arbre de racine
    # noeud mais qui sont dans l'arbre de racine r. 
    noeud_taille_above = n - 1 - noeud_taille_droit - noeud_taille_gauche

    # Si jamais il y a plus de nœuds dans le sous-arbre gauche de noeud
    # que dans le reste de l'arbre, alors on peut gagner en en sélectionnant
    # la racine.
    # etc.
    return noeud_taille_above > 1 + noeud_taille_droit + noeud_taille_gauche or noeud_taille_gauche > 1 + noeud_taille_droit + noeud_taille_above or noeud_taille_droit > 1 + noeud_taille_gauche + noeud_taille_above
