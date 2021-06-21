# Guide du REPL

!!! info "paf"

    === "test"
        Blablabla
        
        {{REPL('exo2')}}
        
    === "Corrigé"
        {{REPL('exo2')}}

    === "Truc"
        {{REPL('exo2')}}

!!! info "pif"

    === "test2"
        {{REPL('exo2')}}
    
    === "Corrigé2"
        {{REPL('exo2')}}

    === "Truc2"
        {{REPL('exo2')}}

    

??? info "pouf"

    === "test3"
        {{REPL('exo2')}}
    
    === "Corrigé3"
        {{REPL('exo2')}}

    === "Truc3"
        {{REPL('exo2')}}

    ??? "Solution3"

        bidule à lire

<div class="admonition warning">
<p class="admonition-title" style="::before">paf</p>
<div class="tabbed-set" data-tabs="1:1">
<input checked="checked" id="__tabbed_4_1" name="__tabbed_4" type="radio"></input>
<label for="__tabbed_4_1">test</label>
<div class="tabbed-content"><p></p>blabla<p></p></div>

<input id="__tabbed_4_2" name="__tabbed_4" type="radio"></input>
<label for="__tabbed_4_2">test2</label>
<div class="tabbed-content"><p></p>blabla2<p></p></div>

<input id="__tabbed_4_31" name="__tabbed_4" type="radio"></input>
<label for="__tabbed_4_31">test3</label>
<div class="tabbed-content"><p></p>blabla3<p></p></div>
</div>
</div>


## Aperçu

Un REPL se présente sous cette forme :

??? info "Déroulez-moi !"

    {{REPL('exo2')}}

Il dispose de quatre boutons : 

- Lancer le script : <button class="emoji">▶️</button> 
- Télécharger le script : <button class="emoji">⤵️</button>
- Téléverser un script : <button class="emoji">⤴️</button>
- Valider le script avec des tests unitaires : <button class="emoji_dark">🛂</button>

!!! info "Rappel"

    Tout se fait du côté client. **Rien n'est envoyé au serveur**.

## Prise en main

Par défaut, la commande `#!markdown {% raw %}{{REPL('exo2')}}{% endraw %}` permet de charger un script placé dans `docs/scripts/`. 

Pour une organisation en chapitre, utilisez un chemin relatif. Par exemple : `#!markdown {% raw %}{{REPL('c1/exo2')}}{% endraw %}` chargera le script exo2.py depuis `docs/scripts/c1`.

!!! warning "Important"

    Le bouton de validation du script à l'aide de tests unitaires est présent uniquement si vous fournissez un fichier `test_nom_du_fichier.py` présent dans le même répertoire que `nom_du_fichier.py`.

    Le lancement du script, le téléchargement et le téléversement sont présentes par défaut.

    Pour l'instant, aucun fichier de correction n'est fourni.

## Plein d'exercices !

!!! info "Exercice 1"

    Écrire une fonction qui découpe une phrase en mots.

    {{REPL('exo_demo_1')}}


<!-- ??? info "Patience, patience"

    Le guide du REPL arrive bientôt.
 -->
