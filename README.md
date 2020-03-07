# Théorie des graphes 
## Implantation d'algorithmes en Python

### Pseudo-code

#### Conversion liste d'adjacence - matrice d'adjacence

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
```

#### royWarshall2 

```
Fonction royWarshall2 (listeAdj)

  nbSommets = taille(listeAdj)
  
  Pour i allant de 0 à nbSommets
    Pour j allant de 0 à nbSommets
      Si i est dans listeAdj[j] alors
        Ajouter à listeAdj[j] le contenu de listeAdj[i]
        Enlever les doublons de listeAdj[j]
      Fin Si
    
    Enlever les doublons de listeAdj[i]
    Fin Pour
   Fin Pour
   
   Retourner listeAdj
   
Fin royWarshall2
```

#### Parcours en profondeur

```
Fonction démarrerParcoursEnProfondeur (listeAdj)

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
```

#### Composantes fortement connexes

```
TODO
```
