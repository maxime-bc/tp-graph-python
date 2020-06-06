Pierre BRUOT et Maxime BLANCHON
# Théorie des graphes 
## TP3 : Coloration de graphes

### Coloration des sommets

...

#### Pseudo-code

```
Fonction WelshPowell1 (listeAdj)

    couleur = 1
    nbSommets := taille(listeAdj)
    couleurSommets := Tableau de taille(nbSommets) initialisé à 0
    degréSommets := Liste de taille(nbSommets), composé de sous-listes contenant l'index du sommet et son degré,
                    triées de façon décroissante en fonction du degré.

    Pour i allant de 0 à nbSommet
        Pour j allant de 0 à nbSommet
            Si le sommet degréSommets[j][0] n'a pas été colorié et que les voisins du sommet degréSommets[j][0] n'ont pas été coloriés avec `couleur`
                couleurSommets[degréSommets[j][0]] = couleur
            Fin Si
        Fin Pour
        couleur += 1
    Fin Pour

    Retourner couleurSommets
Fin WelshPowell


Fonction WelshPowell2 (listeAdj)

    couleur = 1
    nbSommets := taille(listeAdj)
    couleurSommets := Tableau de taille(nbSommets) initialisé à 0

    Pour i allant de 0 à nbSommet
        Pour j allant de 0 à nbSommet
            Si le sommet j n'a pas été colorié et que les voisins du sommet j n'ont pas été coloriés avec `couleur`
                couleurSommets[j] = couleur
            Fin Si
        Fin Pour
        couleur += 1
    Fin Pour

    Retourner couleurSommets
Fin WelshPowell
```

### Graphe des arrêtes

...

#### Pseudo-code

```
Fonction CréationLineGraph (listeAdj)
    
    nbSommets := taille(listeAdj)
    listeDesArêtes := Liste initialisée à vide

    Pour i allant de 0 à nbSommets
        Pour j allant de 0 à nbSommets
            Si l'arête joignant le sommet i au sommet listeAdj[i][j] n'est pas dans listeDesArêtes
                Ajouter la liste [i, listeAdj[i][j]] dans listeDesArêtes 
            Fin Si
        Fin Pour
    Fin Pour

    listeAdjLineGraph := initialisé avec taille(listeDesArêtes) sous-listes vides

    Pour i allant de 0 à taille(listeDesArêtes)
        Pour j allant de 0 à taille(listeDesArêtes)
            Si listeDesArêtes[i] != listeDesArêtes[j] alors
                Si l'un des deux sommets liés par listeDesArêtes[i] est dans listeDesArêtes[j] alors
                     On ajoute j dans listeAdjLineGraph[i]
                Fin Si
        Fin Pour
    Fin Pour

    Retourner listeAdjLineGraph
Fin créationLineGraph
```

### Coloration des arêtes d’un graphe

...

#### Pseudo-code

```
Fonction colorationArêtesGraph (listeAdj)
    Retourner WelshPowell2(CréationLineGraph(listeAdj))
Fin colorationArêtesGraph
```