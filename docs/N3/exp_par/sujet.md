---
author: Franck Chambon
title: Bien parenthésée 2
tags:
  - 3-dictionnaire
  - 7-pile
---
# Expression bien parenthésée (2)

On considère dans cet exercice un parenthésage avec les couples `()`, `{}`, `[]` et `<>`. On dira qu'une expression est bien parenthésée si chaque symbole ouvrant correspond à un symbole fermant et si l'expression contenue à l'intérieur est elle-même bien parenthésée.

!!! success "Bien parenthésées"
    - `(2 + 4)*7`
    - `tableau[f(i) - g(i)]`
    - `#include <stdio.h> int main(){int liste[2] = {4, 2}; return (10*liste[0] + liste[1]);}`

!!! bug "Mauvais parenthésage"
    ![XKCD 859](par.png)

    - `(une parenthèse laissée ouverte` ; pas de fermante associée à `(`.
    - `{<(}>)` ; mauvaise imbrication.
    - `c'est trop tard ;-)` ; pas d'ouvrante associée à `)`.

Écrire une fonction `est_bien_parenthesee` qui détermine si une `expression` passée en paramètre est bien parenthésée avec les couples `()`, `{}`, `[]` et `<>`. La fonction renvoie un booléen. L'`expression` sera une chaine de caractères de longueur au plus 1000.

!!! example "Exemples"

    ```pycon
    >>> est_bien_parenthesee("(2 + 4)*7")
    True
    >>> est_bien_parenthesee("tableau[f(i) - g(i)]")
    True
    >>> est_bien_parenthesee("#include <stdio.h> int main(){int liste[2] = {4, 2}; return (10*liste[0] + liste[1]);}")
    True
    ```

    ```pycon
    >>> est_bien_parenthesee("(une parenthèse laissée ouverte crée une tension intense qui dure toute la journée.")
    False
    >>> est_bien_parenthesee("{<(}>)")
    False
    >>> est_bien_parenthesee("c'est trop tard ;-)")
    False
    ```

On pourra compléter le code donné qui utilise un dictionnaire `ouverture` qui renvoie l'élément ouvrant associé à la clé fermante.

```pycon
>>> ouverture['}']
'{'
>>> ouverture['>']
'<'
```

{{ IDE('exo', MAX=1000) }}