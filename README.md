Pierre BRUOT et Maxime BLANCHON
# Théorie des graphes 
## Implantation d'algorithmes en Python

### Conversion liste d'adjacence - matrice d'adjacence

Le but de cet algorithme est d'obtenir la matrice d'adjacence correpsondant au graphe donné en entrée sous forme de liste d'adjacence. Cet algorithme est utilisé dans la version 1 de Roy-Warshall qui utilise une matrice d'adjacence. 

#### Pseudo-code

```
Fonction listeAdjToMatriceAdj (listeAdj)
  
  nbSommets = taille(listeAdj)
  
  Pour i allant de 0 à nbSommets
    nbSuccesseurs = taille(listeAdj[i])
  
    Pour j allant de 0 à nbSuccesseurs
      matriceAdj[i][listeAdj[i][j] = 1
      
    Fin Pour 
  Fin Pour
  
  Retourner matriceAdj

Fin listeAdjToMatriceAdj
```

#### Roy-Warshall

L'algorithme de Roy-Warshall 1 prend en argument une liste d'adjacence qui doit être convertie en matrice d'adjacence.
L'algorithme de Roy-Warshall 2 prend en argument une liste d'adjacence san.

```
Fonction royWarshall (listeAdj)
  
  matriceAdj = listeAdjToMatriceAdj(listeAdj)
  nbSommets = taille(listeAdj)
  
  Pour k allant de 0 à nbSommets
    Pour i allant de 0 à nbSommets
      Pour j allant de 0 à nbSommets
        matriceAdj[i][j] = matriceAdj[i][j] ou (matriceAdj[i][k] et matriceAdj[k][j])
      Fin Pour
    Fin Pour
  Fin Pour

  Retourner matriceAdj
 
Fin royWarshall


Fonction royWarshall2 (listeAdj)

  nbSommets = taille(listeAdj)
  
  Pour i allant de 0 à nbSommets
    Pour j allant de 0 à nbSommets
      Si i est dans listeAdj[j] alors
        Ajouter à listeAdj[j] le contenu de listeAdj[i]
        Enlever les doublons de listeAdj[j]
      Fin Si
    Fin Pour
   Fin Pour
   
   Retourner listeAdj
   
Fin royWarshall2
```

#### Parcours en profondeur

```
Fonction démarrerParcoursEnProfondeur (listeAdj)

  Fonction parcoursEnProfondeur (listeAdj, sommetActuel, sommetsVisités, ordreDeVisite)
  
    nbSuccesseurs = taille(listeAdj[sommetActuel])
    sommetsVisités[i] = Vrai
    Ajouter sommetActuel à ordreDeVisite 

    Pour i allant de 0 à nbSuccesseurs
      Si sommetsVisités[listeAdj[sommetActuel][i] est Faux alors
        parcoursEnProfondeur(listeAdj, i, sommetsVisités, ordreDeVisite) 
      Fin Si
    Fin Pour
  
  Fin parcoursEnProfondeur

  nbSommets = taille(listeAdj)
  sommetsVisités[0..nbSommets] initialisé à Faux
  ordreDeVisite (liste)

  Pour i allant de 0 à nbSommets
    Si sommetsVisités[i] est Faux alors
      parcoursEnProfondeur(listeAdj, i, sommetsVisités, ordreDeVisite)
    Fin Si
  Fin Pour

  Retourner ordreDeVisite
  
Fin démarrerParcoursEnProfondeur
```

#### Composantes fortement connexes

```
TODO
```

### Jeux d'essais

Nous avons testé tous les algorithmes ci-dessus avec les graphes suivants (représentés sous forme de liste d'adjacence).
Sur 1000 exécutions, l'algorithme Roy-Warshall 2 est en moyenne 2,7 fois plus rapide que l'algorithme Roy-Warshall 2.

```python
   data_set = [[[], [], [], [], []],

                [[1, 2], [2], [3], [4], []],

                [[3], [2], [], [4], [0]],

                [[1], [2], [0], [2], [3]],

                [[1], [], [1], [0, 2, 6, 4], [5], [3], []],

                [[0, 2, 3, 4], [1, 2, 4], [0, 2, 3, 4], [1, 2, 3, 4], [0, 2, 4]],

                [[1], [2], [0], [1, 2, 5], [2, 6], [3, 4], [4], [5, 6, 7]],

                [[4, 6, 8, 9], [1, 2, 7, 9], [0, 2, 9], [1, 4, 5, 6, 8, 9], [1, 8, 9], [3, 4, 6, 9], [2, 3, 5, 6, 8, 9],
                 [3, 4, 5, 6, 8, 9], [0, 1, 3, 6, 8, 9], [0, 1, 2, 5, 7, 9]],

                [[0, 1, 2, 6, 7, 9], [1, 8, 9], [1, 3, 5, 8, 9], [0, 2, 3, 4, 6, 9], [1, 3, 4, 7, 9], [1, 4, 9],
                 [4, 6, 7, 9], [1, 2, 5, 9], [0, 3, 5, 6, 9], [2, 5, 9]],

                [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
                ]


```
