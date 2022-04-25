---
author: Nicolas Revéret
title: Tête de série
tags:
    - dictionnaire
---

# Tête de série

L'organisateur d'un tournoi sportif souhaite déterminer le nom du joueur participant le mieux classé dans le classement international.

Les classements des joueurs sont des entiers tous distincts et compris entre `1` et `len(classement)`.

Il connaît donc le nom des participants au tournoi, donné sous forme d'une liste, ainsi que le classement, donné sous forme d'un dictionnaire.

Par exemple :

```python
participants = ['Stefanos', 'Rafael', 'David', 'Novak']
classement = {'Novak': 1, 'Daniil': 2, 'Alexander': 3, 'Stefanos': 4, 'Rafael': 5}
```

Comme on peut le voir dans l'exemple :

* tous les joueurs classés ne sont pas obligatoirement inscrits au tournoi (ici `Daniil` et `Alexander` ne participent pas)
* certains participants au tournoi, invités d'honneur, n'ont pas de classement (`David` ici)... On considérera donc qu'ils sont moins bien classés que n'importe lequel des joueurs classés

Vous devez écrire une fonction `tete_de_serie(participants, classement)` prenant en arguments la liste des joueurs inscrits au tournoi ainsi que le classement et renvoyant le prénom du joueur le mieux classé.

Il y a plusieurs solutions, par exemple :

* **Proposition 1 :** donner un classement arbitraire aux participants non-classés et les comparer avec les joueurs classés

* **Proposition 2 :** filtrer la liste des participants afin de ne conserver que les joueurs classés :
    * si cette liste est vide, le tournoi ne compte que des participants non-classés. La tête de série est donc le premier joueur
    * sinon, il est inutile de considérer les non-classés, la tête de série sera obligatoirement un joueur classé

!!! warning "Attention"

    Le dictionnaire `classement` ne devra pas être modifié lors de l'exécution de la fonction

Si le tournoi ne comporte que des joueurs non-classés, la fonction renverra le prénom du premier joueur de la liste.

!!! example "Exemples"

    ```pycon
    >>> classement = {'Novak': 1, 'Daniil': 2, 'Alexander': 3, 'Stefanos': 4, 'Rafael': 5}
    >>> participants = ['Stefanos', 'Novak', 'Rafael']
    >>> tete_de_serie(participants, classement)
    'Novak'
    >>> participants = ['Stefanos', 'Rafael', 'David', 'Novak']
    >>> tete_de_serie(participants, classement)
    'Novak'
    >>> participants = ['David', 'Novak', 'Alexander', 'Daniil']
    >>> tete_de_serie(participants, classement)
    'Novak'
    >>> participants = ['David', 'Olivier']
    >>> tete_de_serie(participants, classement)
    'David'
    ```

{{ IDE('exo') }}
