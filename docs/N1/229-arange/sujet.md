---
author: Franck Chambon
title: arange
tags:
  - 1-boucle
  - 2-float
---
# Nombres espacés (2)

Pour construire la représentation graphique d'une fonction définie sur un intervalle de type $[a ; b[$ ($a$ est inclus, $b$ est exclu), on calcule les images de plusieurs antécédents régulièrement espacés, ce qui permet de placer des points à relier. Encore faut-il disposer des antécédents. Comment les choisir ?

!!! example "Exemples"
    - Pour une fonction définie sur $[2.0, 4.0[$, avec des points régulièrement espacés par pas de $0.5$, on prend $2.0, 2.5, 3.0, 3.5$.
    - Pour une fonction définie sur $[5.0, 6.5[$, avec des points régulièrement espacés par pas de $0.25$, on prend $5.0, 5.25, 5.5, 5.75, 6.0, 6.25$.

En paramètre, on utilisera `a`, `b` et `pas` : des flottants ; `pas` est strictement positif.

Pour cet exercice, on souhaite **surtout** qu'aucun nombre de la liste ne soit trop proche de $b$. On veillera donc à ce que tout nombre soit inférieur à $b - \varepsilon$ où $\varepsilon$ sera la constante `EPS = 10**(-6)`

Écrire une fonction telle que `arange(a, b, pas)` renvoie une liste de flottants qui vérifie :

- les nombres sont tous strictement inférieurs à `b - EPS` ;
- le premier, s'il existe, est `a` ;
- les nombres sont rangés dans l'ordre croissant ;
- l'écart entre deux nombres consécutifs est `pas`.

!!! warning "Erreur relative"
    On rappelle qu'on ne fait pas de tests d'égalité entre flottants.
    
    La validation de **cet exercice** autorise des nombres avec une erreur relative de $10^{-6}$. **En contrepartie**, aucun nombre supérieur à `b - EPS` ne sera accepté dans la réponse.
    
    Concrètement, si vous deviez faire le test $x < b$ alors vous devrez écrire `#!py x < b - EPS`.

!!! example "Exemples"

    ```pycon
    >>> arange(2.0, 4.0, 0.5)
    [2.0, 2.5, 3.0, 3.5]
    >>> arange(5.0, 6.5, 0.25)
    [5.0, 5.25, 5.5, 5.75, 6.0, 6.25]
    >>> arange(2.0, 2.0, 0.1)
    []
    ```

{{ IDE('exo') }}

!!! info "`arange` et `numpy`"
    La fonction `arange` n'a aucun rapport avec le mot français « arrange ».

    La fonction `arange` existe dans le module `numpy` ; c'est un vague équivalent de `range` avec des flottants. Il est souhaitable de se passer d'un tel gros module quand c'est possible. Cet exercice montre comment construire la fonction `arange` qui est utile pour des représentations graphiques.
