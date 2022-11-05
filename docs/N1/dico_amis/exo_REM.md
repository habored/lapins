# Commentaires

{{ IDE('exo_corr') }}

Une version un petit peu plus efficace mais qui utilise des tranches :

```python
def amis_d_amis(reseau, membre):
    resultat = [membre]
    for ami in reseau[membre]:
        for ami_de_ami in reseau[ami]:
            if amis_amis not in res:
                resultat.append(ami_de_ami)
    return resultat[1:]
```
