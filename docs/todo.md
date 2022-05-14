# Des questions techniques et métaphysiques

## Versions

???+ warning "0.13"

    === "Ajouts majeurs"
        - Correctif majeur du système de sauvegarde des travaux élèves évitant le problème de doublons et IDE avec les mauvais énoncés : <span style="color:red">sur le navigateur, cliquer sur outils de développement puis dans la console javascript, écrivez : <code>localStorage.clear()</code>.</span>
        - Ajout d'un nouveau système de gestion des palettes de couleur et des modes jour/nuit. La palette de couleur utilisé par Pyodide-Mkdocs est automatiquement la couleur primaire utilisé par le site sous Mkdocs. 
        Il est possible de spécifier les themes de coloration de l'éditeur ACE via le `mkdocs.yml` comme dans l'exemple ci-dessous :
        ```yml
        extra:
            ace_style: # https://ace.c9.io/build/kitchen-sink.html pour avoir plus de themes
                default: crimson_editor  # mode jour
                slate: tomorrow_night_bright   # mode nuit
                # slate: tomorrow_night_bright|youtube (if your dark mode is youtube for example)
        ```
        - Ajout d'un système d'activation/désactivation des tests publics. 

    === "Correctifs mineurs"
        - Raccourci clavier pour autocomplétion modifié : ++alt+tab++ ;
        - Correction affichage des tooltip pour les boutons ;
        - Correction bug existant avec IDE vide et disparition de ligne.

## Todo list

:x: QCM intégré à Mkdocs

:x: intégration de drawSVG

:x: variable dans le mkdocs.yml pour positionner le fichier REM à l'endroit où on le souhaite

:x: Démarrer le comptage des 5 essais avant révélation du code si les premiers tests sont passés.

:x: La fenêtre d’édition est réservée au code de l’élève. Les premiers tests sont dans une fenêtre collée, juste en dessous, visible mais non éditable. Ils peuvent être masqués/affichés.

:x: Amélioration des performances d'affichage

:x: télécharger tous les codes écrits dans les éditeurs de la page en un seul fichier

:x: Doctests

:white_check_mark: Rendre la couleur de l'IDE plus robuste aux changements de palette

:white_check_mark: Adaptable size tooltip

:white_check_mark: Toggle tests on/off

:white_check_mark: Colorisation automatique de l'IDE

:white_check_mark: Bug plusieurs onglets: [voir](https://mooc-forums.inria.fr/moocnsi/t/re-pyodide-mkdocs/5715/4)

:white_check_mark: Autocomplétion du code avec une touche simple (pas de Live autocomplétion -_-)

:white_check_mark: `#!python eval` désactivé en fonction de la présence du mot-clé `#!md SANS = 'eval,max'` dans l'appel à `#!md IDE(..., SANS = ...)`. Prendre en compte les erreurs du créateur `#!md SANS = 'eval, MaX  ,   min'`.

:white_check_mark: Erreur d'assertions et gestion de crash de code

- [x] Mode verbose pour les tests / mode simple
- [x] Mode infini pour les tentatives

:white_check_mark: sauvegarde des codes lors d'un rechargement de la page (oui!!!!)

:white_check_mark: gestion des fichiers d'initialisation (pour les codes longs)

:white_check_mark: Le code solution apparait dans le code source... A cacher d'une manière ou d'une autre

:white_check_mark: Mode sombre / Mode clair (réglage indépendant du choix de palette)

:white_check_mark: Caractères non-ASCII pour nom de fichier et contenu

:white_check_mark: Fichier de remarque, `<nom_du_truc>_rem.txt` 

- [x] Solution en page externe pour les fichiers longs (exclue du menu de navigation avec le hack)
- [x] Solution en menu déroulant pour les fichiers courts

:white_check_mark: Modifications des emoji par des svg classe

:white_check_mark: Infobulles

:white_check_mark: Chemins relatifs

:white_check_mark: Nombre d'essais variés


## En développement

!!! help "Inclure des fichiers externes avec macros fonctionnels"

    Jinja syntax to include an external remark file, including an IDE to give the correction :

    ```{{ "{% include 'scripts/demo/demo2_rem.txt' %}" }}```

    This is the future of the online judge

    Can include automatically a correction. Needs lots of refactoring though ⏳⏳⏳. 


!!! done "REPL > IDE"

    Une reprise complète de la dénomination a été faite. Les REPL s'appellent maintenant (et à raison) [IDE](https://fr.wikipedia.org/wiki/Environnement_de_développement "Définition IDE") Merci Fred Leleu pour le travail supplémentaire 😍 .

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


!!! done "Javascript et IDE"

    ~~La solution avec le -1 dans `main.py`, discutée dans le guide technique du IDE, est vraiment naze. Il faut trouver autre chose.~~
    
    Je devais vraiment dormir. On peut tout simplement ajouter une ligne dans le template Jinja2 `main.html` du `custom_dir` de mkdocs. Cela permet de charger le javascript nécessaire au bon fonctionnement des IDE sans s'embêter.

!!! done "Boutons et IDE"

    ~~La solution avec le -1 dans `main.py`, discutée dans le guide technique du IDE, est vraiment naze. Il faut trouver autre chose.~~
    
    Ajout de boutons permettant de télécharger les scripts écrits et téléverser les scripts disponibles localement. Evaluateur de code ajouté.


## Partis pris

!!! warning "_Namespace_ partagé"
    
    Je trouve ce mode très pratique car on conserve nos fonctions et variables d'un terminal à l'autre au cours d'une leçon. 
    
    Pédagogiquement, c'est plus discutable car certaines variables seront initialisées dans le Terminal 1 et utilisées dans le Terminal 2. Cela cache la notion d'initialisation.

!!! done "IDE vertical"

    Est-ce vraiment utile de les conserver ?
    
    ~~Cela ralentit le chargement de la page web et consomme des ressources pour l'auto-redimensionnement de la partie terminal du IDE. Cela est spécialement visible sur mobile (ou ce mode est d'ailleurs inutile).~~

    Quelques modifications ont permis de les conserver sans altérer les performances.  

!!! done "macro Python"

    ~~Ma solution est un peu sale mais a-t-on vraiment le choix avec l'inclusion de balise HTML ?~~

    J'ai choisi de diviser le problème en sous-fonctions. Cela semble plus lisible à présent avec : lecture de fichier avec `#!python def read_ext_file()` et `#!python def generate_content()`, une seule macro IDE avec deux modes ('v' et 'h' par défaut).

!!! warning "Palette Ideas"

    // __md_scope=new URL(".",location)
    // __md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e))
    // console.log('BLAM', __md_scope)
    // console.log('localStorage', localStorage)
    // console.log('localStorage 2', __md_scope.pathname+"."+"__palette")
    // console.log('localStorage 3', localStorage.getItem(__md_scope.pathname+"."+"__palette"))
    // console.log('localStorage 4', __md_get("__palette").index, __md_get("__palette").color.scheme)
