---
title: TP 0 - Introduction à la programmation avec Scratch
description: Ce premier TP est une introduction à la programmation. Il utilise le langage scratch.
date: 2025-08-01
draft: false
---

Pour cette semaine 0, nous allons (re)découvrir les bases de la programmation à travers le langage Scratch. Scratch est un langage de programmation visuel, développé par le MIT, qui permet de créer facilement des animations, des jeux et des histoires interactives.
![scratch interface](https://cs50.harvard.edu/x/notes/0/cs50Week0Slide162.png "scratch interface")
## Présentation de l'interface 

![scratch interface décrite](/images/scratch_description.png)

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


## Hello World
Pour commencer, nous allons créer un programme simple qui affiche "Hello World" à l'écran.

{{< callout type="todo" title="Hello World " >}}
{{< checkbox checked="false" >}}Ouvrez un éditeur Scratch sur le [site du MIT](https://scratch.mit.edu/projects/editor).{{< /checkbox >}}
{{< checkbox checked="false" >}}Dans la palette de blocs, trouvez le bloc "Quand le drapeau vert est cliqué".{{< /checkbox >}}
{{< checkbox checked="false" >}}Ajoutez le bloc "dire Bonjour pendant 2 secondes" sous le bloc précédent.{{< /checkbox >}}
{{< checkbox checked="false" >}}Modifier le texte pour Hello World{{< /checkbox >}}
{{< checkbox checked="false" >}}Cliquez sur le drapeau vert pour exécuter votre programme.   {{< /checkbox >}}
{{< checkbox checked="false" >}}Vous devriez obtenir le résultat suivant : {{< /checkbox >}}
![scratch says hello](/images/scratch_says_hello.png)
{{< /callout >}}


{{< callout type="tip" title="Besoin d'aide ?" retractable="true" open="False" >}}
Consultez la [documentation de Scratch](https://scratch.mit.edu/help) ou regardez des tutoriels en ligne.
{{< /callout >}}

## Ajoutons des variables
>[!info] Variables
> Les variables sont des conteneurs qui stockent des informations que vous pouvez utiliser dans votre programme. Dans Scratch, vous pouvez créer des variables pour stocker des nombres, du texte ou d'autres données.

Un peu impersonnel ce "Hello World", non ? Ajoutons une variable pour personnaliser le message.
{{< callout type="todo" title="Personnaliser le message" >}}
{{< checkbox checked="false" >}}Créez une variable appelée "Nom".{{< /checkbox >}}
{{< checkbox checked="false" >}}Ajoutez un bloc "demander [Quel est votre nom ?] et attendre" avant le bloc "dire".{{< /checkbox >}}
{{< checkbox checked="false" >}}Utilisez le bloc "mettre [Nom] à [réponse]" pour stocker la réponse de l'utilisateur dans la variable "Nom".{{< /checkbox >}}
{{< checkbox checked="false" >}}Utiliser un bloc "regrouper" pour rassembler "Bonjour" et la variable "Nom" dans le bloc "dire".{{< /checkbox >}}
{{< /callout >}}
