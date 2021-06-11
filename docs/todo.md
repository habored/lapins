# Des questions techniques et métaphysiques.

## Partis pris

!!! warning "Namespace partagé"
    
    Je trouve ce mode très pratique car on conserve nos fonctions et variables d'un terminal à l'autre au cours d'une leçon. 
    
    Pédagogiquement, c'est plus discutable car certaines variables seront initialisées dans le Terminal 1 et utilisées dans le Terminal 2. Cela cache la notion d'initialisation.

!!! warning "REPL vertical"

    Est-ce vraiment utile de les conserver ?
    
    Cela ralentit le chargement de la page web et consomme des ressources pour l'auto-redimensionnement de la partie terminal du REPL. Cela est spécialement visible sur mobile (ou ce mode est d'ailleurs inutile).

!!! help "macro Python"

    Ma solution est un peu sale mais a-t-on vraiment le choix avec l'inclusion de balise HTML ? 

    La solution de [fjunier](https://mooc-forums.inria.fr/moocnsi/t/mkdocs-une-solution-ideale/1758/175) avec l'utilisation des `--8<---` est peut-être plus lisible en évitant l'ouverture de fichier en Python ?


## En développement

!!! warning "Fichiers javascripts"

    C'est le bazar dans l'appel des fichiers JS. Si quelqu'un peut me mettre de l'ordre dans tout cela, je suis preneur !

!!! help "Importation automatique de module"

    Pyodide propose un module `#!python micropip` permettant de charger les modules manquants. Nous pourrions faire des interfaces graphiques à l'aide de cela mais est-ce vraiment utile ? 

!!! help "Evaluateur de code"

    Avec l'utilisation du code de [fjunier](https://mooc-forums.inria.fr/moocnsi/t/mkdocs-une-solution-ideale/1758/175), nous pourrions intégrer un juge en ligne ? Utile ou non ?

!!! danger "Javascript et REPL"

    La solution avec le -1 dans `main.py`, discutée dans le guide technique du REPL, est vraiment naze. Il faut trouver autre chose. 
    
    Ai-je été endormi lors des premiers développements ? Qui a une solution facile ?