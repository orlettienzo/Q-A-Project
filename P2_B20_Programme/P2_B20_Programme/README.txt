SINF - Groupe B.20 - APP2

Explication du code :

Nous allons maintenant expliquer, étape par étape, la mise en œuvre de notre code.
Pour plus de détails, veuillez consulter le rapport qui vous a été fourni.

1- Nous avons créé le fichier prng.py pour réaliser notre propre PRNG, en utilisant la
bibliothèque random et ses méthodes. Nous avons testé et vérifié qu'il répondait aux
exigences établies par INGinious.

2- Une fois créé et passé les tests sans erreurs, nous avons implémenté la classe PRNG
dans le fichier code_b20.py, où se trouve le code de notre projet.

3- Nous avons importé le fichier qcm, qui servira à créer le questionnaire sous forme de
liste, ainsi que la bibliothèque random de Python pour générer des nombres aléatoires,
fonctionnalité qui sera utile dans différentes parties de notre code.

4- Nous avons établi une variable 'graine' qui, chaque fois que nous exécutons le code,
reçoit un nombre entier aléatoire entre 1 et 100. Nous initialisons le PRNG juste après,
où la valeur de la variable graine sera la seed du PRNG (ainsi, chaque fois que nous
exécutons le code, nous avons 99 % de chances de générer une nouvelle seed, ce qui
entraînera la création d'un nouveau PRNG). L'intervalle sera toujours fixe (dans range(100)).

5- Nous avons créé une fonction qui permet à l'utilisateur de choisir quel QCM il souhaite
réaliser. La fonction s'appelle 'chosen_qcm().

6- Après avoir choisi le QCM, l'utilisateur pourra décider comment il souhaite être évalué.
Pour cela, nous avons déterminé deux fonctions uniquement pour imprimer le texte à l'écran
et créé la variable globale 'cotation' qui stockera la réponse correspondant au mode de
correction choisi par l'utilisateur.

7- Nous avons défini une fonction qui reçoit comme paramètre la variable globale 'cotation'
et, grâce à cela, elle imprimera la note de l'utilisateur en fonction de son option.

8- La fonction intructions() imprime à l'écran les instructions à suivre lors de la
réalisation du QCM.

9- Le fichier texte du QCM choisi est stocké dans la variable filename, et la liste est
créée à l'aide de la méthode build_questionnaire(filename), qui est à son tour stockée
dans la variable questions.

10- Étant donné la différence entre les modes de correction,
nous avons décidé de créer 2 variables avec la valeur totale du QCM :

    10.1- total_general --> somme totale des responses correctes dans le QCM
    (pour les modes de cotation: facile + méchante)

    10.2- total_neutre  --> somme totale des proportions de reponses correctes par question
    (pour le mode de cotation: neutre)

11- Pour chaque QCM, nous avons défini 4 variables différentes pour les notes possibles,
qui seront incrémentées à chaque réponse de l'utilisateur.


12- Nous avons déterminé le comportement de chaque mode de correction, en mettant
particulièrement l'accent sur le mode de correction neutre, où nous calculons d'abord
le pourcentage de réponses correctes par question. En général, nous avons établi que
plus la probabilité de réussite est faible (c'est-à-dire plus le pourcentage de réponses
correctes est bas), plus chaque réponse correcte vaudra cher, et vice versa.

13- Nous avons implémenté une boucle 'for' pour chaque question du QCM et, à l'intérieur,
nous avons passé toutes les commandes afin que la réalisation du test se déroule comme
nous l'avons établi :

    13.1- À chaque question, une liste vide est initiée et va stocker les réponses de
    l'utilisateur ("=reponses_user"). Elle servira en pratique à éviter que l'utilisateur
    gagne plus de points en répondant plusieurs fois à la même option (car cela ne se produit
    pas dans la vie réelle).

    13.2- Nous avons initialisé 2 compteurs, l'un pour le nombre de réponses et l'autre pour
    le nombre de réponses correctes. Nous avons également créé une liste de réponses correctes,
    dont nous allons utiliser le nombre d'éléments pour limiter la quantité de réponses possibles
    que l'utilisateur pourra saisir.

-----------------------------------------------------
'TOUTES LES RÉPONSES PRÉCÉDENTES'

(!) ÉTANT DONNÉ QU'EN RÉALITÉ, LORSQUE NOUS COCHONS L'OPTION 'TOUTES LES RÉPONSES PRÉCÉDENTES',
NOUS NE COCHONS PAS LES AUTRES, NOUS AVONS DÉTERMINÉ CE QUI SUIT POUR RENDRE LA RÉALISATION
DU TEST PLUS JUSTE :

     1. FICHIER QCM TEXTE: SI 'TOUTES LES RÉPONSES PRÉCÉDENTES' = V
     => TOUTES L'AUTRES OPTIONS = V

     2. SOUCIS AVEC LE NOMBRE DE REPONSES CORRECTES
     => POSSIBILITÉ DE GAGNER PLUS DE POINTS S'IL NE RÉPOND PAS 'TOUTES LES RÉPONSES
     PRÉCÉDENTES'

     3. SI 'TOUTES LES RÉPONSES PRÉCÉDENTES' = V
     => LIMITATION DU NOMBRE DE REPONSES POSSIBLES À 1; L'UTILISATEUR
     PEUT RÉPONDRE SEULEMENT 1 FOIS

     4. SI REPONSE = 'TOUTES LES RÉPONSES PRÉCÉDENTES'
     => IL GAGNE 1/1 POINTS (LA VALEUR DU TOTAL DIMINUE)

     5. PAR CONTRE, SI REPONSE = AUTRE OPTION QUELCONQUE
     => IL GAGNE 1/NOMBRE DE REPONSES CORRECTES (= NOMBRE DE REPONSES POSSIBLES)
     => IL GANGE 1/NOMBRE DE RÉPONSES POSSIBLES
     (LA VALEUR DU TOTAL N'EST PAS MODIFIÉE)

    6. LE PROGRAMME PASSE DIRECTEMENT À LA QUESTION SUIVANTE APRÈS LA
    PREMIÈRE RÉPONSE DE L'UTILISATEUR DANS CE CAS

PS : Comme nous n'avons pas le droit de modifier les fichiers texte de base, le fait
que l'option soit nommée 'Toutes les réponses précédentes' implique qu'elle doit toujours
être affichée comme la dernière option. Nous avons introduit cette condition dans notre code,
où nous garantissons qu'indépendamment du mélange de l'ordre des réponses, elle sera toujours la
dernière option à être affichée.
-----------------------------------------------------

14- Explication de la méthode de mélange des réponses :

    14.1-  À partir de la liste originale, nous créons une copie contenant uniquement les
    réponses et leurs valeurs booléennes correspondantes.

    14.2- Nous créons une sorte de mémoire où nous allons allouer aléatoirement les réponses.
    Au départ, elle contiendra uniquement des zéros (0).

    14.3- Nous utilisons la bibliothèque random pour générer l'indice de l'élément que nous
    allons prendre dans la liste copie. Après l'avoir sélectionné, nous utilisons la méthode
    de notre PRNG pour générer un nombre entier aléatoire qui sera l'indice où la réponse
    se situera dans la mémoire. Nous répétons ce processus jusqu'à ce que la liste copie soit vide.

    14.4- Nous obtenons le nouvel ordre des réponses en créant une nouvelle liste sans les
    zéros de la mémoire, permettant ainsi de les afficher de la manière la plus aléatoire
    possible à chaque exécution du programme.

15- Les options de réponses sont imprimées.

16- Nous avons créé 2 variables :

    16.1- limite_de_choix --> stocke le nombre de réponses correctes ;
    limite le nombre de réponses que l'utilisateur pourra saisir.

    16.2- reponses_possibles --> stocke le nombre d'options de réponses par question ;
    sert de paramètre pour vérifier si l'utilisateur répond à un nombre supérieur au nombre
    de réponses possibles.

17- Ensuite, nous demandons la réponse de l'utilisateur, qui doit respecter les critères suivants :
    - Être parmi les options possibles
    - Être un nombre
    - Ne pas être répétée

18- Si la réponse respecte tous les critères, nous calculons sa valeur en fonction du
mode de correction choisi et mettons à jour la note de l'utilisateur. Sinon, l'utilisateur
devra répondre à nouveau à la question jusqu'à ce que sa réponse respecte les critères mentionnés.

19- Le résultat de l'utilisateur est affiché à l'écran et le programme se termine.
































