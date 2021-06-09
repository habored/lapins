# : Terminal et REPL dans Mkdocs

## Introduction
<!-- <div class="wrapper">
<div class="interior_wrapper">
<div id="editor_1">docs/scripts/exo1.py</div> 
</div>
<div id="term_editor_1" class="term_editor"></div>
</div>
<button onclick='interpretACE("editor_1")' style='font-size:2em'>⚙️</button> -->

{{py('exo1')}}

{{REPL()}}
{{REPL('exo1')}}


<!--
<div class="wrapper">
<div class="interior_wrapper">
<div id="editor_2"></div>
</div>
<div id="term_editor_2" class="term_editor"></div>
</div>
<button onclick='interpretACE("editor_2")'>⚙️</button> -->

<!-- {{REPL}} -->

{{terminal()}}

{{terminal2(7)}}

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

$$\int_0^t x^2 dx$$

