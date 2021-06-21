# Guide du REPL

## Aperçu

Un REPL se présente sous cette forme :

??? info "Déroulez-moi !"

    {{REPL('exo2')}}

Il dispose de quatre boutons : 

- Lancer le script : <button class="emoji">▶️</button> 
- Télécharger le script : <button class="emoji">⤵️</button>
- Téléverser un script : <button class="emoji">⤴️</button>
- Valider le script avec des tests unitaires : <button class="emoji_dark">🛂</button>

!!! info "Rappel"

    Tout se fait du côté client. **Rien n'est envoyé au serveur**.

## Prise en main

Par défaut, la commande `#!markdown {% raw %}{{REPL('exo2')}}{% endraw %}` permet de charger un script placé dans `docs/scripts/`. 

Pour une organisation en chapitre, utilisez un chemin relatif. Par exemple : `#!markdown {% raw %}{{REPL('c1/exo2')}}{% endraw %}` chargera le script exo2.py depuis `docs/scripts/c1`.

!!! warning "Important"

    Le bouton de validation du script à l'aide de tests unitaires est présent uniquement si vous fournissez un fichier `test_nom_du_fichier.py` présent dans le même répertoire que `nom_du_fichier.py`.

    Le lancement du script, le téléchargement et le téléversement sont présentes par défaut.

    Pour l'instant, aucun fichier de correction n'est fourni.

## Plein d'exercices !

!!! info "Exercices sur la longueur d'un tableau"

    === "Exercice 1"
        Complétez la fonction `longueur` afin que celle-ci renvoie la taille d'un tableau L.
        
        {{REPL('demo/demo1')}}
        
    === "Exercice 2"
        Complétez la fonction `longueur_ajout` afin que celle-ci renvoie la taille de deux tableaux T1 et T2.
        {{REPL('demo/demo2')}}

    === "Exercice 3"
        On découpe une phrase à l'aide de l'instruction [split](https://docs.python.org/fr/3/library/stdtypes.html#str.split "Instruction split en Python").

        Complétez la fonction `nombre_mots` afin que celle-ci renvoie le nombre de mots séparé par un espace d'une phrase `phrase`.
        {{REPLv('demo/demo3')}}


On peut bien sur enrouler tout cela...

??? info "Exercices sur la longueur d'un tableau"

    === "Exercice 1"
        Complétez la fonction `longueur` afin que celle-ci renvoie la taille d'un tableau L.
        
        {{REPL('demo/demo1')}}
        
    === "Exercice 2"
        Complétez la fonction `longueur_ajout` afin que celle-ci renvoie la taille de deux tableaux T1 et T2.
        {{REPL('demo/demo2')}}

    === "Exercice 3"
        On découpe une phrase à l'aide de l'instruction [split](https://docs.python.org/fr/3/library/stdtypes.html#str.split "Instruction split en Python").

        Complétez la fonction `nombre_mots` afin que celle-ci renvoie le nombre de mots séparé par un espace d'une phrase `phrase`.
        {{REPLv('demo/demo3')}}


<!-- ??? info "Patience, patience"

    Le guide du REPL arrive bientôt.
 -->
