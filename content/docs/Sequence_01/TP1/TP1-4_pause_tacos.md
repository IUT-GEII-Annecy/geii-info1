---
title: TP 1 - La pause Tacos
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 140
---

# La pause Tacos
## Niveau 1

> [!note]  
> **Cahier des charges : Pause Tacos - Niveau 1**  
> Votre programme tient un Tacos dont vous devez inventer le nom. 
> Il reçoit un client, qui lui commande un certain nombre de tacos et de kebab et votre programme lui dit annonce alors le montant total de la commande 
> {{< checkbox checked="false" >}}Le programme Affiche d'abord une phrase de bienvenue {{< /checkbox >}}
> ```bash
> Bonjour, bienvenu chez <nom_du_tacos>
> ```
> {{< checkbox checked="false" >}}Le programme demande alors le nombre de Tacos, puis le nombre de Kebab voulu {{< /checkbox >}}
> {{< checkbox checked="false" >}}Le programme écrit alors le prix total de la commande, arrondi au centième. {{< /checkbox >}}
> {{< checkbox checked="false" >}}Le programme écrit ensuite le message de remerciement {{< /checkbox >}}
> ```
> Montant total : <montant_total> euros
> Merci pour votre commande chez <nom_du_tacos>
> ```
>
> |Produit|Prix|
> |---|---|
> |Tacos|6,30 €|
> |Kebab|5,50 €|
>---
>**Checks:**
> ```
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp1/3_tacos/niveau1
> ```


> [!exemple]  
> **Exemple de sortie pour cet exercice**  
> [{{< asciicast "https://asciinema.org/a/hD1h6Kxu9xtn1pfwgW2e7oetj.js" "hD1h6Kxu9xtn1pfwgW2e7oetj">}}](https://asciinema.org/a/hD1h6Kxu9xtn1pfwgW2e7oetj)

> [!info]  
> **Fiche méthode**  
> Pour ce programme, comme pour beaucoup, posez-vous ces questions, dans l'ordre. 
> 1. "Si j'étais à la place du programme, comment je ferai ?"
>   - Vous pourrez en déduire les étapes de l'algorithme
> 2. "Si j'étais vraiment très mauvais en mémorisation, qu'est-ce que je devrais écrire ?" 
>   - Vous pourrez en déduire les variables du programme
> 	{{< checkbox checked="false" >}}Lesquelles sont des entiers `int` ? {{< /checkbox >}}
> 	{{< checkbox checked="false" >}}Lesquelles sont des nombres à virgule `float` ? {{< /checkbox >}}
> 	{{< checkbox checked="false" >}}Autres ? {{< /checkbox >}}
> 3. "Y a-t-il des 'cas bizarre' ?"

## Niveau 2 
Même chose avec gestion des stocks

> [!note]  
> **Cahier des charges : Pause Tacos - Niveau 2 - Gestion des stocks**  
> {{< checkbox checked="false" >}}Même cahier des charges que le niveau 1 auquel s'ajoute :{{< /checkbox >}}
> {{< checkbox checked="false" >}}Le restaurant a un stock limité. {{< /checkbox >}}
> 	{{< checkbox checked="false" >}}Après avoir demandé le nombre de tacos et de kebab :{{< /checkbox >}}
> 		{{< checkbox checked="false" >}}Si le client demande unnombre négatif de l'un, l'autre ou les deux : {{< /checkbox >}}
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
> 
> ---
> ```
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp1/3_tacos/niveau2
> ```

## Bonus : Niveau 3

> [!note]  
> **Cahier des charges : Pause Tacos - Niveau 3 - Réduction**  
> {{< checkbox checked="false" >}}Même cahier des charges que précédemment {{< /checkbox >}}
> {{< checkbox checked="false" >}}Si le client commande plus de 5 articles au total, une réduction de 10% est appliquée sur le montant total de la commande {{< /checkbox >}}
> {{< checkbox checked="false" >}}Les sorties attendues sont identiques aux cahiers des charges précédents{{< /checkbox >}}
> ---
> ```
> check50 IUT-GEII-Annecy/exercices/2025/info1/tp1/3_tacos/niveau3
> ```
