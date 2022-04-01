# Commentaires

Il s'agit d'une recherche de maximum classique. La liste étant non-vide, on initialise la variable `maxi` avec la première valeur.

{{ py('exo_corr', 0, '# TESTS') }}

## Variante récursive

```python
def maximum(nombres):
    if len(nombres) == 1:
        return nombres[0]
    dernier = nombres.pop()
    maxi = maximum(nombres)
    nombres.append(dernier)
    if dernier > maxi:
        return dernier
    else:
        return maxi
```

On prend soin, ici, de reconstruire la liste après l'appel récursif.
