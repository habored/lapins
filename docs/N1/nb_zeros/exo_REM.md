# Commentaires

## Version simple

{{ IDE('exo_corr') }}

On fait attention ; la fonction bouclerait à l'infini pour $n=0$ ; elle n'est pas clairement définie.

Étudions des variantes.

## Version avec `divmod`

`divmod` renvoie le quotient et le reste dans une division entière. Par exemple `divmod(1789, 100)` renvoie `(17, 89)`. En effet, $1789$ divisé par $100$ donne un quotient de $17$ et un reste de $89$. On peut vérifier que $1789 = 17×100 + 89$.

```python
def nb_zeros(n):
    assert n > 0

    resultat = -1
    reste = -1
    while reste != 0:
        n, reste = divmod(n, 10)
        resultat += 1
    return resultat
```

Ici, on initialise `reste` et `resultat` à $-1$ ; on est sûr de faire au moins un tour de boucle, et il y en aura un de plus que le nombre cherché.

On ne fait qu'une seule division par tour de boucle.

Dans la version précédente, il y a avait une division **et** un modulo par tour de boucle.

**Soyons honnête** : cette version apporte très peu en efficacité, mais rend le code plus complexe. La première version est largement recommandée.
