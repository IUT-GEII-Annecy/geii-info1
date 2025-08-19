---
title: TP 0 - Introduction à la programmation avec Scratch
description: Ce premier TP est une introduction à la programmation. Il utilise le langage scratch.
date: 2025-08-01
draft: false
---

{{< callout type="info" title="Objectif du TP" >}}
Pour cette semaine 0, nous allons (re)découvrir les bases de la programmation à travers le langage Scratch. 
L'utilisation de Scratch nous permettra de nous familiariser avec les concepts fondamentaux de la programmation sans avoir à se soucier de la syntaxe complexe des langages de programmation traditionnels.
A la fin de cette séance, vous connaitrez les principaux concepts de la programmation :
- Variables
- Boucles
- Conditions
Durant toute cette séance, s'il y a le moindre détail qui n'est pas clair pour vous, n'hésitez pas à poser une question à l'enseignant ou à un camarade.
{{< /callout >}}

> [!question] Je sais déjà programmer, est-ce que je peux passer ce TP ?
> Si vous avez déjà une expérience de programmation, les premiers exercices vous paraitront très simples. Faites alors le dernier exercice de chaque section et faites-le valider par l'enseignant. 
> Vous pourre alors choisir un problème de niveau avancé. 

{{< callout type="warning" title="Anglais ou français ? " >}}
Sur cette page, les images des blocs sont en anglais. Vous pouvez utiliser Scratch dans la langue de votre choix. 
{{< /callout >}}


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



# 0. Là où tout commence : Hello World
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
Le bloc "Quand le drapeau vert est cliqué" ("When green flag is clicked") se trouve dans la catégorie "Événements" ("Events").
Le bloc "dire" se trouve dans la catégorie "Apparence".
Consultez la [documentation de Scratch](https://scratch.mit.edu/help) ou regardez des tutoriels en ligne.
{{< /callout >}}

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
![my-variable@4x.png](/cours/my-variable@4x.png)


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


# 2. Conditions : Si, alors, sinon
{{< callout type="info" title="Qu'est-ce qu'une condition ?" >}}
Une condition est une instruction qui permet de prendre des décisions dans un programme.
Par exemple, si l'utilisateur a plus de 18 ans, on peut lui afficher un message différent que s'il a moins de 18 ans.
Sur Scratch, on utilise le bloc "si [condition] alors" pour créer une condition. 
On peut aussi utiliser le bloc "sinon" pour exécuter un bloc de code si la condition n'est pas remplie.
{{< /callout >}}

## 2.1. Conditions simples  
{{< callout type="todo" title="Condition simple" >}}
{{< checkbox checked="false" >}}Demander à l'utilisateur son âge et stocker la réponse dans une variable "Âge".{{< /checkbox >}}
{{< checkbox checked="false" >}}Utiliser un bloc "si [Âge > 18] alors"{{< /checkbox >}}
{{< checkbox checked="false" >}}Dans le bloc "si", ajouter un bloc "dire [Vous êtes majeur]" pour afficher un message si l'utilisateur est majeur.{{< /checkbox >}}
{{< checkbox checked="false" >}}Ajouter un bloc "sinon" pour afficher un message différent si l'utilisateur est mineur.{{< /checkbox >}}
{{< checkbox checked="false" >}}Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez voir le sprite demander votre âge et afficher un message différent selon que vous êtes majeur ou mineur.{{< /checkbox >}}
{{< /callout >}}

## 2.2. Conditions imbriquées
Les conditions peuvent aussi être imbriquées, c'est-à-dire qu'on peut mettre une condition à l'intérieur d'une autre condition. 

{{< callout type="todo" title="Condition imbriquée" >}}
{{< checkbox checked="false" >}}Créer un programme qui dit à l'utilisateur s'il est un enfant (0-12 ans), un adolescent (13-17 ans), un adulte (18-64 ans) ou un senior (65 ans et plus).{{< /checkbox >}}
- Pour cela, vous devrez utiliser des conditions imbriquées.
{{< checkbox checked="false" >}}Faire valider votre programme par l'enseignant.{{< /checkbox >}}
{{< /callout >}}



# 3. Boucles et répétitions
## Introduction : Un peu de mouvement
{{< callout type="todo" title="Ajouter du mouvement" >}}
{{< checkbox checked="false" >}}Ajoutez un bloc "quand le drapeau vert est cliqué"{{< /checkbox >}}
{{< checkbox checked="false" >}}Ajoutez un bloc "aller à x: [0] y: [0]"{{< /checkbox >}}
{{< checkbox checked="false" >}}Ajoutez un bloc "tourner de 15 degrés"{{< /checkbox >}}
{{< checkbox checked="false" >}}Ajoutez un bloc "avancer de 10 pas"{{< /checkbox >}}
{{< checkbox checked="false" >}}Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez voir le sprite se déplacer et tourner.{{< /checkbox >}}
{{< checkbox checked="false" >}}Cliquer autant de fois que vous voulez pour faire faire un tour complet à votre sprite.{{< /checkbox >}}
{{< /callout >}}

Répondre à la question suivante avant de regarder la réponse :
> [!question]- Combien de fois faut-il cliquer pour faire un tour complet ?
> Il faut cliquer 24 fois pour faire un tour complet, car 360 degrés divisé par 15 degrés donne 24.

> [!question]- Comment faire pour que le sprite fasse un tour complet sans avoir à cliquer 24 fois ?
> Pour faire faire un tour complet à votre sprite sans avoir à cliquer 24 fois, on peut simplement copier le bloc "tourner de 15 degrés" et le bloc "avancer de 10 pas" 24 fois.
> Vous pouvez faire l'esai. 
> 
> Il y a une meilleure solution : utiliser une boucle.

## 3.1. Boucles
{{< callout type="info" title="Qu'est-ce qu'une boucle ?" >}}
Une boucle est une structure de programmation qui permet de répéter un bloc de code plusieurs fois sans avoir à le réécrire. 
Par exemple, si vous voulez faire tourner un sprite de 15 degrés 24 fois, vous pouvez utiliser une boucle pour éviter de répéter le bloc "tourner de 15 degrés" 24 fois.
Sur Scratch, on utilise le bloc "répéter [nombre] fois" pour créer une boucle.
{{< /callout >}}

{{< callout type="todo" title="Utiliser une boucle" >}}
{{< checkbox checked="false" >}}Ajoutez un bloc "répéter 24 fois" autour des blocs "tourner de 15 degrés" et "avancer de 10 pas".{{< /checkbox >}}
{{< checkbox checked="false" >}}Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez voir le sprite faire un tour complet en 24 étapes.{{< /checkbox >}}
{{< checkbox checked="false" >}}Modifier le programme pour que le sprite fasse deux tours complets. {{< /checkbox >}}
{{< /callout >}}

## 3.2. Boucles infinies
{{< callout type="info" title="Qu'est-ce qu'une boucle infinie ?" >}}
Une boucle infinie est une boucle qui ne s'arrête jamais.
Par exemple, si vous utilisez le bloc "répéter indéfiniment", le programme continuera à exécuter le bloc de code à l'intérieur de la boucle sans jamais s'arrêter.
Sur Scratch, on utilise le bloc "répéter indéfiniment" pour créer une boucle infinie.
{{< /callout >}}

### 3.2.1. Déplacer un sprite au clavier

{{< callout type="todo" title="Déplacer un sprite au clavier" >}}
{{< checkbox checked="false" >}}Copier le code ci-dessus. {{< /checkbox >}}
{{< /callout >}}

> [!question]- Que se passe-t-il si vous appuyez sur la touche "flèche droite" ?
> Il ne se passe rien... 
> 
> **Pourquoi ?**
> Lorsque le programme est lancé, il vérifie si la touche "flèche droite" est pressée. Si c'est le cas, il déplace le sprite de 10 pas vers la droite. Sinon, il ne fait rien.
> Le problème est que le programme ne vérifie pas en continu si la touche "flèche droite" est pressée. Il ne le fait qu'une seule fois au début du programme.
> Vous pouvez le vérifier en maintenant la touche "flèche droite" pendant que vous lancez le programme. Le sprite se déplace car la touche est pressée au moment du lancement du programme. Il ne le fait qu'une seule fois, et ne continue pas à vérifier si la touche est pressée.

{{< callout type="todo" title="Corriger le programme" >}}
{{< checkbox checked="false" >}}Entourez le bloc "si [touche flèche droite pressée] alors" avec un bloc "répéter indéfiniment".{{< /checkbox >}}
{{< checkbox checked="false" >}}Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez maintenant pouvoir déplacer le sprite en maintenant la touche "flèche droite" enfoncée.{{< /checkbox >}}
{{< checkbox checked="false" >}}Ajoutez des blocs similaires pour les touches "flèche gauche", "flèche haut" et "flèche bas" pour déplacer le sprite dans toutes les directions.{{< /checkbox >}}
- **ASTUCE** : Vous pouvez dupliquer tout le bloc "si [touche flèche pressée] alors" avec un clic droit et en sélectionnant "Dupliquer". Cela vous permettra de gagner du temps pour créer les autres directions.
{{< checkbox checked="false" >}}Cliquez sur le drapeau vert pour exécuter votre programme. Vous devriez maintenant pouvoir déplacer le sprite dans toutes les directions en utilisant les touches fléchées.{{< /checkbox >}}
{{< /callout >}}

### 3.2.2. Un premier jeu

Nous allons ajouter un second sprite qu'il faudra attraper. 

{{< callout type="info" title="Un code pour chaque sprite" >}}
Chaque sprite peut avoir son propre code. Vous pouvez ajouter un nouveau sprite en cliquant sur le bouton "Choisir un sprite" en bas à droite de l'interface. 
Chaque sprite peut avoir son propre code, ce qui permet de créer des interactions entre les sprites. 
{{< /callout >}}

{{< callout type="todo" title="Attraper le sprite" >}}
{{< checkbox checked="false" >}}Ajoutez un nouveau sprite (par exemple, un chat) à votre projet{{< /checkbox >}}
{{< /callout >}}
>
> **Dans le code de ce nouveau sprite :**
> {{< checkbox checked="false" >}}Ajoutez un bloc "quand le drapeau vert est cliqué"{{< /checkbox >}}
> {{< checkbox checked="false" >}}Ajoutez un bloc "Aller à position aléatoire" pour que le sprite apparaisse à une position aléatoire sur la scène.{{< /checkbox >}}
> {{< checkbox checked="false" >}}Ajoutez un bloc "répéter indéfiniment" à l'intérieur duquel vous ajouterez un bloc si touche [votre sprite] alors aller à une position aléatoire.{{< /checkbox >}}
> {{< checkbox checked="false" >}}Testez votre programme et faites valider votre programme par l'enseignant.{{< /checkbox >}}
