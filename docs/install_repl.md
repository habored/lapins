# Guide du REPL

!!! info "paf"

    === "test"
        {{REPL('exo2')}}
    
    === "Corrigé"
        {{REPL('exo2')}}


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

!!! info "Exercice 1"

    Écrire une fonction qui découpe une phrase en mots.

    {{REPL('exo_demo_1')}}


<!-- ??? info "Patience, patience"

    Le guide du REPL arrive bientôt.
 -->
