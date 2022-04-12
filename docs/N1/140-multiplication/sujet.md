---
author: Nicolas Revéret
title: Multiplier sans *
tags:
  - 1-boucle
---

# Multiplication sans *

Programmer la fonction `multiplication` :

* prenant en paramètres deux nombres entiers `a` et `b`,
  
* renvoyant le produit de ces deux nombres.
 
!!! example "Exemples"

    ```pycon
    >>> multiplication(3, 5)
    15
    >>> multiplication(-4, -8)
    32
    >>> multiplication(-2, 6)
    -12
    >>> multiplication(3, -4)
    -12
    >>> multiplication(-2, 0)
    0
    ```

!!! warning "Contrainte"

    Les seules opérations autorisées sont **l'addition et la soustraction** !

??? tip "Indications"

    * On rappelle que si $n$ est un nombre négatif, $-n$ est un nombre positif.

    * On a $5 \times (-3) = -5\times 3=0 +(- 5)+(- 5)+(- 5)$ !


{{ IDE('exo') }}
