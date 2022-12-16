# Bonus : QCM et multi QCM

## Des QCM en MkDocs

Quelle est la réponse à la question universelle (deux réponses possibles) ?

{{ qcm(
    ["$6\\times 7$", "Ça : $\\int_0^{42} 1 \\textrm{d} x$", "`#!python sum([i for i in range(10)])`", "La réponse D"], [1,2], shuffle = True
    ) 
}}

!!! warning "Syntaxe"
    
    === "Utilisation"

        ```markdown 
        {% raw %}
        {{ qcm(["$6\\times 7$", "$\\int_0^{42} 1 dx$", "`#!python sum([i for i in range(10)])`", "La réponse D"], [1,2], shuffle = True) }}
        {% endraw %}
        ```
        
        - Argument 1: Tableau de strings contenant vos réponses.

        - Argument 2: Entier ou tableau d'entiers indiquant les bonnes réponses. L'indexation naturelle (1 à N) est choisie.

        - Argument 3: True pour une génération aléatoire à chaque rechargement du site web. False sinon. 
    
    === "Limitations"

        - Toute instruction Latex nécessitant un backslash `\` doit être échappé avec un second backslash `\`.
        
        - Les codes (e.g. instructions Python) doivent tenir sur une ligne.
        
        - La génération aléatoire n'est faite qu'une seule fois (à la génération du site statique).


## Installation

!!! help "Prérequis" 
    
    - Plugin macro
    - MathJax 3.0
    - Pyodide-MkDocs

    === "mkdocs.yml"

        Ajouter le lien vers le fichier de css du QCM :

        ```yml
            extra_css:
                ....
                - my_theme_customizations/qcm/qcm.css
                ....
        ```
    
    === "my_theme_customizations/main.html"

        Dans la partie de chargement des libraires (`md{%raw%}{% block libs %}{%endraw%}`), ajouter :
        
        ```html
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/styles/atom-one-light.min.css">
            <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.5.0/highlight.min.js"></script>  
        ```

    === "my_theme_customizations/js/ide.js"

        À la fin du fichier, ajouter :

        ```javascript
            document.addEventListener('DOMContentLoaded', () => {
                document.querySelectorAll('pre code.qcm').forEach((el) => {
                hljs.highlightElement(el);
                });
            });
            
            document.querySelectorAll("[id^=qcm_]").forEach((el) => {
                let qcmAns = el.childNodes;
                if (el.dataset.shuffle == 1) {
                for (let i = qcmAns.length - 1; i >= 0; i--) el.appendChild(qcmAns[Math.floor(Math.random() * i)])
                }
                
                for (let element of el.children) {
                element.addEventListener('click', () => {
                    element.firstChild.disabled = true
                    element.firstChild.checked = true
                })
                }
            });
        ```

    === "docs/xtra/stylesheets/qcm.css"

        Télécharger le fichier appelé [`qcm.css`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/docs/xtra/stylesheets/qcm.css "Des supers styles pour QCM").

    === "main.py"

        À la suite de votre configuration existante et au sein de la fonction `define_env`, ajouter le contenu du fichier [`main_QCM.py`](https://gitlab.com/bouillotvincent/pyodide-mkdocs/-/raw/main/docs/scripts/main_qcm.py "Faire des QCM").
    
    === "MathJax"

        Pour rappel, votre fichier de configuration `docs/xtra/javascripts/mathjax-config.js` doit ressembler à cela :

        ```js
        window.MathJax = {
        startup: {
            ready: () => {
                console.log('MathJax is loaded, but not yet initialized');
                MathJax.startup.defaultReady();
                console.log('MathJax is initialized, and the initial typeset is queued');
            }
        },
        tex: {
            inlineMath: [["\\(", "\\)"]],
            displayMath: [["\\[", "\\]"]],
            processEscapes: true,
            processEnvironments: true
        },
        options: {
            ignoreHtmlClass: ".*|",
            processHtmlClass: "arithmatex"
        }
        };

        document$.subscribe(() => {
        MathJax.typesetPromise()
        })
        ```

## Multi QCM

!!! warning "test"

    {{multi_qcm("exemple.csv")}}

{{multi_qcm(
  ["1+1=?", ["$6\\times 7$", "Ça : $\\int_0^{42} 1 \\textrm{d} x$", "`#!python sum([i for i in range(10)])`", "La réponse D", '42'], [1,2, 5]],
  ["1+1=?", ["$12$", "2", "Je sais pas", "L'age du capitaine"], [2]],
  ["$x - {n} = {p}$", ["$x = {n} + {p}$", "$x = {n} - {p}$", "$x = {p}$", "$x = {n} / {p}$"], [1], {'p' : [1, 3, 7], 'n' : [4, 2, 1]} ],  
  ["Résoudre l'équation $x - {n} = {p}$ pour $x>{p}$.", ["$x = |{n} + {p}|$", "$x = |{n} - {p}|$", "$x = |{p}|$", "$x = \\dfrac{{n}}{{p}}$"], [1], {'p' : [1, 3, 7], 'n' : [4, 2, 1]} ]
)}}
