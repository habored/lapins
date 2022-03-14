Il s'agit d'un exemple de programmation dynamique :

* on découpe le problème en plusieurs problèmes de plus petites tailles
* les différents sous-problèmes se recoupent : on garde trace des résultats intermédiaires afin d'éviter les calculs identiques

On choisit ici de traiter le problème à l'aide d'une approche récursive.

# Commentaires

La fonction `sans_dernier` ne présente pas de difficultés. On parcourt le `texte` en ajoutant au fur et à mesure les caractères dans `résultats`. On prend soin de s'arrêter avant le dernier caractères (`range(len(texte)-1)`).

On aurait aussi pu utiliser une tranche et le fait que, en Python, le dernier élément d'une chaîne a aussi `-1` comme indice :

```python
def sans_dernier(texte) :
    return texte[:-1]
```

La fonction `plus_longue_sous_chaine` est plus compliquée.

Comme il s'agit d'une fonction récursive, il est bon de débuter par un cas de base, ici le cas ou l'un des deux textes est vide. On renvoie directement la chaîne vide.

On vérifie ensuite que le cas a été traité ou non. Pour cela on se demande si le couple `(texte1, texte2)` est une clé du dictionnaire `memoire`. Si oui on renvoie directement la valeur associée.

Dans le cas contraire, on doit faire la comparaison :

* si les derniers caractères sont identiques, on compare les chaînes raccourcies et l'on ajoute ce dernier caractère au résultat. Cette valeur est immédiatement stockée dans le dictionnaire `memoire`
* si les caractères diffèrent, on étudie les deux cas précisés par l'énoncé. On place dans le dictionnaire le résultat le plus long

En dernier lieu on renvoie la valeur que l'on vient d'insérer dans le dictionnaire.