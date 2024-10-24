import qcm
import random

""" 
    Code Groupe B.20 - P2_B20_Programme 

    Groupe:
    - Andrade Orletti, Enzo
    - M'Rabti, Jad 
    - Sibomana, Pedro       
    - Profirov, Viktor
    
 """


#1. Nous créons notre propre PRNG, car nous utilisons
#l'une de ses méthodes pour mélanger les réponses.
class PRNG:
    def __init__(self, seed, intervalle):
        self.seed = seed
        self.intervalle = intervalle
        self._rng = random.Random(seed)  # Générateur de nombres aléatoires avec une seed définie

    def next_int(self):
        # Nous garantissons que les nombres générés sont dans l'intervalle correct
        return self._rng.randint(0, self.intervalle - 1)


#2.On intialise le prng qui va contenir une graine aléatoire
# à chaque fois que le programme est lancé
graine = random.randint(1, 100)

intervalle = 100 # Nous fixons l'intervalle à 100,
# car il sera utilisé comme la capacité totale
# d'une simulation de mémoire que nous allons créer.

prng = PRNG(graine, intervalle)

#3. Ici, nous créons une fonction qui permet à l'utilisateur de
# choisir quel test il souhaite effectuer.
def chosen_qcm():
    """Cette fonction retourne lequel QCM
    l'utilisateur souhaite réaliser

    @pre: -

    @post:
    - retourne la variable filename (où sera stocké
    le nom du fichier QCM)
    """
    print()
    print("Choisissez un QCM:")
    print("\t1. QCM.txt")
    print("\t2. QCM2.txt")
    print("\t3. QCM3.txt")
    print()
    filename = None
    answer = (input("Entrez votre choix: "))
    if answer == '1':
        filename = "QCM.txt"
        return filename
    elif answer == '2':
        filename = "QCM2.txt"
        return filename
    elif answer == '3':
        filename = "QCM3.txt"
        return filename
    else:
        print("Cette option n'existe pas")
        while answer != '1' and answer != '2':
            answer = input("Entrez votre choix: ")
            if answer != '1' and answer != '2':
                print("Cette option n'existe pas")

        if answer == '1':
            filename = "QCM.txt"
            return filename
        elif answer == '2':
            filename = "QCM2.txt"
            return filename
        elif answer == '3':
            filename = "QCM3.txt"
            return filename


def toutes_ou_une_seule_cotation():


    print("Choisissez combien modes de correction voulez-vous: ")
    print("\t1. Toutes | Mode comparaison")
    print("\t2. Une seule | Mode évaluation")
    print()

def quelle_seule_cotation():
    print("Choisissez un mode de cotation:")
    print("\ta. Cotation gentile")
    print("\tb. Cotation sévère")
    print("\tc. Cotation neutre")


toutes_ou_une_seule_cotation()
cotation = None
choix = input("Entrez votre choix: ")
if choix == '1':
    cotation = 'Toutes'

elif choix == '2':
    quelle_seule_cotation()
    choix = input("Entrez votre choix: ")
    if choix == 'a':
        cotation = 'facile'
    elif choix == 'b':
        cotation = 'dificile'
    elif choix == 'c':
        cotation = 'neutre'
    else:

        while choix != 'a' and choix != 'b' and choix != 'c':
            print("Cette option n'existe pas")
            choix = input("Entrez votre choix: ")


else:

    while choix != '1' and choix != '2':
        print("Cette option n'existe pas")
        choix = input("Entrez votre choix: ")

    if choix == '1':
        cotation = 'Toutes'

    elif choix == '2':
        quelle_seule_cotation()
        choix = input("Entrez votre choix: ")
        if choix == 'a':
            cotation = 'facile'
        elif choix == 'b':
            cotation = 'sévère'
        elif choix == 'c':
            cotation = 'neutre'
        else:

            while choix != 'a' and choix != 'b' and choix != 'c':
                print("Cette option n'existe pas")
                choix = input("Entrez votre choix: ")


def show_cotation(cotation):
    if cotation == 'Toutes':
        print("Votre résultat:")
        print(f"\tCotation sympathique : {note_gentille} / {total_general}")
        print(f"\tCotation sévère : {note_severe} / {total_general}")
        print(f"\tCotation neutre : {round(note_neutre, 1)} / {round(total_neutre,0)}")

    elif cotation == 'facile':
        print("Votre résultat:")
        print(f"Cotation gentille : {note_cotation_chosie} / {total_general}")

    elif cotation == 'dificile':
        print("Votre résultat:")
        print(f"Cotation sévère : {note_cotation_chosie} / {total_general}")

    elif cotation == 'neutre':
        print("Votre résultat:")
        print(f"Cotation neutre : {round(note_cotation_chosie,1)} / {round(total_neutre,0)}")



#5. Nous créons une fonction pour déterminer les instructions
# à suivre lors de la réalisation du QCM
def instructions():
    return"Veuillez répondre chaque question avec la chiffre de l'option souhaitée"




if __name__ == '__main__':
    filename = chosen_qcm()
    #filename = "QCM3.txt"


    # Chargement du questionnaire
    questions = qcm.build_questionnaire(filename)

    total_neutre = 0
    total_general = 0

    #On intialise la variable 'note' pour
    #stocker la valeur de la note de
    #l'utilisateur
    note_gentille = 0
    note_severe = 0
    note_neutre = 0
    note_cotation_chosie = 0

    #6. On definit les modes de cotation
    def cotation_gentil(liste, index):
        if liste[index][1] == True:
            return 1
        else:
            return 0

    def cotation_severe(liste, index):
        if liste[index][1] == True:
            return 1
        else:
            return -1

    #
    def cotation_neutre(liste, index, compteur_bonnes_reponses):

        """Pourcentage des reponses vraies"""

        total_options = len(liste)

        pourcentage = compteur_bonnes_reponses / total_options

        


        #La pourcentage ne peut pas être plus grande que 1
        if pourcentage > 1:
            print("Il y a plus de réponses correctes que d'options")
            return False

        if pourcentage == 1: #Ex: 10/10
            if liste[index][1] == True:
                return 0.1

            else:
                return 0

        elif pourcentage >= 0.9: #Ex: 9/10
            if liste[index][1] == True:
                return 0.2

            else:
                return 0

        elif pourcentage >= 0.8: #Ex: 8/10
            if liste[index][1] == True:
                return 0.3
            else:
                return 0

        elif pourcentage >= 0.7: #Ex: 7/10
            if liste[index][1] == True:
                return 0.4
            else:
                return 0

        elif pourcentage >= 0.6:
            if liste[index][1] == True:
                return 0.5
            else:
                return 0

        elif pourcentage >= 0.5:
            if liste[index][1] == True:
                return 0.6
            else:
                return 0

        elif pourcentage >= 0.4:
            if liste[index][1] == True:
                return 0.7
            else:
                return 0


        elif pourcentage >= 0.3:
            if liste[index][1] == True:
                return 0.8
            else:
                return 0

        elif pourcentage >= 0.2:
            if liste[index][1] == True:
                return 0.9
            else:
                return 0


        elif pourcentage < 0.2 and pourcentage > 0:
            if liste[index][1] == True:
                return 1
            else:
                return 0






    print()
    print("TEST QCM - Octobre 2024")
    print()
    print('-'*len(instructions()))
    print(instructions())
    print('-' * len(instructions()))



    for question in range(len(questions)):


        print()
        print(f'\tQuestion {question + 1}: {questions[question][0]}') #Chaque option de réponse est imprimée

        reponses_user = [] #liste pour stocker les options déjà répondues
        # par l'utilisateur et effectuer les comparaisons nécessaires

        compteur_bonnes_reponses = 0 #varibale pour stocker la quantité de bonnes reponses par question

        compteur_options = 0

        bonnes_reponses = []



        for reponses in questions[question][1]:
            compteur_options += 1
            if reponses[1] == True:
                compteur_bonnes_reponses += 1

        total_general += compteur_bonnes_reponses


        proportion = compteur_bonnes_reponses / compteur_options
        total_neutre += (compteur_bonnes_reponses * proportion)


        for number in range(compteur_bonnes_reponses):
            bonnes_reponses.append(number)

        #print(bonnes_reponses)


        #Voir README.txt - 'TOUTES LES RÉPONSES PRÉCÉDENTES'
        for reponses in questions[question][1]:
            if reponses[0] == 'Toutes les réponses précédentes' and reponses[1] == True:
                new_len = 1
                bonnes_reponses = [new_len]






        #7. Nous créons une liste qui copie toutes les options de réponses
        # pour chaque question du questionnaire
        liste_originale =  questions[question][1]
        liste_copie = liste_originale[:]

        #8. Nous créons notre mémoire qui servira à mélanger les réponses
        memoire = []
        for zero in range(102):
            memoire.append(0)


        #print(liste)
        #for r in liste_copie:
            #print(r)

        #9. Nous allons retirer tous les éléments de la liste copie et les placer à
        # différents endroits dans la mémoire
        while len(liste_copie) != 0:

            # On va prendre aleatoirement une des reponses pour la placer dans la memoire
            index_to_get = random.randint(0, len(liste_copie)-1)
            if liste_copie[index_to_get] not in memoire:

                # Voir README.txt - 'TOUTES LES RÉPONSES PRÉCÉDENTES'
                if liste_copie[index_to_get][0] == 'Toutes les réponses précédentes':
                     memoire[-1] = liste_copie[index_to_get]
                     liste_copie.remove(liste_copie[index_to_get])

                else:


                    #À travers le prng, on détermine l'indice où
                    # la réponse va être stocké dans la memoire
                    index_to_put = prng.next_int()

                    if memoire[index_to_put] == 0:
                        memoire[index_to_put] = liste_copie[index_to_get]
                        liste_copie.remove(liste_copie[index_to_get])
                    else:
                        index_to_put = prng.next_int() #On obtient un nouveau endroit dans le memoire
                        memoire[index_to_put] = liste_copie[index_to_get]
                        liste_copie.remove(liste_copie[index_to_get])

        #print(memoire)
        #10. Nous créons alors une nouvelle liste en prenant les réponses
        # qui ont été mélangées dans la mémoire.
        reponses = [reponse for reponse in memoire if reponse != 0] #On obtient la liste des reponses melangés à chaque fois
        #que le programme est lancé



        #print(reponses)
        for r in range(len(reponses)):
            print(f'\t\t{r+1}. {reponses[r][0]}')


        #11. Nous déterminons le nombre d'options pour cette question et
        # limitons le nombre de réponses de l'utilisateur à exactement
        # le même nombre de réponses correctes de la question
        limite_de_choix = compteur_bonnes_reponses
        reponses_possibles = len(questions[question][1])


        while len(reponses_user) != len(bonnes_reponses):


            answer = input("Entrez votre choix: ")

            #D'abord, on regarde si l'utilisateur a      
            #entré un nombre                             
            if answer.isdigit() == False:                
                print("Vous n'avez pas entré un nombre") 
                                                         
            else:                                        
                answer = int(answer)

                #On vérifie si la réponse se trouve parmi les reponses
                #possibles
                if answer <= 0 or answer > reponses_possibles:
                    print("Cette option n'existe pas")


                #Ensuite, on vérifie s'il à déjà choisi cette
                #option avant
                elif answer in reponses_user:
                    print("Vous avez déjà choisi cette option")

                #Si sa réponse répond à tous les critères, nous vérifions si elle est
                # correcte ou incorrecte et effectuons l'ajustement de sa note
                else:
                    reponses_user.append(answer)
                    index = answer - 1


                    #Voici en bas, on assure que si l'utilisateur repond 'Toute les reponses précedentes'
                    #le programme passe directement à la prochaine question.

                    #Voir README.txt - 'TOUTES LES RÉPONSES PRÉCÉDENTES'
                    if reponses[index][0] == 'Toutes les réponses précédentes':
                        if reponses[index][1] == True:
                            note_gentille += 1 - len(reponses_user)
                            note_neutre += 1 - len(reponses_user)
                            note_severe += 1 - len(reponses_user)
                            total_general -= len(reponses) + 1
                            total_neutre -= (len(reponses)/ len(reponses) + 1)

                            break

                        note_gentille += cotation_gentil(reponses, index)
                        note_severe += cotation_severe(reponses, index)
                        note_neutre += cotation_neutre(reponses, index, compteur_bonnes_reponses)
                        break



                    note_gentille += cotation_gentil(reponses, index)
                    note_severe += cotation_severe(reponses, index)
                    note_neutre += cotation_neutre(reponses, index, compteur_bonnes_reponses)


                    if cotation == 'facile':
                        # Voir README.txt - 'TOUTES LES RÉPONSES PRÉCÉDENTES'
                        if reponses[index][0] == 'Toutes les réponses précédentes':
                            if reponses[index][1] == True:
                                note_cotation_chosie += 1 - len(reponses_user)
                                break
                        note_cotation_chosie += cotation_gentil(reponses, index)
                    elif cotation == 'sévère':
                        # Voir README.txt - 'TOUTES LES RÉPONSES PRÉCÉDENTES'
                        if reponses[index][0] == 'Toutes les réponses précédentes':
                            if reponses[index][1] == True:
                                note_cotation_chosie += 1 - len(reponses_user)
                                break
                        note_cotation_chosie += cotation_severe(reponses, index)
                    elif cotation == 'neutre':
                        # Voir README.txt - 'TOUTES LES RÉPONSES PRÉCÉDENTES'
                        if reponses[index][0] == 'Toutes les réponses précédentes':
                            if reponses[index][1] == True:
                                note_cotation_chosie += 1 - len(reponses_user)

                                break
                        note_cotation_chosie += cotation_neutre(reponses, index, compteur_bonnes_reponses)


#total_neutre = total_neutre / len(questions)

#12. Le resultat est affiché sur l'ecran
print()
show_cotation(cotation)
