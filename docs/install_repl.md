# Guide du REPL

## Exemple

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

Pour une organisation en chapitre, utilisez un chemin relatif. Par exemple : `#!markdown {% raw %}{{REPL('foo/bar/exo2')}}{% endraw %}` chargera le script exo2.py depuis `docs/scripts/foo/bar`.

!!! warning "Important"

    Le bouton de validation du script à l'aide de tests unitaires est présent uniquement si vous fournissez un fichier `test_nom_du_fichier.py` présent dans le même répertoire que `nom_du_fichier.py`.

    La solution apparait au bout de 5 tests unitaires si vous fournissez un fichier `corr_nom_du_fichier.py`dans le même répertoire que `nom_du_fichier.py`.

    Le lancement du script, le téléchargement et le téléversement sont présentes par défaut.

!!! warning "Format de fichiers"

    === "Fichier Python"
        Le script Python est écrit de manière classique. 
        
        Les librairies standards sont acceptés. Les annotations, même complexes, sont normalement acceptées : merci de me contacter si vous observez des comportements inattendus.
        

    === "Fichier Correction"

        Le fichier Python de correction `corr_nom_de_script.py` est écrit de manière classique. 

        ```python linenums="1"
        --8<-- "docs/scripts/corr_exo2.py"
        ```

    === "Fichier Juge"

        Le fichier de juge en ligne doit contenir une variable appelée `benchmark`, de type `#!python list` ou `#!python tuple` :

        1) Si l'on souhaite vérifier une unique fonction grâce à l'évaluateur de code :

        ```python linenums="1"
        --8<-- "docs/scripts/demo/test_demo2.py"
        ```
        
        On a donc un tableau de chaines de caractères qui seront évaluées avec `#!python eval()`. Attention donc aux caractères d'échappement.
 
        1) Si l'on souhaite vérifier plusieurs fonctions grâce à l'évaluateur de code :
   
        ```python linenums="1"
        --8<-- "docs/scripts/test_exo2.py"
        ```

        On a donc un tableau de tableau de chaines de caractères qui seront évaluées avec `#!python eval()`. 


    

!!! conclu "Conclusion"

    À condition que les fichiers `corr_` et `test_`soient présents, `#!markdown {% raw %}{{REPL('foo/bar/truc/muche/fichier')}}{% endraw %}` gère **tout seul** :

    - l'énoncé, 
    - le juge en ligne, 
    - les fichiers de correction

## Technique !

_Pour l'instant, j'ai la grosse flemme d'écrire cette section._

En quelques mots, on crée deux `#!html div` désigné par un numéro auto-incrémenté : 

- `#!html <div id="editor_6">` crée la partie éditeur de texte. Ce `#!html div` est converti en éditeur grâce à l'[éditeur ACE](https://ace.c9.io "ACE Editor") ;
- `#!html <div id="term_editor_6">` crée la partie Terminal. Le Terminal n'est créé qu'au moment de la validation du script ou du juge en ligne. Il est créé grâce au plugin Terminal de jQuery par converstion du `#!html div` (voir section Guide du Terminal).


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
