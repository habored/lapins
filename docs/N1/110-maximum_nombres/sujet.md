---
author: BNS2022-24.1, puis Nicolas Revéret
title: Maximum
tags:
  - boucle
---

# Maximum

Écrire une fonction `maximum` :

- prenant en paramètre une liste **non vide** de nombres : `nombres`
- renvoyant le plus grand élément de cette liste.

> :warning: On interdit ici d'utiliser `max`, ainsi que `sort` ou `sorted`.

!!! example "Exemples"

    ```pycon
    >>> maximum([98, 12, 104, 23, 131, 9])
    131
    >>> maximum([-27, 24, -3, 15])
    24
    ```

{{ IDE('exo', SANS = "min,max") }}
