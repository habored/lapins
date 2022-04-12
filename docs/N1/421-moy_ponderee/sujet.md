---
author: Franck Chambon
title: Moyenne pondérée
tags:
  - 1-boucle
  - 2-tuple
  - 4-maths
---

# Moyenne de notes avec coefficients

Les résultats aux évaluations d'un élève sont regroupés dans une liste non vide composée de couples `(note, coefficient)`. Dans ce couple :

- `note` est un nombre de type flottant (`float`) compris entre `0.0` et `20.0`
- `coefficient` est un nombre de type entier (`int`) strictement positif


Écrire une fonction `moyenne` qui renvoie la moyenne pondérée de cette liste donnée en paramètre.

!!! example "Exemple"
    Le calcul suivant illustre l'exemple :

    $$\frac{2×15,\!0 + 1×9,\!0 + 3×12,\!0}{2+1+3} = 12,\!5$$

    ```pycon
    >>> moyenne([(15.0, 2), (9.0, 1), (12.0, 3)])
    12.5
    ```

{{ IDE('exo', SANS='max,min,math') }}
