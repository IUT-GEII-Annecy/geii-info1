---
title: TP 0 - Introduction à la programmation avec Scratch
description: Ce premier TP est une introduction à la programmation. Il utilise le langage scratch.
date: 2025-08-01
draft: false
weight: 1
---

> [!info]  
> **Objectif du TP**  
> Pour cette semaine 0, nous allons (re)découvrir les bases de la programmation à travers le langage Scratch. 
> L'utilisation de Scratch nous permettra de nous familiariser avec les concepts fondamentaux de la programmation sans avoir à se soucier de la syntaxe complexe des langages de programmation traditionnels.
> A la fin de cette séance, vous connaitrez les principaux concepts de la programmation :
> - Variables
> - Boucles
> - Conditions
> Durant toute cette séance, s'il y a le moindre détail qui n'est pas clair pour vous, n'hésitez pas à poser une question à l'enseignant ou à un camarade.

{{< details "Question : Je sais déjà programmer, est-ce que je peux passer ce TP ?" >}}
> Si vous avez déjà une expérience de programmation, les premiers exercices vous paraitront très simples. Faites alors le dernier exercice de chaque section et faites-le valider par l'enseignant. 
> Vous pourre alors choisir un problème de niveau avancé.
{{< /details >}}

> [!warning]  
> **Anglais ou français ?**  
> Sur cette page, les images des blocs sont en anglais. Vous pouvez utiliser Scratch dans la langue de votre choix.


## Présentation de l'interface 

![![scratch interface décrite](/images/scratch_description.png)](/images/scratch_description.png)

L'interface de Scratch est divisée en plusieurs sections :
- **Palette de blocs** : où vous trouverez les différents blocs de code que vous pouvez utiliser
    - **Mouvement** : pour déplacer les sprites
    - **Apparence** : pour modifier l'apparence des sprites
    - **Événements** : pour déclencher des actions
    - **Contrôle** : pour gérer le flux du programme
    - **Sons** : pour ajouter des effets sonores
- **Zone de script** : où vous assemblez les blocs pour créer votre programme
- **Zone de scène** : où vous pouvez voir votre projet en action
- **Liste des sprites** : où vous pouvez ajouter ou sélectionner les sprites de votre projet



# 0. Là où tout commence : Hello World
Pour commencer, nous allons créer un programme simple qui affiche "Hello World" à l'écran.

> [!note]  
> **À faire : Hello World**  
> {{< checkbox checked="false" >}}Ouvrez un éditeur Scratch sur le [site du MIT](https://scratch.mit.edu/projects/editor).{{< /checkbox >}}
> {{< checkbox checked="false" >}}Dans la palette de blocs, trouvez le bloc "Quand le drapeau vert est cliqué".{{< /checkbox >}}
> {{< checkbox checked="false" >}}Ajoutez le bloc "dire Bonjour pendant 2 secondes" sous le bloc précédent.{{< /checkbox >}}
> {{< checkbox checked="false" >}}Modifier le texte pour Hello World{{< /checkbox >}}
> {{< checkbox checked="false" >}}Cliquez sur le drapeau vert pour exécuter votre programme.   {{< /checkbox >}}
> {{< checkbox checked="false" >}}Vous devriez obtenir le résultat suivant : {{< /checkbox >}}
> ![![scratch says hello](/images/scratch_says_hello.png)](/images/scratch_says_hello.png)


> [!tip]  
> **Besoin d'aide ?**  
> Le bloc "Quand le drapeau vert est cliqué" ("When green flag is clicked") se trouve dans la catégorie "Événements" ("Events").
> Le bloc "dire" se trouve dans la catégorie "Apparence".
> Consultez la [documentation de Scratch](https://scratch.mit.edu/help) ou regardez des tutoriels en ligne.

Vous êtes prêts pour commencer à jouer avec [les variables](/cours/TP0-1 Les Variables)