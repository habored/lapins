author: Romain JANVIER
title: Dentiste

---

# Élocution chez le dentiste

Chez le dentiste, la bouche grande ouverte, lorsqu'on essaie de parler, il
ne reste que les voyelles. Même les ponctuations sont supprimées. 
Vous devez écrire une fonction `dentiste(texte)` qui renvoie un texte 
ne contenant que les voyelles de `texte`, dans l'ordre. 

Les voyelles sont données par :
```python
voyelles = ['a', 'e', 'i', 'o', 'u', 'y']
```
On ne considèrera que des textes écrits en minuscules, sans accents.

!!! example "Exemples"

    ```pycon
    >>> dentiste("j'ai mal")
    'aia'
    >>> dentiste("il fait chaud")
    'iaiau'
    >>> dentiste("")
    ''
    ```

{{ IDE('exo') }}