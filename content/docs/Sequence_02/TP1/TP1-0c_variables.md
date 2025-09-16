---
title: TP 1 - Premières variables
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 103
---
# Notre première variable 
Nous allons à présent utiliser nos premières variables. Pour cela, commençons simplement avec l'exemple du cours et le cahier des charges suivant : 
> [!note]  
> **Cahier des charges : Afficher le nom de l'utilisateur**  
> - Le programme doit demander le nom de l'utilisateur avec le message de votre choix.
> - Le programme doit afficher "Hello, \<nom\>" où \<nom\> est le nom entré par l'utilisateur.
>
> **Sortie attendue :**
> | Entrée | Affichage attendue | 
> | --- | --- |
> | <nom> | Hello, <nom>|  
>
> **Exemples de tests :**  
> | Entrée | Affichage attendue | 
> | --- | --- |
> | Alice | Hello, Alice |  
>
> ---
> Pour lancer les tests : 
>   ```bash
> 	check50 iut-geii-annecy/exercices/2025/info1/tp1/0_hello/variable
> 	```

Le cahier des charges mentionne la sortie attendue. **Votre programme doit ABSOLUMENT afficher la sortie attendue pour être correct.**

> [!note]  
> **À faire : Afficher le nom de l'utilisateur**  
> 
> Pour répondre à ce cahier des charges, vous devez réaliser les 4 prochaines étapes. A vous de trouver où effectuer chacune des modifications. 
>
> {{< checkbox checked="false" >}}Inclure la bibliothèque `cs50.h` pour utiliser la fonction `get_string`. {{< /checkbox >}}
> 	```c
> 	#include <cs50.h>
> 	```
> {{< checkbox checked="false" >}}Déclarer une variable de type `string` pour stocker le nom de l'utilisateur.  {{< /checkbox >}}
> 	```c
> 	string nom;
> 	```
> {{< checkbox checked="false" >}}Utiliser `get_string` pour obtenir le nom de l'utilisateur.  {{< /checkbox >}}
> 	```c
> 	nom = get_string("Entrez votre nom : ");
> 	```
> {{< checkbox checked="false" >}}Modifier `printf` pour afficher le message "Hello , [nom]!" où [nom] est le nom entré par l'utilisateur.{{< /checkbox >}}


> [!note]  
> **À faire : Vérification**  
> A l'aide de la fiche "Aide Mémoire" : 
> {{< checkbox checked="false" >}}Vérifier la mise en page de votre code (`style50`){{< /checkbox >}}
> {{< checkbox checked="false" >}}Faire passer les tests automatiques (`check50`){{< /checkbox >}}





