---
author: Franck Chambon
title: Nombre de zéros à la fin d'un entier
tags:
  - boucle
  - maths
---
# Nombre de zéros à la fin d'un entier

On souhaite avoir une fonction `nb_zeros` qui détermine le nombre de zéros à la fin de l'écriture décimale d'un entier $n>0$, très grand.

!!! tip "Méthode"
    **On s'interdit**, ici, d'utiliser la fonction de conversion `str`. Cette méthode est totalement inefficace avec des nombres très grands.
    
    On demande plutôt de compter combien de fois on peut diviser un nombre par $10$ avec un reste égal à zéro.

    Par exemple, 

    1. $42000 = 4200×10 + 0$,
    2. $4200 = 420×10 + 0$,
    3. $420 = 42×10 + 0$,
    4. $42$ n'est pas divisible par $10.

    On a pu diviser $42000$ **trois fois** par $10$ avec un reste égal à $0$. Ce nombre se finit donc par **3** zéros.



!!! example "Exemples"

    ```pycon
    >>> nb_zeros(42000)
    3
    >>> nb_zeros(3210)
    1
    >>> nb_zeros(282475249)
    0
    >>> nb_zeros(7**10000)
    0
    >>> nb_zeros(7**10000 * 1000)
    3
    ```

    Pour information,
    
    - $7^{10} = 282475249$ finit sans aucun zéro.
    - $7^{10000}$ est un nombre très grand qui finit sans aucun zéro.

{{ IDE('exo') }}
