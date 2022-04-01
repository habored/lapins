---
author: Florian Picard
title: Jeu Arbre
tags:
  - arbre
statut: proposition
---


# Jeu de coloriage d'arbre.



## Description du problème

Deux joueurs jouent à tour de rôle sur un arbre binaire. On donne la
racine `r` de cet arbre binaire, ainsi que le nombre de nœuds `n` de l'arbre.
`n` est un nombre impair, et chacun nœud de l'arbre est étiqueté par un nombre
compris entre $1$ et $n$ (toutes les étiquettes sont distinctes).

Initialement, le premier joueur choisit une valeur $x$ avec $1 \leq x \leq n$
puis colorie le nœud d'étiquette $x$ en rouge. Puis le second joueur choisit
une valeur $y$ avec $1 \leq y \leq n$, $y \neq x$, et colorie le nœud $y$ en bleu.   

Ensuite, chaque joueur joue à tour de rôle. À son tour, le joueur choisit
un nœud de sa couleur (rouge pour le joueur 1, et bleu pour le joueur 2), et
colorie un des voisins non coloriés de ce nœud (l'enfant droit, gauche, ou le
parent du nœud).

Lorsqu'un joueur ne peut plus choisir de nœud de cette façon, alors il doit
passer son tour. Si les deux joueurs passent leur tour, alors la partie est
terminée et le joueur avec le plus de nœuds coloriés avec sa couleur gagne la partie.

Vous jouez en second. On souhaite écrire une fonction `est_gagnable` qui
détermine, étant donné la racine `r` d'un arbre binaire $\mathcal{A}$  correspondant à la
description de l'énoncé, un nombre `n` (la taille de $\mathcal{A}$) et un nombre
$x$ avec $1 <= x <= n$, s'il vous est possible de trouver une valeur $y$ avec
$1 <= y <= n$ et $y \neq x$ qui vous assure la victoire. 

La classe `Noeud` dont on donne le code ci-dessous permet de représenter les nœuds d'un
arbre binaire. On représente l'arbre vide avec la valeur spéciale `None`. 

```python
class Noeud:
    """
    Classe implémentant un nœud d'arbre disposant de 3 attributs :
    - valeur : la valeur de l'étiquette,
    - gauche : le sous-arbre à gauche.
    - droite : le sous-arbre à droite.
    Par défaut les nœuds gauche et droit sont initialisés à None. 
    """
    def __init__(self, valeur, gauche = None, droite = None):
        self.valeur = valeur
        self.gauche = gauche
        self.droite = droite
```



## Exemples



### Exemple 1

        _____1_  
       /       \ 
      _2__     3 
     /    \   / \
     4    5_  6 7
    / \  /  \    
    8 9 10 11    

Dans cet exemple, le premier joueur a sélectionné le nœud d'étiquette $x = 3$.
Le second joueur peut sélectionner le nœud d'étiquette $y = 2$. Avec ce choix de
nœud, il est certain de gagner la partie. 
Il faut donc répondre `True`.


### Exemple 2

     1 
    / \
    2 3

Dans cet exemple, le premier joueur a séléctinné le nœud d'étiquette $x = 1$. Quelque
soit son choix, le second joueur ne pourra colorier qu'un seul nœud avec sa couleur,
alors que le premier joueur pourra en colorier deux.
Il faut donc répondre `False`. 


### Exemple 3

         _______1
        /        
      __2_____   
     /        \  
     3_     __4  
    /  \   /   \ 
    5  6   7_  8 
      /   /  \   
      9  10 11   

Dans cet exemple le premier joueur sélectionne le nœud d'étiquette $x = 4$.
Le second joueur sélectionne alors le nœud d'étiquette $y = 2$.
En alternant les coups, le joueur 1 ne pourra que colorier les nœuds d'étiquette
$7$, $8$, $10$, et $11$, soit au total 5 nœuds. Le second joueur pourra colorier
les autres nœuds de l'arbre, soit au total 6 nœuds. Il est donc possible pour
le second joueur de gagner.
Il faut donc répondre `True`. 


## Résolution du problème

La stratégie optimale à ce jeu est d'empêcher le plus rapidement
possible l'autre joueur de pouvoir "s'étendre". On note `r` le nœud
choisit par le premier joueur.

- si le sous-arbre gauche du nœud `r` possède plus de nœuds que dans le reste de l'arbre, alors en choisissant la racine du sous-arbre gauche de `r` on gagne la partie.
- si le sous-arbre droit du nœud `r` possède plus de nœuds que dans le reste de l'arbre, alors en choisissant la racine du sous-arbre droit de `r` on gagne la partie.
- si le sous-arbre de racine `r` possède moins de nœuds que le reste de l'arbre, alors en choisissant le nœud parent de `r` on gagne la partie.

Écrire les trois fonctions ci-dessous qui permettent de résoudre le problème. 

- La fonction `sélectionne`, qui étant donné la racine `r` d'un arbre binaire $\mathcal{A}$ et une étiquette `x`, renvoie l'objet de type `Noeud` dont l'étiquette est `x`, si l'étiquette `x` est présente dans $\mathcal{A}$ ; et renvoie `None` sinon.
- Une fonction `compte_éléments`, qui étant donné un objet `r` de type `Noeud` ou `None`, détermine le nombre d'éléments présents dans l'arbre correspondant à `r`.
- Une fonction `est_gagnable` qui détermine, étant donné la racine `r`d'un arbre binaire $\mathcal{A}$ correspondant à la description de l'énoncé, un nombre `n` (la taille de $\mathcal{A}$) et un nombre $x$ avec $1 <= x <= n$, s'il vous est possible de trouver une valeur $y$ avec $1 <= y <= n$ et $y \neq x$ qui vous assure la victoire.

{{IDE('exo')}}