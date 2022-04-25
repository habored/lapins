# Commentaires

Le problème revient à sélectionner le minimum dans une liste. Deux subtilités toutefois :

* la liste contient les "étiquettes" des données à comparer (les prénoms des joueurs alors que l'on compare les classements)
* certains joueurs n'ont pas de classement : on utilise alors une valeur par défaut supérieure au plus grand classement possible

## Une solution possible

{{ IDE('exo_corr') }}

On vérifie tout d'abord que la liste comporte au moins un joueur.

On initialise ensuite la recherche en considérant que le premier joueur participant a le meilleur classement. Si ce joueur n'est pas classé, on lui donne la note de `len(classement)+1`.

La suite de la fonction est construite autour d'une boucle *Pour chaque*. On parcourt l'ensemble des participants et pour chacun on se demande :

* est-il classé ? Si non, il ne peut pas être mieux classé que le "meilleur" actuel
* s'il est classé, est-il mieux classé que le "meilleur" actuel ? Si oui, on met à jour les valeurs

La fonction se termine en renvoyant le prénom du joueur le mieux classé.

## Autre solution

Si l'on commence par trier les participants entre joueurs classés et non classés, on peut faire :

```python
def tete_de_serie(participants, classement):
    participants_classes = [joueur for joueur in participants if joueur in classement]
    if participants_classes == []:
        meilleur_joueur = participants[0]
    else:
        meilleur_joueur = participants_classes[0]
        for joueur in participants_classes:
            if classement[meilleur_joueur] > classement[joueur]:
                meilleur_joueur = joueur
    return meilleur_joueur
```