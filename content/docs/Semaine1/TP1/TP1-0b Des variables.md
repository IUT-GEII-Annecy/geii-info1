---
title: TP 1 - Variables
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 101
---
### Notre première variable 
Nous allons à présent utiliser nos premières variables. Pour cela, commençons simplement avec l'exemple du cours et le cahier des charges suivant : 
> [!attention]  
> **Cahier des charges  -- `iut-geii-annecy/exercices/2025/x/me`**  
> - Le programme doit demander le nom de l'utilisateur avec le message de votre choix.
> - Le programme doit afficher "Hello, \<nom\>" où \<nom\> est le nom entré par l'utilisateur.
> 
> ** Entrée : **  
> \<nom\> : Le nom de l'utilisateur
> 
> ** Sortie attendue : **
> ```bash
> Hello, <nom>
> ```
>
> **Exemples de tests :**
> **Entrée :** Alice        
> **Sortie attendue :** `Hello, Alice`

Le cahier des charges mentionne la sortie attendue. **Votre programme doit ABSOLUMENT afficher la sortie attendue pour être correct.**

> [!note]  
> **À faire : Modifier le programme pour demander le nom de l'utilisateur et l'afficher.**  
> 1. Inclure la bibliothèque `cs50.h` pour utiliser la fonction `get_string`. 
> 	```c
> 	#include <cs50.h>
> 	```
> 2. Déclarer une variable de type `string` pour stocker le nom de l'utilisateur.  
> 	```c
> 	string nom;
> 	```
> 3. Utiliser `get_string` pour obtenir le nom de l'utilisateur.  
> 	```c
> 	nom = get_string("Entrez votre nom : ");
> 	```
> 4. Modifier `printf` pour afficher le message "Hello , [nom]!" où [nom] est le nom entré par l'utilisateur.




> [!note]  
> **À faire : Vérifier, puis soumettre votre travail sur cs50**  
> {{< checkbox checked="false" >}}Vérifier que votre code passe *style50* :{{< /checkbox >}}
>   {{< checkbox checked="false" >}}En haut à droite de vsCode, cliquer sur *style50*.    {{< /checkbox >}}
>   {{< checkbox checked="false" >}}Vous pouvez alors appliquer les changements suggérés.{{< /checkbox >}}
> {{< checkbox checked="false" >}}Vérifier que votre programme répond au cahier des charges : {{< /checkbox >}}
>  {{< checkbox checked="false" >}}Vérifer le programme avec `check50` : {{< /checkbox >}}
> 	```bash
> 	check50 iut-geii-annecy/exercices/2025/info1/tp1/0_hello/variable
> 	```
>   {{< checkbox checked="false" >}}Si des erreurs sont détectées, corrigez-les et vérifiez à nouveau.{{< /checkbox >}}
> {{< checkbox checked="false" >}}Soumettre votre travail sur cs50 :{{< /checkbox >}}
>   {{< checkbox checked="false" >}}Exécuter la ligne suivante{{< /checkbox >}}
> 	  ```bash
> 	  submit50 iut-geii-annecy/exercices/2025/info1/tp1/0_hello/variable
> 	  ``` 
>   {{< checkbox checked="false" >}}Suivez les instructions à l'écran pour finaliser la soumission.{{< /checkbox >}}


> [!success]  
> **Félicitations !**  
> Vous venez de soumettre votre premier exercice en C. Vous avez appris à utiliser le terminal, à écrire un programme simple en C, à compiler et exécuter ce programme, et à soumettre votre travail sur cs50.

