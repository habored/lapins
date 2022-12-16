# Guide du Terminal

## Exemple

{{ terminal() }}

## Utilisation

Entrez simplement sur une ligne : 

```markdown
{% raw %}
{{ terminal() }}
{% endraw %}
```

## Technique

Techniquement, le terminal est obtenu en utilisant le plugin [Terminal](https://terminal.jcubic.pl "plugin Jquery") de jQuery[^ip]. 

[^ip]: C'est pour cela qu'on ne peut pas se passer de jQuery actuellement. 

On crée un `#!html <div>` qui possède un identificateur numéro (entier commençant à 1 et auto-incrémenté). Ce `#!html <div>` est ensuite colorié à l'aide du plugin Terminal. 

??? warning "Technique"

    Un problème provient du focus du terminal. Par défaut, le dernier terminal créé aura le focus, ce qui souvent nous emmène en bas de page...  

    La solution a été de créer deux `#!html <div>`: 
        
    - Le premier `#!html <div>` est un simple bloc de texte mimant un Terminal. Il est appelé [fake_id](https://www.youtube-nocookie.com/embed/uwNIMM4qnrI?autoplay=1&iv_load_policy=3&loop=1&modestbranding=1&playlist=uwNIMM4qnrI "Fake ID").
    - Le second `#!html <div>` contient effectivement le Terminal. Il ne se créera que si l'événement onclick du `#!html <div id = fake_id>` est déclenché.