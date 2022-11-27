## Commentaires

{{ IDE('exo_corr') }}

- `#!py b = a / 2`, la variable `b` est à la fois
    - le décalage pour rejoindre un sommet du carré
    - le côté des prochains carrés à construire
- `#!py for dx, dy in [(-b, -b), (b, -b), (-b, b), (b, b)]:`
    - prépare la construction des 4 motifs de niveau `n - 1` dans les 4 coins du carré.