# Terminal et IDE dans Mkdocs

{{ macros_info() }}



## Introduction

Afin d'écrire un cours interactif utilisant Mkdocs, le besoin s'est fait sentir de pouvoir écrire des scripts Python en ligne directement dans le navigateur.

Garantie :

- [x] sans iframe
- [x] sans cookie
- [x] sans inscription

!!! info "Solution"
    La solution existe et s'appelle [Pyodide](https://pyodide.org/en/stable/ "Pyodide, Python with the scientific stack, compiled to WebAssembly").
    
    Pyodide utilise WebAssembly pour faire le lien entre Python et Javascript et proposer un environnement permettant de manipuler le DOM avec Python, ou de manipuler Python avec Javascript.

??? warning "Un hic"
    La documentation quasi-absente ou réservée aux initiés du projet Pyodide...


## Prise en main

Voici les commandes Markdown permettant de créer un terminal ainsi qu'un IDE grâce au **plugin macro**.

### Syntaxe Markdown

Mais d'abord, le résultat, histoire d'appâter le chaland.

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
        Création d'un IDE (~ Thonny) vide. La flèche permet de lancer le code tapé dans la zone de saisie (avec les numéros de ligne). La zone de saisie se redimensionne automatiquement et autorise l'auto-complétion de type _snippet_ avec ++tab++.

        {{IDE()}}

    === "IDE vertical"
        ```markdown
        {% raw %}
        {{ IDEv() }}
        {% endraw %}
        ```
        Cette commande crée un IDE vide, avec division verticale. La flèche permet de lancer le code tapé dans la zone de saisie (avec les numéros de ligne). La zone de saisie se redimensionne automatiquement et autorise l'auto-complétion de type snippet avec ++tab++.

        {{IDEv()}}

    === "IDE avec code"
        ```markdown
        {% raw %}
        {{ IDE('foo/bar/nom_de_fichier', MAX = 8) }}
        {% endraw %}
        ```
        Cette commande charge le fichier `nom_de_fichier.py` dans un IDE. Le fichier doit être dans `docs/scripts/foo/bar/`. Ne pas oublier les guillemets. 
        
        `MAX = 8` indique le nombre maximal de tentatives de validation que l'élève peut effectuer. `MAX = 1000` permet de mettre ce nombre à l'infini. Valeur par défaut : `MAX = 5` .

        {{IDE('demo/demo1')}}

    === "IDE vertical avec code"
        ```markdown
        {% raw %}
        {{ IDEv('foo/bar/nom_de_fichier', MAX = 1000) }}
        {% endraw %}
        ```
        Cette commande charge le fichier `nom_de_fichier` dans un IDE avec division verticale. Le fichier doit être dans `docs/scripts/foo/bar/`.       

        {{IDEv('demo/demo1', MAX = 3)}}
 

???+ warning "Détails techniques"

    Tous les IDE et les terminaux partagent le même _namespace_. On peut donc accéder à n'importe quelle fonction créée dans n'importe quel IDE ou terminal. 
    
    **C'est un comportement qui a l'avantage de pouvoir proposer des exercices où l'on construit petit à petit un code complexe.**


### Exemples

L'exemple ci-dessous, obtenu avec `#!markdown {% raw %} {{ IDEv('exo2') }} {% endraw %}`. N'hésitez pas à modifier le code pour calculer la moyenne, l'écart-type, afficher cela dans le terminal etc.

{{IDEv('exo2')}}

L'exemple ci-dessous a été obtenu avec `#!markdown {% raw %} {{ IDE('algo_glouton') }} {% endraw %}`.

{{IDE('algo_glouton')}}


## Installation

On part d'une installation comme indiqué sur https://ens-fr.gitlab.io/mkdocs/ avec le module macro.

L'installation demande de rajouter à cette configuration les éléments suivants.

__Modification__ :
  
- fichier YML `mkdocs.yml` ;
- fichier de macro `main.py` ;

__Ajout__ :

- un dossier `#!bash my_theme_customizations/` à la racine du projet Mkdocs ;
- un template HTML `#!bash my_theme_customizations/main.html` ;
- un fichier CSS `#!bash docs/xtra/stylesheets/pyoditeur.css` ;
- deux fichiers Javascript `#!bash docs/xtra/javascripts/interpreter.js` et `#!bash my_theme_customizations/js/ide.js` ;
- deux fichiers Markdown `#!bash docs/xtra/start.md` et `#!bash docs/xtra/end.md`.

### Fichier YML `mkdocs.yml`

Ajoutez les lignes surlignées dans votre fichier mkdocs.yml .

```yaml hl_lines="7 16 19"
    --8<--- "docs/scripts/mkdocs.yml"
```

### Fichier macro Python `main.py`

À votre fichier `main.py`, ajoutez les lignes du fichier [`main.py`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/docs/scripts/main.py "main.py sur Gitlab").


### Création du dossier `custom_dir`

**N'oubliez pas de créer le dossier `#!bash my_theme_customizations/` à la racine du projet Mkdocs**.

Dans ce dossier, ajoutez le template Jinja `#!bash main.html` :

```jinja
    --8<--- "my_theme_customizations/main.html"
```

### Fichier CSS `pyoditeur.css`

Afin de coller au thème du site, recopiez et ajoutez le fichier [`pyoditeur.css`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/docs/xtra/stylesheets/pyoditeur.css "Pyoditeur CSS sur Gitlab") au dossier `docs/xtra/stylesheets/`.

### Fichiers javascripts `interpreter.js` et `ide.js`

Deux fichiers Javascript [`interpreter.js`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/docs/xtra/javascripts/interpreter.js "interpreter JS sur Gitlab ") et [`ide.js`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/my_theme_customizations/js/ide.js "ide JS sur Gitlab ") sont nécessaires :

- `interpreter.js` doit être placé dans le dossier : `docs/xtra/javascripts/` ;
- `ide.js` doit être placé dans le dossier : `my_theme_customizations/js/ide.js`.

### Fichiers `start.md` et `end.md`

Pour la bonne gestion des fichiers de remarque, il faut également ajouter deux fichiers standardisés au format markdown : [`start.md`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/docs/xtra/start.md "start.md sur Gitlab ") et [`end.md`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/docs/xtra/end.md "end.md sur Gitlab ")

**Et c'est tout !**