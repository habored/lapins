def redimensionner(tableau, nouvelle_largeur, nouvelle_hauteur):
    nouveau_tab = [[0]*nouvelle_largeur for _ in range(nouvelle_hauteur)]

    indice_ligne, indice_colonne = 0, -1
    for ligne in tableau:
        for valeur in ligne:
            indice_colonne += 1
            if indice_colonne == nouvelle_largeur:
                indice_ligne += 1
                indice_colonne = 0
            nouveau_tab[indice_ligne][indice_colonne] = valeur
    return nouveau_tab


# Tests
tab1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
tab2 = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
tab3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
assert redimensionner(tab1, 6, 2) == tab2
assert redimensionner(tab1, 3, 4) == tab3
