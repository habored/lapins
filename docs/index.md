# Pyodide-MkDocs 0.9.1 : Terminal et IDE dans MkDocs

## Introduction

Pyodide-MkDocs est une solution technique permettant de créer un cours interactif à partir d'un site statique généré par MkDocs. 

Il permet d'intégrer, dans le navigateur, côté client :

- une console Python ;
- un éditeur de code ;
- un juge en ligne associé à des corrigés.

Garantie :

- [x] sans cookie
- [x] sans inscription
- [x] créé par un enseignant pour les enseignants

??? info "Solution"
    La technologie permettant ce tour de force s'appelle [Pyodide](https://pyodide.org/en/stable/ "Pyodide, Python with the scientific stack, compiled to WebAssembly").
    
    Pyodide utilise WebAssembly pour faire le lien entre Python et Javascript et proposer un environnement permettant de manipuler le DOM Javascript avec Python, ou inversement de manipuler Python avec Javascript.

## Aperçu

Une installation complète permet d'obtenir ce résultat :

{{IDE('dentiste/exo', MAX = 3)}}

<!--## Démarrage rapide

Vous ne connaissez rien à MkDocs et vous souhaitez vous y mettre ? Des mots comme `yaml`, `javascript`, `Pyodide` ou templates `Jinja` vous font peur ? 

Commencez en douceur en partant d'un repo MkDocs aux dernières normes en vigueur : clonez le [répertoire Git](https://gitlab.com/ens-fr/exp2) !-->

## Installation

### Prérequis

- Material for MkDocs : par exemple, installé comme indiquée sur [cet excellent lien](https://ens-fr.gitlab.io/mkdocs/) ;
- [Plugin macro](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) ;
- Python 3.5 et supérieur.

### Ajout nécessaire

À la racine du projet MkDocs (dans le dossier docs/), vous devez décompresser l'archive .zip téléchargeable [en cliquant ici](my_theme_customizations.zip) :

??? question "Plus d'information"

    Cela rajoutera les éléments suivants à votre configuration :

    - un dossier `#!bash my_theme_customizations/` ; <!-- originally it's `bundled_custom_dir` without the banner -->
    - un template HTML `#!bash my_theme_customizations/main.html` ;
    - un fichier CSS `#!bash my_theme_customizations/pyodide-mkdocs/pyoditeur.css` ;
    - trois fichiers Javascript `#!bash my_theme_customizations/pyodide-mkdocs/interpreter.js`, `#!bash my_theme_customizations/pyodide-mkdocs/ide.js` et `#!bash my_theme_customizations/pyodide-mkdocs/utils.js`;
    - six images de boutons.

### Modification apportée

Vous devez également modifier deux fichiers créés lors de votre installation de Material for Mkdocs.

!!! question  "Fichiers à modifier"

    === "Fichier YAML `mkdocs.yml`"

        Ajoutez la ligne appelée `custom_dir` dans la partie `theme` de votre fichier mkdocs.yml :

        ```yaml
        theme:
          name: material
          custom_dir: my_theme_customizations/
        ```

    === "Fichier de macro `main.py`"

        À votre fichier `main.py`, ajoutez les lignes comprises entre _Debut copie_ et _Fin copie_ du fichier [`main.py`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/release/0.9.0/main.py "main.py sur Gitlab"). 

        Il y a deux blocs : le bloc des `python import` et le bloc de code.

## Syntaxe et exemples

!!! summary "La syntaxe"

    === "Terminal"
        ```markdown
        {% raw %}
        {{ terminal() }}
        {% endraw %}
        ```
        Création d'un terminal vide. L'auto-complétion avec ++tab++ et le rappel de l'historique (avec ++ctrl+"R"++ ) sont possibles.

        {{ terminal () }}

    === "IDE vide"
        ```markdown
        {% raw %}
        {{ IDE() }}
        {% endraw %}
        ```
        Création d'un IDE vide, visuellement proche de Thonny. La zone de saisie se redimensionne automatiquement et autorise l'auto-complétion de type _snippet_ avec ++alt+space++.

        {{IDE()}}

    === "IDE vertical"
        ```markdown
        {% raw %}
        {{ IDEv() }}
        {% endraw %}
        ```
        Cette commande crée un IDE vide, avec division verticale. 

        {{IDEv()}}

    === "IDE avec code"
        ```markdown
        {% raw %}
        {{ IDE('foo/bar/nom_de_fichier', MAX = 8, SANS = 'max,min') }}
        {% endraw %}
        ```
        
        - Le fichier `nom_de_fichier.py` est chargée dans un IDE. Ce fichier doit être situé impérativement dans `docs/scripts/foo/bar/`. 
    
        - `MAX = 8` : indique le nombre maximal de tentatives de validation que l'élève peut effectuer. `MAX = 1000` ou `MAX = "+"` permet de mettre ce nombre à l'infini. Valeur par défaut : `MAX = 5` .

        - `SANS = 'max,min'` permet d'interdire l'utilisation des fonctions built-ins `#!python max` et `#!python min`.

        Les IDE sont enregistrés à intervalle de temps régulier. Ils permettent également l'autocomplétion avec la combinaison de touches ++alt+space++.

        {{IDE('demo/demo1')}}

    === "IDE vertical avec code"
        ```markdown
        {% raw %}
        {{ IDEv('foo/bar/nom_de_fichier', MAX = 1000) }}
        {% endraw %}
        ```
        Cette commande charge le fichier `nom_de_fichier` dans un IDE avec division verticale. Le fichier doit être dans `docs/scripts/foo/bar/`.       

        {{IDEv('demo/demo2', MAX = 3)}}
 

??? warning "Détails techniques"

    Tous les IDE et les terminaux partagent le même _namespace_. On peut donc accéder à n'importe quelle fonction créée dans n'importe quel IDE ou terminal. 
    
    C'est un comportement qui a l'avantage de pouvoir proposer des exercices où l'on construit petit à petit un code complexe mais qui fera l'objet de changement important à l'avenir.