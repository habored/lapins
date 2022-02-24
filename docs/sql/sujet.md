---
title: SQL
Author: Vincent-Xavier Jumel
---

# Un peu de SQL

Dans cet exercice une fonction `initialise_base_donnees` et une fonction
`execute_requete` vous sont fournies. L'exercice utilise les mots `SELECT`
`FROM` `WHERE` `JOIN` `INSERT INTO` `VALUES` et `ORDER BY`

L'étude de la fonction initialise vous donnera le schéma de la base de
données.

On demande de compléter le code proposé pour réaliser les requêtes SQL
suivantes :

1. Obtenir la salle et la marque de l'ordinateur
2. Obtenir la salle et la marque de l'ordinateur s'il y a un
   vidéo-projecteur
3. Classer par ordre croissant les ordinateurs avec une année d'entrée
   supérieure ou égale à 2017
4. Écrire une requête SQL permettant d'obtenir le nom de l'imprimante, le
   nom de la salle et de le nom de l'ordinateur connecté à cette imprimante
5. Écrire une requête SQL permettant d'insérer un nouveau vidéo-projecteur
   de marque NEC, modèle ME402X, sans TNI dans la salle 315.

!!! example "Exemples"
    ```pycon
    >>> execute_requete("SELECT COUNT(*) FROM Ordinateur")
    [(5,)]
    ```


{{ IDE('exo') }}
