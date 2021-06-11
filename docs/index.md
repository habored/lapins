# Terminal et REPL dans Mkdocs

## Introduction

Afin d'écrire un cours interactif utilisant sur Mkdocs, le besoin s'est fait sentir de pouvoir  écrire directement des scripts en ligne :

- dans le navigateur
- sans iframe
- sans cookie
- sans inscription

!!! info "Solution"
    La solution existe et s'appelle [Pyodide](https://pyodide.org/en/stable/ "Pyodide, Python with the scientific stack, compiled to WebAssembly"). 
    
    Pyodide utilise WebAssembly pour faire le lien entre Python et Javascript et proposer un environnement permettant de manipuler le DOM avec Python, ou de manipuler Python avec Javascript.

??? warning "Un hic"
    La documentation quasi-absente ou réservée aux experts du projet Pyodide...



## Prise en main

Je vous propose ici des commandes Markdown permettant de créer un terminal ainsi qu'un REPL grâce au **plugin macro**.

### Balises

Vite vite ! Le résultat, histoire d'appâter le chaland.

!!! summary "Les commandes"

    === "Terminal"
        ```markdown
        {% raw %}
        {{ terminal() }}
        {% endraw %}
        ```
        Cette commande crée un terminal vide. L'auto-complétion avec ++tab++ et le rappel de l'historique (avec ++ctrl+"R"++ ) sont possibles.

        {{ terminal () }}

    === "REPL vide"
        ```markdown
        {% raw %}
        {{ REPL() }}
        {% endraw %}
        ```
        Cette commande crée un REPL (~ Thonny) vide. L'engrenage permet de lancer le code tapé dans la zone de saisie (avec les numéros de ligne). La zone de saisie se redimensionne automatiquement et autorise l'auto-complétion avec ++tab++.

        {{REPL()}}

    === "REPL vertical"
        ```markdown
        {% raw %}
        {{ REPLv() }}
        {% endraw %}
        ```
        Cette commande crée un REPL vide, avec division verticale. L'engrenage permet de lancer le code tapé dans la zone de saisie (avec les numéros de ligne). La zone de saisie se redimensionne automatiquement et autorise l'auto-complétion avec ++tab++.

        {{REPLv()}}

    === "REPL avec code"
        ```markdown
        {% raw %}
        {{ REPL('nom_de_fichier') }}
        {% endraw %}
        ```
        Cette commande charge le fichier `nom_de_fichier.py` dans un REPL. Le fichier doit être dans `docs/scripts/`. Ne pas oublier les guillemets.

    === "REPL vertical avec code"
        ```markdown
        {% raw %}
        {{ REPLv('nom_de_fichier') }}
        {% endraw %}
        ```
        Cette commande charge le fichier `nom_de_fichier` dans un REPL avec division verticale. Le fichier doit être dans `docs/scripts/`.        

??? warning "Détails techniques"

    Tous les REPL et les terminaux partagent le même namespace. On peut donc accéder à n'importe quelle fonction créée dans n'importe quel REPL ou terminal. 
    
    **C'est un comportement voulu que l'on pourra discuter.**

!!! danger "Très très important"

    Pour que les REPL fonctionnent, il faut absolument indiquer `{% raw %} {{ REPL('nom_de_fichier', -1) }} {% endraw %}` sur le dernier REPL de la page. 
    
    **Notez le -1. Si vous souhaitez un REPL vide, utilisez `{% raw %} {{ REPL('', -1) }} {% endraw %}`**.

    Cette solution _temporaire_ permet de générer la balise `#!html <script>` permettant le chargement des REPL.

### Exemples

L'exemple ci-dessous, obtenu avec `#!markdown {% raw %} {{ REPLv('exo2') }} {% endraw %}`. N'hésitez pas à modifier le code pour calculer la moyenne, l'écart-type, afficher cela dans le terminal etc.

{{REPLv('exo2')}}

L'exemple ci-dessous a été obtenu avec `#!markdown {% raw %} {{ REPL('algo_glouton', -1) }} {% endraw %}`. C'est en effet le dernier REPL de la page.

{{REPL('algo_glouton', -1)}}


## Installation

L'installation demande d'ajouter :

- un dossier `custom_dir` de Mkdocs `#!bash my_theme_customizations/` ;
- un template HTML `#!bash my_theme_customizations/main.html` ;
- un fichier CSS `#!bash docs/xtra/stylesheets/pyoditeur.css` ;
- deux fichiers Javascript `#!bash docs/xtra/stylesheets/pyoditeur.css` ;
- des macros Python.

### Fichier YML





!!! {{exercice()}}

    === "Énoncé"

        ${1: enonce}

    === "Tips"

        ${1: enonce}

	=== "Solutions"

        ${2: sol}

`#!python lambda x : x**2`

`#!latex \left( \dfrac 1x \right)^2=1`

<!-- !!! danger "Les consoles"

    === "Une console Linux"
        {{ linux(700) }}

    === "Une console python"
        {{ basthon('scripts/exo1.py', 700) }} -->

Lorem ipsum dolor sit amet, consectetur
adipiscing elit. Proin at cursus nibh,
et lobortis mauris. Sed tempus turpis
quis turpis pulvinar, ac vehicula dui
convallis. Phasellus tempus massa quam,
ac mollis libero cursus eget.
Donec convallis a nisl vitae scelerisque.
Ut vel nisl id augue ullamcorper lobortis at id dolor.

    Lorem ipsum dolor sit amet, consectetur
adipiscing elit. Proin at cursus nibh,
et lobortis mauris. Sed tempus turpis
quis turpis pulvinar, ac vehicula dui
convallis. Phasellus tempus massa quam,
ac mollis libero cursus eget.
    Donec convallis a nisl vitae scelerisque.
    Ut vel nisl id augue ullamcorper lobortis
at id dolor.

> Ceci est un texte cité. Vous pouvez répondre
> à cette citation en écrivant un paragraphe
> normal juste en-dessous !

???+ warning "Attention au Python:"
    !!! summary "Voici un code Python:"
        ```python 
        [i**2 for i in range(10)]
        ```
    !!! summary "Voici un code Python:"
        ```python linenums="1" hl_lines="1-3"
        def tableau_markdown(liste: list) -> str:
            lignes = ['|n|']+[f'{i}|' for i in range(len(liste))]+['\n']
            lignes.extend(['|']+['-|']*(len(liste)+1) +['\n'])
            lignes.extend(['|u_n|']+[f'{liste[i]}|' for i in range(len(liste))])
            print(lignes)
            return "".join(lignes)
        ```

Pour afficher des touches, on fait `++ctrl++`+`++alt++`. 

++ctrl+alt++

++"Maj"+"Entrée"++

??? info "Fichier YAML"
    ```yaml
    --8<--- "mkdocs.yml"
    ```

## Inclure un fichier Python

!!! info "Fichier Python `docs/scripts/exo1.py`"
    ```python
    --8<--- "docs/scripts/exo1.py"
    ```

ou même !

!!! info "Fichier Python `docs/scripts/exo1.py`"


`Un blabla introductif:`
:   et voilà la définition

`Un blabla plus précis:`
:   et voilà une autre définition

    et ca marche avec deux paragraphes

J'essaie les caractères Unicode : `&#127140`&#127140

La définition de la fonction `premier` commence avec le mot clé `def`

Elle prend en paramètre un entier `n`

Elle renvoie un booléen avec le mot clé `return`

Let's try some Maths : 

$$\int_0^t x^2 \text{d}x$$

