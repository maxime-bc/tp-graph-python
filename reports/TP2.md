Pierre BRUOT et Maxime BLANCHON
# Théorie des graphes 
## TP2 : Algorithmes dans les graphes sans circuits

### Mise en niveau des sommets du graphe

Cet algorithme prend en paramètre une liste d’adjacence et renvoie une liste contenant les niveaux de chaque sommet d'un graphe sans circuit.

#### Pseudo-code

```
Fonction MiseEnNiveau (listeAdj)

    nbSommets := taille(listeAdj)
    sommetsSansSuccesseurs := Tableau vide
    niveaux := Tableau de taille(nbSommets) initialisé à 0
    i := 0

    Tant que i < taille(sommetsSansSuccesseurs)
        Pour j allant de 0 à nbSommets
            Pour chaque successeur du sommet j
                
                Si le successeur est égal à sommetsSansSuccesseurs[i] alors 
                    On ajoute le successeur à sommetsSansSuccesseurs

                    Si niveaux[j] < (niveaux[sommetsSansSuccesseurs[i]] + 1) alors
                        niveaux[j] := niveaux[sommetsSansSuccesseurs[i]] + 1
                    Fin Si              
                Fin Si
            Fin Pour
        Fin Pour
        On incrémente i
    Fin Tant que

    Retourner niveaux

Fin MiseEnNiveau
```

### Création d'une liste d'association

La liste d'association est une liste de liste d'entiers qui permet d'associer un sommet à son niveau. \
 Chaque sous-liste de la liste d'association se compose de 2 entiers : \
 1 - le numéro du sommet \
 2 - son niveau 
 
La création de cette liste d'association est intermédiaire et permet par la suite d'appliquer la fonction de Grundy à chaque sommet d'un graphe.

#### Pseudo-code
```
Fonction CréationDeLaListeD'association (listeAdj) 
    
    nbSommets := taille(listeAdj)
    niveaux := MiseEnNiveau(listeAdj)
    listeD'association := liste de taille(listeAdj) initialisé avec des sous-listes vides

    Pour i allant de 0 à nbSommets
        On ajoute dans la sous-liste listeD'association i, le numéro du sommet, ainsi que niveaux[i], le niveau du sommet i

    Retourner la listeD'association triée de manière croissante en fonction du niveau de chaque sous-liste

Fin CréationDeLaListeD'association
```

### Fonction de Grundy

Cet algorithme prend en paramètre une liste d'adjacence et retourne une liste contenant le chiffre de Grundy pour chaque sommet du graphe.

#### Pseudo-code

```
Fonction Grundy (listeAdj)
    
    Fonction trouverLaValeurDeGrundy (liste, élément)
        
        valeurDeGrundy := -1
        Pour chaque sous-liste dans liste
            Si élément est égal au sommet de la sous-liste alors
                valeurDeGrundy := niveau de la sous-liste
                On sort de la boucle
            Fin Si
        Fin Pour
        
        Retourner valeurDeGrundy

    Fin trouverLaValeurDeGrundy

    listeGrundy := liste vide
    valeurDeGrundy := liste vide
    listeDesSuccesseurs := liste vide
    listeD'association := CréationDeLaListeD'association (listeAdj)

    Pour i allant de 0 à taille(listeD'association)
        Si le niveau de listeD'association[i] est égal à 0 alors
            On ajoute listeD'association[i] à listeGrundy
        Sinon
            listeDesSuccesseurs := listeAdj[sommet de listeD'association[i]]

            Pour j allant de 0 à taille(listeDesSuccesseurs)
                On ajoute trouverLaValeurDeGrundy (listeGrundy, listeDesSuccesseurs[j]) à valeurDeGrundy
            Fin Pour

            k := 0
            Tant que k est dans valeurDeGrundy
                On incrémente k
            Fin Tant que

            On ajoute la liste [sommet de listeD'association[i], k] à listeGrundy 
        Fin Si
    Fin Pour

    Retourner listeGrundy

Fin Grundy
```
