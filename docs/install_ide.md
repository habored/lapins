# Guide de l'IDE

## Exemple

Un IDE se présente sous cette forme :

???+ info "Enroulez-moi !"

    {{IDE('exo2', MAX = "+", SANS = "eval,max")}}

Il dispose de six boutons :
<div class="py_mk_ide">
<ul>
<li> Lancer le script : <button class="tooltip"><img src="../pyodide-mkdocs/icons8-play-64.png"></button></li>
<li> Valider le script avec des tests unitaires : <button class="tooltip"><img src="../pyodide-mkdocs/icons8-check-64.png"></button></li>
<li> Télécharger le script actuel : <button class="tooltip"><img src="../pyodide-mkdocs/icons8-download-64.png"></button></li>
<li> Téléverser un script local : <button class="tooltip"><img src="../pyodide-mkdocs/icons8-upload-64.png"></button></li>
<li> Recharger l'énoncé : <button class="tooltip"><img src="../pyodide-mkdocs/icons8-restart-64.png"></button></li>
<li> Enregistrer le script actuel : <button class="tooltip"><img src="../pyodide-mkdocs/icons8-save-64.png"></button></li>
</ul>
</div>

??? info "Rappel RGPD"

    Tout se fait du côté client. **Rien n'est envoyé au serveur**.

## Prise en main

Par défaut, la commande `#!markdown {% raw %}{{IDE('exo2')}}{% endraw %}` permet de charger un script placé dans `docs/scripts/`.

!!! summary "Organisations possibles"

    === "Classement par chapitre"
    
        Votre page `markdown` constitue un chapitre et regroupe de nombreux exercices avec de nombreux IDE. 
        
        Dans ce cas, optez pour l'arborescence suivante :

        ```bash
        docs/
        ├── images
        │   └── projet2
        │       └── plante.png
        ├── index.md
        ├── projet1.md
        ├── projet2.md     ⬅︎ corps du chapitre que vous souhaitez écrire
        ├── projet3.md
        ├── scripts
        │   ├── projet2    ⬅︎ dossier contenant les exercices à intégrer à vos IDE
        │   │   ├── exo1.py
        │   │   ├── exo1_corr.py
        │   │   ├── exo1_test.py
        │   │   ├── exo2.py
        │   │   ├── exo2_corr.py
        │   │   ├── exo2_test.py
        │   │   ├── exo3.py
        │   │   ├── exo3_corr.py
        │   │   ├── exo3_test.py
        │   │   ├── exo4.py
        │   │   ├── exo4_corr.py
        │   │   ├── exo4_test.py
        │   │   ├── exo5.py
        │   │   ├── exo5_corr.py
        │   │   ├── plante_fractale.py
        │   │   └── tableau_dynamique.py
        ......
        ```
        
        Exemple : 
        
        `#!markdown {% raw %}{{IDE('projet2/exo2')}}{% endraw %}` chargera le script exo2.py depuis `docs/scripts/projet2/`.

    === "Classement par exercice" 
    
        Votre page `markdown` est spécialisée sur un exercice particulier, indiqué dans `mkdocs.yml`. 
        
        Dans ce cas, optez pour l'arborescence ci-dessous :

        ```bash
        docs/
        ├── N1
        │   ├── 110-maximum_nombres
        │   │   ├── exo.py
        │   │   ├── exo_corr.py
        │   │   ├── exo_test.py
        │   │   └── sujet.md
        ```

        Exemple : 
        
        - `mkdocs.yml` contient la ligne `#!markdown {% raw %}- "Calcul de max": N1/110-maximum_nombres/sujet.md{% endraw %}`. 
        - `#!markdown {% raw %}{{IDE('exo')}}{% endraw %}` chargera le script exo.py depuis `docs/N1/110-maximum_nombres/`.

!!! warning "Format de fichiers"

    === "Fichier d'exercice : `exo.py`"
        Le script Python est écrit de manière classique avec quelques particularités. 

        Il peut se décomposer en ces éléments (tous facultatifs) :

        ```python
        #MAX Nombre_d_essais_autorisés
        #--- HDR ---#
        """
        Code Python dans un header
        Ce code ne sera pas visible par l'élève et sera exécuté avant le code élève à l'exécution et à la validation
        
        Utile pour proposer des classes spécifiques à un exercice
        """
        #--- HDR ---#

        """
        Code élève à compléter
        """

        #Tests
        """
        Tests publics faits à l'exécution et à la validation
        Exemple: assert machin == 0, "vous avez une erreur de machin"
        """
        ```
        
        Les librairies standards sont pour la plupart acceptées, les limitations étant principalement graphiques. Les annotations de type, le walrus opérator sont acceptées.

    === "Fichier correction `exo_corr.py`"

        Le fichier Python de correction s'appelle `nom_de_script_corr.py`. 

        Vous pouvez répéter le HDR si vous le souhaitez afin que l'élève puisse tester en local

        ```python linenums="1"
        --8<-- "docs/scripts/exo2_corr.py"
        ```

    === "Fichier juge `exo_test.py` - Assert"

        Le fichier de juge en ligne peut être écrit de manière beaucoup plus "classique" en utilisant `#!python assert` :

        ```python linenums="1"
        --8<-- "docs/scripts/demo/demo2_test.py"
        ```
        
        Les `#!python assert` sont directement évalués par Pyodide. Seul le test ayant échoué sera affiché. Les tests réussis n'afficheront rien.
        
        Pas de problème pour tester autant de fonctions que nécessaire.

    === "Fichier juge `exo_test.py` - Benchmark"

        Le fichier de juge en ligne doit contenir une variable appelée `benchmark`, de type `#!python list` ou `#!python tuple` :

        1) Si l'on souhaite vérifier une unique fonction grâce à l'évaluateur de code :

        ```python linenums="1"
        --8<-- "docs/scripts/demo/demo1_test.py"
        ```
        
        On a donc un tuple de chaînes de caractères qui sera évalué avec `#!python eval()`. 
 
        2) Si l'on souhaite vérifier plusieurs fonctions grâce à l'évaluateur de code :
   
        ```python linenums="1"
        --8<-- "docs/scripts/exo2_test.py"
        ```

        On a donc un tuple de tableau de chaînes de caractères qui sera évalué avec `#!python eval()`. 

!!! warning "Important"

    Le bouton de validation du script à l'aide de tests unitaires est présent uniquement si vous fournissez un fichier `nom_du_fichier_test.py` présent dans le même répertoire que `nom_du_fichier.py`.

    La solution apparait au bout du nombre de tests unitaires définis dans le fichier ou directement dans la création de l'IDE seulement si vous fournissez un fichier `nom_du_fichier_corr.py`dans le même répertoire que `nom_du_fichier.py`.

    Les boutons de lancement du script, de téléchargement, de téléversement, de sauvegarde et de rechargement sont présents par défaut.

!!! conclu "Conclusion"

    À condition que les fichiers `fichier.py`, `fichier_corr.py` et `fichier_test.py` soient présents, `#!markdown {% raw %}{{IDE('foo/bar/truc/muche/fichier')}}{% endraw %}` gère **tout seul** :

    - l'énoncé, 
    - le juge en ligne, 
    - les fichiers de correction


<!-- !!! info "Exercices sur la longueur d'un tableau"

    === "Exercice 1"
        Complétez la fonction `longueur` afin que celle-ci renvoie la taille d'un tableau L.
        
        {{IDE('demo/demo1')}}


    === "Exercice 2"
        Complétez la fonction `longueur_ajout` afin que celle-ci renvoie la taille de deux tableaux T1 et T2.
        {{IDE('demo/demo2')}}

    === "Exercice 3"
        On découpe une phrase à l'aide de l'instruction [split](https://docs.python.org/fr/3/library/stdtypes.html#str.split "Instruction split en Python").

        Complétez la fonction `nombre_mots` afin que celle-ci renvoie le nombre de mots séparé par un espace d'une phrase `phrase`.
        {{IDEv('demo/demo3')}}

On peut bien sur enrouler tout cela... -->



<!--
??? info "Exercices sur la longueur d'un tableau"

    === "Exercice 1"
        Complétez la fonction `longueur` afin que celle-ci renvoie la taille d'un tableau L.
    
        {{IDE('demo/demo1')}}
        
    === "Exercice 2"
        Complétez la fonction `longueur_ajout` afin que celle-ci renvoie la taille de deux tableaux T1 et T2.
        {{IDE('demo/demo2')}}

    === "Exercice 3"
        On découpe une phrase à l'aide de l'instruction [split](https://docs.python.org/fr/3/library/stdtypes.html#str.split "Instruction split en Python").

        Complétez la fonction `nombre_mots` afin que celle-ci renvoie le nombre de mots séparé par un espace d'une phrase `phrase`.
        {{IDEv('demo/demo3')}}


## Technique !

_Pour l'instant, j'ai la grosse flemme d'écrire cette section._

En quelques mots, on crée deux `#!html div` désigné par un numéro auto-incrémenté : 

- `#!html <div id="editor_6">` crée la partie éditeur de texte. Ce `#!html div` est converti en éditeur grâce à l'[éditeur ACE](https://ace.c9.io "ACE Editor") ;
- `#!html <div id="term_editor_6">` crée la partie Terminal. Le Terminal n'est créé qu'au moment de la validation du script ou du juge en ligne. Il est créé grâce au plugin Terminal de jQuery par converstion du `#!html div` (voir section Guide du Terminal).


<!-- ??? info "Patience, patience"

    Le guide du IDE arrive bientôt.
 -->
