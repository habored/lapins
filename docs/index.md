# Pyodide-MkDocs 0.8 : Terminal et IDE dans MkDocs

## Introduction

`Pyodide-MkDocs` est une solution technique permettant de créer un cours interactif à partir d'un site généré par MkDocs. 

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
    
    Pyodide utilise WebAssembly pour faire le lien entre Python et Javascript et proposer un environnement permettant de manipuler le DOM avec Python, ou de manipuler Python avec Javascript.

## Aperçu

{{IDE('dentiste/exo', MAX = 5)}}

## Démarrage rapide

Vous ne connaissez rien à MkDocs et vous souhaitez vous y mettre ? Des mots comme `yaml`, `javascript`, `Pyodide` ou templates `Jinja` vous font peur ? 

Commencez en douceur en partant d'un repo MkDocs aux dernières normes en vigueur : clonez le [répertoire Git](https://gitlab.com/ens-fr/exp2) !

## Installation

On part d'une installation comme indiqué sur [ce lien](https://ens-fr.gitlab.io/mkdocs/) avec le **plugin macro**, préalablement installé.

L'installation demande de rajouter à cette configuration les éléments suivants.

__Modification apportée__ :
  
- fichier YML `mkdocs.yml` ;
- fichier de macro `main.py` ;

__Ajout nécessaire__ :

- un dossier `#!bash my_theme_customizations/` à la racine du projet MkDocs ;
- un template HTML `#!bash my_theme_customizations/main.html` ;
- un fichier CSS `#!bash my_theme_customizations/pyodide-mkdocs/pyoditeur.css` ;
- deux fichiers Javascript `#!bash my_theme_customizations/pyodide-mkdocs/interpreter.js` et `#!bash my_theme_customizations/pyodide-mkdocs/ide.js` ;
- six images de boutons.

### Fichier YML `mkdocs.yml`

Ajoutez la ligne appelée `custom_dir` dans la partie `theme` de votre fichier mkdocs.yml :

```yaml
theme:
  name: material
  custom_dir: my_theme_customizations/
```

### Fichier macro Python `main.py`

À votre fichier `main.py`, ajoutez les lignes du fichier [`main.py`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/main.py "main.py sur Gitlab"). Vous devez disposer de Python 3.5 au minimum. 


### Création du dossier `custom_dir`

**N'oubliez pas de créer le dossier `#!bash my_theme_customizations/` à la racine du projet MkDocs**.

Dans ce dossier, ajoutez le template Jinja [`#!bash main.html`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/my_theme_customizations/main.html).

### Fichier CSS `pyoditeur.css`

Afin de coller au thème du site, recopiez et ajoutez le fichier [`pyoditeur.css`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/my_theme_customizations/pyodide-mkdocs/pyoditeur.css "Pyoditeur CSS sur Gitlab") au dossier `my_theme_customizations/pyodide-mkdocs/`.

??? note "Couleurs" 

    Si vous avez opté pour d'autres couleurs, c'est là que vous pourrez faire les modifications de l'éditeur.

### Fichiers javascripts `interpreter.js` et `ide.js`

Deux fichiers Javascript [`interpreter.js`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/my_theme_customizations/pyodide-mkdocs/interpreter.js "interpreter JS sur Gitlab ") et [`ide.js`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/my_theme_customizations/pyodide-mkdocs/ide.js "ide JS sur Gitlab ") sont nécessaires :

Ces fichiers doivent être placés dans le dossier : `my_theme_customizations/pyodide-mkdocs/`.

### Images des boutons

Les boutons doivent être placés à cette adresse : `/docs/images/buttons/`. Il existe six boutons que vous pouvez récupérer en téléchargeant l'[archive](images/buttons/Buttons.zip).

## Syntaxe et exemples

### Syntaxe Markdown

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
        {{ IDE('foo/bar/nom_de_fichier', MAX = 8, SANS = 'max,min') }}
        {% endraw %}
        ```
        Cette commande charge le fichier `nom_de_fichier.py` dans un IDE. Le fichier doit être dans `docs/scripts/foo/bar/`. Ne pas oublier les guillemets. 
        
        `MAX = 8` indique le nombre maximal de tentatives de validation que l'élève peut effectuer. `MAX = 1000` permet de mettre ce nombre à l'infini. Valeur par défaut : `MAX = 5` .

        `SANS = 'max,min'` permet d'interdire l'utilisation des fonctions built-ins `#!python max` et `#!python min`.

        Les IDE sont enregistrés à intervalle de temps régulier. Ils permettent également l'autocomplétion avec la combinaison de touches ++alt+space++.

        {{IDE('demo/demo1')}}

    === "IDE vertical avec code"
        ```markdown
        {% raw %}
        {{ IDEv('foo/bar/nom_de_fichier', MAX = 1000) }}
        {% endraw %}
        ```
        Cette commande charge le fichier `nom_de_fichier` dans un IDE avec division verticale. Le fichier doit être dans `docs/scripts/foo/bar/`.       

        {{IDEv('demo/demo1', MAX = 3)}}
 

??? warning "Détails techniques"

    Tous les IDE et les terminaux partagent le même _namespace_. On peut donc accéder à n'importe quelle fonction créée dans n'importe quel IDE ou terminal. 
    
    **C'est un comportement qui a l'avantage de pouvoir proposer des exercices où l'on construit petit à petit un code complexe.**


### Exemples

L'exemple ci-dessous, obtenu avec `#!markdown {% raw %} {{ IDEv('exo2') }} {% endraw %}`. N'hésitez pas à modifier le code pour calculer la moyenne, l'écart-type, afficher cela dans le terminal etc.

{{IDEv('exo2')}}

L'exemple ci-dessous a été obtenu avec `#!markdown {% raw %} {{ IDE('algo_glouton') }} {% endraw %}`.

{{IDE('algo_glouton')}}

