
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
