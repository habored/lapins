# Commentaires

## Itération sans indice

Version recommandée

```python
def moyenne(notes_ponderees):
    cumul_points = 0.0
    cumul_coeffs = 0
    for (note, coeff) in notes_ponderees:
        cumul_points += coeff * note
        cumul_coeff += coeff
    return cumul_points / cumul_coeff
```

!!! info "parcourir un tuple"
    La construction

    ```python
    for (note, coeff) in notes_ponderees:
        ...
    ```

    est équivalente à

    ```python
    for element in notes_ponderees:
        note  = element[0]
        coeff = element[1]
        ...
    ```

    On préfèrera la première version.


## Itération avec indice

Peu d'intérêt

```python
def moyenne(notes_ponderees):
    cumul_points = 0.0
    cumul_coeffs = 0
    for i in range(len(notes_ponderees)):
        note, coeff = notes_ponderees[i]
        cumul_points += coeff * note
        cumul_coeff += coeff
    return cumul_points / cumul_coeff
```

!!! info "_unpack_ d'un tuple"
    La construction

    ```python
    note, coeff = notes_ponderees[i]
    ```

    est équivalente à

    ```python
    note  = notes_ponderees[i][0]
    coeff = notes_ponderees[i][1]
    ```

    On préfèrera la première version.


## Version fonctionnelle

Non recommandée ; deux parcours de la liste

```python
def moyenne(notes_ponderees):
    cumul_points = sum(note * coeff for (note, coeff) in notes_ponderees)
    cumul_coeffs = sum(coeff for (note, coeff) in notes_ponderees)
    return cumul_points / cumul_coeff
```
