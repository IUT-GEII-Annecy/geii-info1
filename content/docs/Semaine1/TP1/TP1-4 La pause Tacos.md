---
title: TP 1 - La pause Tacos
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 140
---
C'est parti pour notre premier problème ! 

## Niveau 1
> [!note]  
> **À faire : Enoncé du problème :**  
> Votre programme tient un Tacos dont vous devez inventer le nom. 
> Il reçoit un client, qui lui commande un certain nombre de tacos et de kebab. 
> Il doit alors lui dire quel est le montant total de la commande

> [!attention]  
> **Pause Tacos - Niveau 1**  
> Le programme Affiche d'abord une phrase de bienvenue 
> ```bash
> Bonjour, bienvenu chez <nom_du_tacos>
> ```
> {{< checkbox checked="false" >}}Le programme demande alors le nombre de Tacos, puis le nombre de Kebab voulu {{< /checkbox >}}
> {{< checkbox checked="false" >}}Le programme écrit alors le prix total de la commande, arrondi au centième. {{< /checkbox >}}
> 
> |Produit|Prix|
> |---|---|
> |Tacos|6,30 €|
> |Kebab|5,50 €|
> 
> {{< checkbox checked="false" >}}Le programme écrit ensuite le message de remerciement {{< /checkbox >}}
> ```
> Montant total : <montant_total> euros
> Merci pour votre commande chez <nom_du_tacos>
> ```
>---
>**Checks:**
> ```
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp1/3_tacos/niveau1
> ```


> [!exemple]  
> **Exemple de sortie pour cet exercice**  
> [![![asciicast](https://asciinema.org/a/hD1h6Kxu9xtn1pfwgW2e7oetj.svg)](/images/hD1h6Kxu9xtn1pfwgW2e7oetj.svg)](https://asciinema.org/a/hD1h6Kxu9xtn1pfwgW2e7oetj)

> [!info]  
> **Un peu d'aide ?**  
> {{< checkbox checked="false" >}}De quelles variables avez-vous besoin ? {{< /checkbox >}}
> 	{{< checkbox checked="false" >}}Lesquelles sont des entiers `int` ? {{< /checkbox >}}
> 	{{< checkbox checked="false" >}}Lesquelles sont des nombres à virgule `float` ? {{< /checkbox >}}
> 	{{< checkbox checked="false" >}}Autres ?{{< /checkbox >}}

## Niveau 2 
Même chose avec gestion des stocks

> [!attention]  
> **Pause Tacos - Niveau 2**  
> {{< checkbox checked="false" >}}Même cahier des charges que le niveau 1 auquel s'ajoute :{{< /checkbox >}}
> {{< checkbox checked="false" >}}Le restaurant a un stock limité. {{< /checkbox >}}
> 	{{< checkbox checked="false" >}}Après avoir demandé le nombre de tacos et de kebab :{{< /checkbox >}}
> 		{{< checkbox checked="false" >}}Si le client demande un nombre négatif de l'un, l'autre ou les deux : {{< /checkbox >}}
> 			{{< checkbox checked="false" >}}affiche le message {{< /checkbox >}}
> 			```bash
> 			ERREUR : Valeurs négatives interdites.
> 			```
> 			{{< checkbox checked="false" >}}Arrête le programme sans autre affichage -> `return 1;`{{< /checkbox >}}
> 		{{< checkbox checked="false" >}}Si les stocks sont insuffisant, le programme{{< /checkbox >}}
> 			{{< checkbox checked="false" >}}affiche un message selon le tableau ci-dessous{{< /checkbox >}}
> 			{{< checkbox checked="false" >}}affiche ensuite le message de remerciement du Niveau 1{{< /checkbox >}}
> 		{{< checkbox checked="false" >}}Sinon, pas de changement par rapport au niveau 1{{< /checkbox >}}
> 
> | Produit hors stock | Sortie attendue |
> |---|---|
> | Kebab | `Désolé, nous n'avons pas assez de Kebab`|
> | Tacos | `Désolé, nous n'avons pas assez de Tacos`|
> |Tacos et Kebab | `Désolé, nous n'avons pas assez de Tacos, ni de Kebab` |
> ---
> ```
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp1/3_tacos/niveau2
> ```

## Bonus : Niveau 3

> [!attention]  
> **Pause Tacos - Niveau 3**  
> {{< checkbox checked="false" >}}Même cahier des charges que précédemment {{< /checkbox >}}
> {{< checkbox checked="false" >}}Si le client commande plus de 5 articles au total, une réduction de 10% est appliquée sur le montant total de la commande {{< /checkbox >}}
> {{< checkbox checked="false" >}}Les sorties attendues sont identiques aux cahiers des charges précédents{{< /checkbox >}}
> ---
> ```
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp1/3_tacos/niveau3
> ```
