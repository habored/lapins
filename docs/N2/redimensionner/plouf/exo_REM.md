Cet exercice demande de coder une fonction approchant la méthode `reshape` du module `numpy`.

# Commentaires

On commence par créer un nouveau tableau vide aux bonnes dimensions.

On parcourt ensuite l'ancien tableau (les lignes puis les valeurs dans chaque ligne) en calculant les coordonnées de la cellule correspondante du nouveau tableau.

Pour ce faire, à chaque nouvelle valeur, on augmente l'indice de la colonne dans laquelle insérer.

Si celui-ci est égal à la nouvelle largeur, cela signifie que l'on a fini de remplir une colonne du nouveau tableau. Dans ce cas on passe à la ligne suivante (`indice_ligne += 1)` et on recommence à la première colonne (`indice_colonne = 0`).

A la fin de la fonction, on renvoie le nouveau tableau.