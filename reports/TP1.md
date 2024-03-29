Pierre BRUOT et Maxime BLANCHON
# Théorie des graphes 
## TP1 : Implantation d'algorithmes en Python

### Conversion liste d'adjacence - matrice d'adjacence

Le but de cet algorithme est d'obtenir la matrice d'adjacence correspondant au graphe donné en entrée sous forme de liste d'adjacence. Cet algorithme est utilisé dans la version 1 de Roy-Warshall qui utilise une matrice d'adjacence. 

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

### Roy-Warshall

L'algorithme royWarshall1 prend en argument une liste d'adjacence qui doit être convertie en matrice d'adjacence.
L'algorithme royWarshall1Bis est une implémentation différente de royWarshall1.

L'algorithme royWarshall2 prend en argument une liste d'adjacence sans passer par une matrice d'adjacence.

Cet algorithme permet de déterminer la fermeture transitive d'un graphe, où chaque sommet est relié à tous les autres sommets du graphe.

#### Pseudo-code
```
Fonction royWarshall1 (listeAdj)
  
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
 
Fin royWarshall1


Fonction royWarshall1Bis (listeAdj)

  matriceAdj = listeAdjToMatriceAdj(listeAdj)
  nbSommets = taille(listeAdj)
    
  Pour i allant de 0 à nbSommets
    Pour j allant de 0 à nbSommets
      Si matriceAdj[i][j] = 1 alors
        Pour k allant de 0 à nbSommets
          Si matriceAdj[j][k] = 1 alors
            matriceAdj[i][k] = matriceAdj[j][k]
          Fin Si
        Fin Pour
      Fin Si
    Fin Pour
  Fin Pour

  Retourner matriceAdj
 
Fin royWarshall1Bis


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

### Parcours en profondeur et composantes fortement connexes

Cet algorithme retourne une liste des sommets dans l'ordre de leur visite lors du parcours en profondeur du graphe ainsi que ses composantes fortement connexes en utilisant l'algorithme de Tarjan.

#### Pseudo-code
```
Fonction démarrerParcoursEnProfondeur(listeAdj)

    num := 0
    pileSommetsVisités := Pile vide
    tableauSommetsVisités = Tableau de taille(listeAdj) initialisé à Faux
    listeComposantesFortementConnexes := Ensemble vide
    indexGlobal = 0
    index = Tableau vide
    sommetsAccessibles = Tableau vide

    Fonction ParcoursEnProfondeur(sommetActuel)

        Si tableauSommetsVisités[sommetActuel] est Vrai
            Retourner Vide
        Fin Si

        tableauSommetsVisités[sommetActuel] est Vrai
        Ajouter sommetActuel à pileSommetsVisités 

        index[sommetActuel] := indexGlobal
        numAccessible[sommetActuel] := indexGlobal
        indexGlobal++

        Pour chaque successeur de sommetActuel
            Si successeur n'est pas défini
                ParcoursEnProfondeur(successeur)
                numAccessible[sommetActuel] = min(numAccessible[sommetActuel], numAccessible[successeur])
            Sinon si successeur est dans pileSommetsVisités
                numAccessible[sommetActuel] = min(numAccessible[sommetActuel], index[successeur])
            Fin Si

            Si numAccessible[sommetActuel] = index[sommetActuel]

                composanteFortementConnexe := Ensemble vide
                dépiler pileSommetsVisités dans successeur 

                Tant que successeur est différent de sommetActuel
                    ajouter successeur à composanteFortementConnexe
                    dépiler pileSommetsVisités dans successeur

                Ajouter sommetActuel dans composanteFortementConnexe
                Ajouter composanteFortementConnexe à listeComposantesFortementConnexes

            Fin Si

        Fin Pour

    Fin ParcoursEnProfondeur

    Pour chaque sommet de listeAdj
        Si sommet n'est pas dans pileSommetsVisités
            ParcoursEnProfondeur(sommet)
        Fin Si
    Fin Pour

    Renvoyer pileSommetsVisités et listeComposantesFortementConnexes

Fin démarrerParcoursEnProfondeur
```

### Jeux d'essais

Afin de comparer la performance des différentes implémentations de Roy-Warshall, nous avons écrit une fonction qui génère des graphes aléatoirement.

```
Fonction génèreGraphe (nbSommets)

  graphe := liste contenant nbSommets sous-listes vides
  
  Pour i allant de 0 à nbSommets-1
    nbSuccesseurs := nombre aléatoire supérieur ou égal à 0 et inférieur ou égal à nbSommets
    On ajoute un nombre aléatoire de successeurs compris entre 0 à nbSommets dans graphe[i]
  Fin Pour
  
  Retourner graphe
  
Fin génèreGraphe
```

Cette fonction permet de tester les performances en exécutant n fois chaque algorithme avec des graphes aléatoires dont la taille augmente progressivement de a à b, b compris.

Exemple ci-dessous, avec n = 1000, a = 1 et b = 100

![Figure1](../figures/figure1.png?raw=true)

On peut voir sur le diagramme ci-dessous que l'algorithme le plus efficace est Roy-Warshall 2 (environ 2 fois plus efficace que Roy-Warshall 1).
On remarque également que Roy-Warshall 1 Bis est l'implémentation la moins efficace.

Cependant, si on zoome dans le diagramme, on peut voir que Roy-Warshall 1 bis est très légèrement plus efficace que Roy-Warshall 1 pour des graphes avec des sommets allant de 1 à 7/8.

![Figure2](../figures/figure2.png?raw=true)

Le diagramme peut être visualisé en exécutant les commandes suivantes dans un terminal à l'intérieur du dossier racine (sur Linux) :

```bash
python3 -m venv venv # création d'un environnement virtuel pour installer la bibliothèque matplotlib
source venv/bin/activate # activation de l'environnement virtuel
pip3 install matplotlib # installation de la bibliothèque Python matplotlib
python3 -m src.tp1 1 100 1000 # exécution du script Python, 1 = sommet de départ, 100 = sommet d'arrivée, 1000 = nombre d'exécutions des algos
```

Le script prend en paramètres le nombre de sommets de départ, le nombre de sommets d'arrivée et le nombre d'exécution des algorithmes à chaque fois que le nombre de sommets augmente.
