---
author: Nicolas Revéret
title: Maximum
tags:
  - 1-boucle
---

# Maximum

Écrire une fonction `maximum` :

- prenant en paramètre une liste **non vide** de nombres : `nombres`
- renvoyant le plus grand élément de cette liste.

Chacun des nombres utilisés est de type `int` ou `float`.

> :warning: On interdit ici d'utiliser `max`, ainsi que `sort` ou `sorted`.

!!! example "Exemples"

    ```pycon
    >>> maximum([98, 12, 104, 23, 131, 9])
    131
    >>> maximum([-27, 24, -3, 15])
    24
    ```

{{ IDE('exo', SANS = "max, sorted, sort") }}
