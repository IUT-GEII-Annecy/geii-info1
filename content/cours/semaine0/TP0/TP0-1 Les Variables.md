---
title: TP 0.1 Les Variables
description: Ce premier TP est une introduction à la programmation. Il utilise le langage scratch.
date: 2025-08-01
draft: false
---


# 1. Un premier pas vers la mémoire : les variables 
{{< callout type="info" title="Qu'est-ce qu'une variable ?" >}}

Une variable est un espace de stockage pour des données qui peuvent changer au cours de l'exécution du programme. Par exemple, vous pouvez utiliser une variable pour stocker le score d'un jeu ou le nom d'un utilisateur.
On peut imaginer une variable comme une boîte dans laquelle on peut mettre des informations. On peut ouvrir cette boîte pour voir ce qu'il y a à l'intérieur, ou y mettre de nouvelles informations.
Sur scratch, on affecte une valeur à une variable en utilisant le bloc "mettre [nom de la variable] à [valeur]".
{{< /callout >}}


## 1.1. Notre première variable
{{< callout type="todo" title="Comment créer une variable Scratch ?" >}}
{{< checkbox checked="false" >}}Dans la palette de blocs, trouvez la catégorie "Variables".{{< /checkbox >}}
{{< checkbox checked="false" >}}Cliquez sur "Créer une variable" et nommez-la comme vous le souhaitez.   {{< /checkbox >}}
Un bloc orange arrondi apparaît alors dans la palette de blocs, c'est votre variable.
{{< /callout >}}
![Scratch3-Blocks/iCompute-Scratch3-Blocks/png/Variables/my-variable@4x.png](/cours/Scratch3-Blocks/iCompute-Scratch3-Blocks/png/Variables/my-variable@4x.png)


Notre premier programme était très impersonnel ! Accueillons l'utilisateur avec un message personnalisé. 
{{< callout type="todo" title="Personnaliser le message" >}}
{{< checkbox checked="false" >}}Créez une variable appelée "Nom".{{< /checkbox >}}
{{< checkbox checked="false" >}}Ajoutez un bloc "demander [Quel est votre nom ?] et attendre" avant le bloc "dire".{{< /checkbox >}}
![ask-and-wait@4x.png](/cours/ask-and-wait@4x.png)
- Le bloc Demander est associé à une variable spéciale appelée "réponse". Ces deux blocs se trouvent dans la catégorie Capteur ("Sensing").
{{< checkbox checked="false" >}}Utilisez le bloc "mettre [Nom] à [réponse]" pour stocker la réponse de l'utilisateur dans la variable "Nom".{{< /checkbox >}}
 ![set-variable@4x.png](/cours/set-variable@4x.png)
{{< checkbox checked="false" >}}Utiliser un bloc "regrouper" pour rassembler "Bonjour" et la variable "Nom" dans le bloc "dire".{{< /checkbox >}}
![join@4x.png](/cours/join@4x.png)
{{< checkbox checked="false" >}}Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez voir le sprite demander votre nom et afficher un message personnalisé.{{< /checkbox >}}
{{< /callout >}}

## 1.2. Nos premiers calculs 
Notre première variable était un texte, mais on peut aussi utiliser des nombres.
{{< callout type="todo" title="Calculer l'année de naissance" >}}
{{< checkbox checked="false" >}}Créez une variable appelée "Âge" ainsi qu'une variable "Année de naissance".{{< /checkbox >}}
{{< checkbox checked="false" >}}Ajoutez un bloc "demander [Quel est votre âge ?] et attendre" avant le bloc "dire".{{< /checkbox >}}
{{< checkbox checked="false" >}}Utilisez le bloc "mettre [Âge] à [réponse]" pour stocker la réponse de l'utilisateur dans la variable "Âge".{{< /checkbox >}}
{{< checkbox checked="false" >}}Utilisez un bloc "mettre [Année de naissance] à [2025 - Âge]" pour calculer l'année de naissance de l'utilisateur.{{< /checkbox >}}
{{< checkbox checked="false" >}}Utilisez un bloc "dire" pour afficher "Vous êtes né en [Année de naissance]".{{< /checkbox >}}
{{< checkbox checked="false" >}}Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez voir le sprite demander votre âge et afficher l'année de naissance calculée.{{< /checkbox >}}
{{< /callout >}}

## 1.3. A vous de jouer 

{{< callout type="todo" title="Sprite tient un tacos" >}}
{{< checkbox checked="false" >}}Créer un programme qui demande à l'utilisateur combien de tacos et de kebab il veut commander. {{< /checkbox >}}
- Ce programmme répondra le montant total de la commande.
{{< checkbox checked="false" >}}Faire valider votre programme par l'enseignant.{{< /checkbox >}}
{{< /callout >}}