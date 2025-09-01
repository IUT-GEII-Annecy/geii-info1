---
title: TP 1 - Configuration
description: Ce premier TP est une introduction à la programmation.
date: 2025-08-31
draft: false
weight: 101
---
# Un peu de configuration 
## Avant toute chose : Un compte GitHub !

> [!info]  
> **GitHub ? Qu'est-ce que c'est ?**  
> GitHub est une plateforme de développement collaboratif qui permet de stocker et de partager du code. 
> Vous l'utiliserez pour soumettre vos travaux pratiques et collaborer avec vos camarades.
>
> Dans le monde professionnel, GitHub est un outil incontournable pour le développement logiciel. Il sert notamment à gérer les versions du code, à collaborer avec d'autres développeurs et à partager des projets open source.

> [!note]  
> **À faire : Créer un compte GitHub**  
> {{< checkbox checked="false" >}}Si vous n'avez pas encore de compte GitHub, créez-en un : {{< /checkbox >}}
>   - **Attention, ce compte vous sera utile dans votre vie professionnelle, choisissez votre pseudo avec soin !**
>   {{< checkbox checked="false" >}}Utilisez votre **adresse email académique** pour créer votre compte sur [GitHub](https://github.com).{{< /checkbox >}}
> {{< checkbox checked="false" >}}Rejoignez le cours du semestre 1 : {{< /checkbox >}}
>   {{< checkbox checked="false" >}}Cliquez sur ce lien [submit.cs50.io](https://submit.cs50.io/invites/61a963c727374a32aa487ead18d908c5) et connectez votre compte GitHub{{< /checkbox >}}
>   - Ce site contiendra vos rendus et les retours des enseignants. 
> {{< checkbox checked="false" >}}Lancez l'IDE{{< /checkbox >}}
>   {{< checkbox checked="false" >}}Rendez-vous sur la page de [cs50](https://cs50.dev). {{< /checkbox >}}
>   {{< checkbox checked="false" >}}Cliquez sur `Log in`{{< /checkbox >}}


## Le terminal 
### Présentation
En bas de la fenêtre de vsCode, vous trouverez un terminal. C'est un outil qui vous permet d'interagir avec votre système d'exploitation en utilisant des commandes textuelles. 

> [!important]  
> **Liste des commandes utiles**  
> Voici quelques commandes de base que vous utiliserez fréquemment :    
> - `clear` :  nettoie l'affichage dans le terminal
> Les éléments entre chevrons <>, sont à remplacer en fonction du contexte
> - `cd <nom_du_dossier>` : change le répertoire courant pour `<nom_du_dossier>`.
>    - `cd ..` permet de remonter dans le dossier parent 
> - `code <nom_du_fichier>` permet d'ouvrir le fichier `<nom_du_fichier>` en le créant si besoin
> - `cp <source> <destination>` : copie un fichier ou dossier de `<source>` à `<destination>`.
> - `ls` : liste les fichiers et dossiers dans le répertoire courant.
> - `mv <source> <destination>` : déplace ou renomme un fichier ou dossier de `<source>` à `<destination>`.
> - `mkdir <nom_du_dossier>` : crée un nouveau dossier nommé `<nom_du_dossier>`.
> - `rm <nom_du_fichier>` : supprime le fichier nommé `<nom_du_fichier>`.
> - `rmdir <nom_du_dossier>` : supprime un dossier nommé `<nom_du_dossier>` (le dossier doit être vide).

> [!tip]  
> **L'autocomplétion dans le terminal**  
> Bien souvent, le terminal peut deviner ce que vous voulez faire à partir du début de la commande, à l'aide de la touche `Tab`.

Par, exemple, la commande suivante rentre dans le dossier `0_hello` se trouvant dans le dossier `tp1`
```bash
cd tp1/0_hello
```

> [!warning]  
> **Informations importantes à propos du terminal :**  
>  - Certains raccourcis ne sont pas les même qu'habituellement 
> 	 - `Ctrl-Maj-C` pour copier 
> 	 - `Maj-INSER` pour coller 
>  - Les commandes ne répondent souvent rien lorsqu'elle réussissent
>  - Il est impossible de bouger le curseur avec la souris. Il faut utiliser les flèches


### Téléchargement du dossier de TP
Prêts ? Allons-y ! Nous allons écrire nos premières commandes dans le terminal ... 

> [!note]  
> **À faire : Premières commandes dans le terminal**  
> <script src="https://asciinema.org/a/qiLs8ysmvZjWn8MoMIZMel1wZhttps://asciinema.org/a/.js" id="https://asciinema.org/a/" async="true"></script>
> {{< checkbox checked="false" >}}Télécharger les fichiers du tp1 : {{< /checkbox >}}
> 	{{< checkbox checked="false" >}}Copier la commande suivante puis la coller la dans le terminal `Maj-INSER`. Appuyer sur Entrée{{< /checkbox >}}
> 	```bash
> 	wget https://github.com/IUT-GEII-Annecy/squelettes/releases/download/branch-2025/tp1_2025.zip
> 	```
> {{< checkbox checked="false" >}}Décompresser le dossier et supprimer le *.zip*{{< /checkbox >}}
> 	{{< checkbox checked="false" >}}Exécuter la commande suivante **(Essayer l'autocomplétion en tapant `unzip t` puis en appuyant sur `Tab`)** : {{< /checkbox >}}
> 		```bash
> 		unzip tp1.zip
> 		```
> 	{{< checkbox checked="false" >}}Supprimer le fichier `tp1.zip` en exécutant {{< /checkbox >}}
> 		```bash
> 		rm tp1.zip
> 		```
> 	{{< checkbox checked="false" >}}Répondre `y` s'il demande confirmation{{< /checkbox >}}
>  {{< checkbox checked="false" >}}Vous pouvez afficher la liste des fichiers et dossiers avec la commande `ls`.{{< /checkbox >}}
> 	 ```bash
> 	 ls
> 	 ```
> {{< checkbox checked="false" >}}Naviguer dans le dossier `tp1/0_hello`{{< /checkbox >}}
> 	  ```bash
> 	  cd tp1/0_hello
> 	  ```
> {{< checkbox checked="false" >}}Créer un fichier `hello.c` :{{< /checkbox >}}
> 	  ```bash
> 	  code hello.c
> 	  ```
>   {{< checkbox checked="false" >}}Un nouvel onglet devrait s'ouvrir dans vsCode avec un fichier vide nommé `hello.c`.{{< /checkbox >}}
>   - *Vous pouvez également créer un fichier en cliquant sur l'icône "Nouveau fichier" dans l'explorateur de fichiers à gauche.*


> [!tip]  
> **Besoin d'aide ?**  
> CS50 Duck Debugger est là pour vous aider ! 
> Cliquer sur l'icône en forme de canard dans la colonne de gauche pour ouvrir l'extension.
> Vous pouvez lui demander "Answer in French" pour obtenir de l'aide en français.

   

