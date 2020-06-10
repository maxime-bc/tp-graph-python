Pierre BRUOT et Maxime BLANCHON
# Théorie des graphes 
## TP3 : Coloration de graphes

### Coloration des sommets

L'algorithme de Welsh Powell est un algorithme de coloration de sommets. C'est un algorithme heuristique, c'est à dire qu'il ne permet pas de colorier les sommets d'un graph de façon optimale.

Cet algorithme prend en paramètre une liste d’adjacence et renvoie une liste contenant la couleur du sommet à l'index i, représentée par un entier.

Avec WelshPowell1, les sommets sont triés selon leur degré avant d'être parcourus pour leur appliquer une couleur tandis qu'avec WelshPowell2 ils sont parcourus selon leur ordre dans la liste d'adjacence.

![graph1](../figures/graph1.png?raw=true)

Pour obtenir la coloration maximale des sommets sur le graph ci-dessus avec l'algorithme de Welsh Powell,
il suffit de renommer les sommets comme montré ci-dessous :

![graph2](../figures/graph2.png?raw=true)

La coloration optimale de ce graph comporte deux couleurs.

---

![graph3](../figures/graph3.png?raw=true)

Pour obtenir la coloration maximale des sommets sur le graph ci-dessus avec l'algorithme de Welsh Powell,
il suffit de renommer les sommets comme montré ci-dessous :

![graph4](../figures/graph4.png?raw=true)

La coloration optimale de ce graph comporte deux couleurs.

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

### Graphe des arêtes

Soit G un graph.
Soit A(G) le graphe des arêtes de G.

Chaque sommet de A(G) représente une arête de G et deux sommets de A(G) sont adjacents si et seulement si les arêtes de G correspondantes sont adjacentes.

CréationGrapheArêtes prend en argument la liste d'adjacence représentant le graphe G et renvoie une liste d'adjacence représentant le graphe des arêtes de G, A(G).

#### Pseudo-code

```
Fonction CréationGrapheArêtes (listeAdj)
    
    nbSommets := taille(listeAdj)
    listeDesArêtes := Liste initialisée à vide

    Pour i allant de 0 à nbSommets
        Pour j allant de 0 à nbSommets
            Si l'arête joignant le sommet i au sommet listeAdj[i][j] n'est pas dans listeDesArêtes
                Ajouter la liste [i, listeAdj[i][j]] dans listeDesArêtes 
            Fin Si
        Fin Pour
    Fin Pour

    listeAdjLineGraphe := initialisé avec taille(listeDesArêtes) sous-listes vides

    Pour i allant de 0 à taille(listeDesArêtes)
        Pour j allant de 0 à taille(listeDesArêtes)
            Si listeDesArêtes[i] != listeDesArêtes[j] alors
                Si l'un des deux sommets liés par listeDesArêtes[i] est dans listeDesArêtes[j] alors
                     On ajoute j dans listeAdjLineGraphe[i]
                Fin Si
        Fin Pour
    Fin Pour

    Retourner listeAdjLineGraphe
Fin créationLineGraphe
```

### Coloration des arêtes d’un graphe

Cet algorithme colorie, de façon heuristique, les arêtes d’un graphe.
Pour une liste d'adjacence donnée, il génère le graph d'arêtes correspondant et le colorie avec l'algorithme de Welsh Powell.

#### Pseudo-code

```
Fonction colorationArêtesGraphe (listeAdj)
    Retourner WelshPowell2(CréationGrapheArêtes(listeAdj))
Fin colorationArêtesGraphe
```
