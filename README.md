# Projet - Prix de l'immobilier

## Objectif du projet
Le but de ce projet est de réaliser un programme en Python permettant de traiter et d'afficher des données stockées à partir de fichiers .txt à récupérer [ici](https://www.data.gouv.fr/en/datasets/demandes-de-valeurs-foncieres/), sans importer de module externe.

**Au sujet des chemins relatifs:** pour le bon fonctionnement du programme sans modification, les fichiers *valeursfoncieres-xxxx.txt* doivent être placés dans le même dossier que le fichier main.py. 

## Structuration du projet
Selon le sujet du projet, le programme réalisé devait pouvoir réaliser *l'affichage des ventes de maisons pour une commune et année données*, et *l'affichage des communes les plus chères*.

Conformément au cahier des charges, nous avons développé les fonctions suivantes: *mean, splitLineTable, splitLineDictionary* et *displayFunction*.

En addition à ces fonctions là, pour le bon fonctionnement du programme et pour pour augmenter la lisibilité du code, nous avons rajouté quelques fonctions non demandées par le cahier de charges:
- *sortDates*: Trie un tableau selon l'ordre chronologique du champ date mutation
- *launcher*: Gère le déroulement du programme et permet d'avoir un programme principal *main* plus compact.
- *displayTown*: Affiche les villes les plus chères au m² selon un departement et une année

Une description de chacune des fonctions présentes est disponible dans le docstring dans la déclaration de chaque fonction dans le fichier main.py.

## Explication des calculs pour "Affichage des communes les plus chères"
Afin d'afficher les communes les plus chères selon un département et une année, il est nécessaire d'effectuer certains traitements avec les données. Les valeurs que vous pourrez retrouver grâce à ce programme sont issues des traitements qui vous seront décrits ci-dessous.
- Récupération des valeurs : 
    - Les parcelles cadastrales sont rangées selon les communes auquelles elles correspondent.
    - Chaque parcelle cadastrale possède une surface bati. ainsi qu'une valeur foncière.
        - Dans l'hypothèse où la valeur foncière n'a pas de valeur, la valeur par défaut sera 0,0
        - Dans l'hypothèse où il y aurait deux surface bati. pour une parcelle cadastrale alors les surfaces seront additionnés entre elles

- Calcul du prix au m² de chaque parcelle :
    - La valeur foncière est divisée par la surface bati. pour chaque parcelle cadastrale
        - Dans l'hypothèse où la surface bati. est égale à 0 alors le calcul ne sera pas effectué

- Calcul de la moyenne du prix par m² de chaque commune :
    - On réalise la moyenne du prix au m² de chaque commune 

## Credits
Nathan RANAIVO RAVOAJA - nathan.ranaivo-ravoaja@isen-ouest.yncrea.fr

Alexandre TIGNAC - alexandre.tignac@isen-ouest.yncrea.fr