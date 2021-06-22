# Des questions techniques et métaphysiques

## Partis pris

!!! warning "Namespace partagé"
    
    Je trouve ce mode très pratique car on conserve nos fonctions et variables d'un terminal à l'autre au cours d'une leçon. 
    
    Pédagogiquement, c'est plus discutable car certaines variables seront initialisées dans le Terminal 1 et utilisées dans le Terminal 2. Cela cache la notion d'initialisation.

!!! done "REPL vertical"

    Est-ce vraiment utile de les conserver ?
    
    ~~Cela ralentit le chargement de la page web et consomme des ressources pour l'auto-redimensionnement de la partie terminal du REPL. Cela est spécialement visible sur mobile (ou ce mode est d'ailleurs inutile).~~

    Quelques modifications ont permis de les conserver sans altérer les performances.  

!!! done "macro Python"

    ~~Ma solution est un peu sale mais a-t-on vraiment le choix avec l'inclusion de balise HTML ?~~

    J'ai choisi de diviser le problème en sous-fonctions. Cela semble plus lisible à présent avec : lecture de fichier avec `#!python def read_ext_file()` et `#!python def generate_content()`, une seule macro REPL avec deux modes ('v' et 'h' par défaut).


## En développement

!!! done "Fichiers javascripts"

    ~~C'est le bazar dans l'appel des fichiers JS. Si quelqu'un peut me mettre de l'ordre dans tout cela, je suis preneur !~~

    J'ai repris l'organisation générale. C'est toujours un peu le bazar mais cela me semble acceptable.


!!! help "Importation automatique de module"

    Pyodide propose un module `#!python micropip` permettant de charger les modules manquants. Nous pourrions faire des interfaces graphiques à l'aide de cela mais est-ce vraiment utile ? 

!!! done "Evaluateur de code"

    ~~Avec l'utilisation du code de [fjunier](https://mooc-forums.inria.fr/moocnsi/t/mkdocs-une-solution-ideale/1758/175), nous pourrions intégrer un juge en ligne ? Utile ou non ?~~

    L'évaluateur de code est fonctionnel et permet de faire des benchmarks complexes.
    
    Le bouton du juge en ligne n'apparaitra que s'il existe un fichier de benchmark **`test_nom_de_script.py`**.

    Le corrigé n'apparaitra que si un fichier de **`corr_nom_de_script.py`** est présent.

    Il faudra créer un pipe pour générer automatiquement un fichier de benchmark depuis un script de corrigé.


!!! done "Javascript et REPL"

    ~~La solution avec le -1 dans `main.py`, discutée dans le guide technique du REPL, est vraiment naze. Il faut trouver autre chose.~~
    
    Je devais vraiment dormir. On peut tout simplement ajouter une ligne dans le template Jinja2 `main.html` du `custom_dir` de mkdocs. Cela permet de charger le javascript nécessaire au bon fonctionnement des REPL sans s'embêter.

!!! done "Boutons et REPL"

    ~~La solution avec le -1 dans `main.py`, discutée dans le guide technique du REPL, est vraiment naze. Il faut trouver autre chose.~~
    
    Ajout de boutons permettant de télécharger les scripts écrits et téléverser les scripts disponibles localement. Evaluateur de code ajouté.