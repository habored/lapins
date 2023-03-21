# Options avancées

## Version

Pour connaitre la version de Pyodide-MkDocs que vous utilisez. Utiliser simplement le terminal ou le terminal associé à un IDE :

- `version()`.

Si cette commande n'existe pas, votre version est antérieure à la 0.9.1 et vous loupez de nombreuses fonctionnalités !

## Pyodide et récursion

Les fonctions récursives peuvent prendre significativement plus de temps pour terminer. 

En raison de la taille limitée de la pile d'exécution sur le navigateur, la limite de récursion maximale est fixée à 200 appels.

Pour des raisons de performance, la profondeur de récursion au démarrage est fixée à 100.

Il est possible de changer cette profondeur à partir du terminal ou d'un terminal associé à un IDE :

- `setrecursionlimit(153)` fixe le nombre d'appels récursif maximal à 153

- `getrecursionlimit()` donne le nombre d'appels récursif maximal actuel

???+ warning "Module `sys`"

    Un appel au module `sys` et à `setrecursionlimit` sera inopérant.

## Palette de couleur et coloration de l'IDE

Mkdocs appelle son mode sombre `slate` et son mode jour `default`.

Par défaut, Pyodide-MkDocs utilise le thème de coloration :
- `crimson_editor` pour le mode `default` ; 
- `tomorrow_night_bright` pour le mode `slate`.

Il est possible de changer cela en ajoutant les lignes suivantes dans la partie `extra` de votre fichier `mkdocs.yml` :

```yaml
extra:
  ace_style: 
    default: crimson_editor
    slate: tomorrow_night_bright
```

Vous avez de nombreux choix de palette disponibles à cette adresse : [https://ace.c9.io/build/kitchen-sink.html].x

## Intégration à la palette de MkDocs

Il existe d'autres modes de colorations dans MkDocs. Vous pouvez par exemple imposer que le mode noir ne soit pas `slate` mais `youtube`. 

Dans ce cas, il est impératif de rajouter les lignes suivantes dans la partie `extra` du fichier `yaml` : 

```yaml
extra:
  ace_style: 
    default: crimson_editor
    slate: tomorrow_night_bright|youtube
```

Cela permettra à Pyodide-MkDocs de déterminer quel est le mode sombre et quel est le mode jour.

## Fichier de remarques

Il est possible de joindre un fichier de remarques au format markdown avec admonition, superfence voire même des IDE !

Celui-ci porte l'extension `_REM`. 

Ce fichier de remarques n'est actif que si votre exercice dispose d'un fichier de correction `_corr` et d'un fichier de test `_test` en plus du fichier d'exerice. 

Ainsi, on aura l'arborescence suivante :

  ```bash
  docs/
  ├── N1
  │   ├── 110-maximum_nombres
  │   │   ├── exo.py
  │   │   ├── exo_REM.md
  │   │   ├── exo_corr.py
  │   │   ├── exo_test.py
  │   │   └── sujet.md
  ```