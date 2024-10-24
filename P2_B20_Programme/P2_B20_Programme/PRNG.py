import random

"""
Ceci est un fichier destiné à tester notre PRNG 
(Générateur de Nombres Pseudo-aléatoires).
"""

class PRNG:
    def __init__(self, seed, intervalle):
        self.seed = seed
        self.intervalle = intervalle
        self._rng = random.Random(seed)  # Générateur de nombres aléatoires avec une seed définie

    def next_int(self):
        # Nous garantissons que les nombres générés sont dans l'intervalle correct
        return self._rng.randint(0, self.intervalle - 1)






prng = PRNG(33, 11)

def is_correct(prng):
    """
    Cette fonction renvoie True dès que le PRNG réussit tous les tests

    """

    # Test1: même seed --> même sequence
    prng1 = prng
    prng2 = PRNG(33, 11)

    sequence1 = []
    sequence2 = []

    for i in range(10):
        sequence1.append(prng1.next_int())
    for i in range(10):
        sequence2.append(prng2.next_int())

    if sequence1 != sequence2:
        return False

    # Test2: Vérificarion de l'intervalle
    for number in sequence1:
        if number < 0 or number >= 11:
            return False

    # Test3: seed differente --> sequence differente
    prng3 = PRNG(42, 11)  # Nous utilisons une seed différente (42)

    sequence3 = []

    for i in range(10):
        sequence3.append(prng3.next_int())

    if sequence1 == sequence3:
        return False

    # Test4: tous les nombres sont positifs (>0)
    for number in sequence1:
        if number < 0:
            return False
    for number in sequence2:
        if number < 0:
            return False
    for number in sequence3:
        if number < 0:
            return False

    # Test5: Vérifier si le PRNG génère tous les nombres possibles dans l'intervalle [0, 10]
    prng4 = PRNG(33, 11)
    generated_numbers = set()  # Utiliser un set pour stocker les nombres uniques générés

    # Générer une séquence longue pour s'assurer que tous les nombres de l'intervalle apparaissent
    for number in range(100):  # Générer 100 nombres pour essayer de couvrir toutes les valeurs possibles
        generated_numbers.add(prng4.next_int())

    # Vérifier si l'ensemble contient tous les nombres de 0 à 10
    if generated_numbers != set(range(11)):
        return False

    # Test 6 (PRNG4): Vérifier si la seed 3 ne génère pas une séquence suffisamment aléatoire
    prng5 = PRNG(3, 11)
    sequence4 = [prng5.next_int() for number in range(20)]  # Générer 20 nombres avec la seed 3

    # Test 6.1: Vérifier le nombre de nombres uniques dans la séquence
    unique_numbers = len(set(sequence4))
    if unique_numbers < 5:  # S'il y a moins de 5 nombres uniques sur 20 essais, faible aléatoire
        return False

    # Test 6.2: Vérifier la distribution des nombres
    count_distribution = [0] * 11  # Créer une liste pour compter l'occurrence de chaque nombre de 0 à 10
    for number in sequence4:
        count_distribution[number] += 1

    # Si un nombre apparaît trop de fois (par exemple, plus de 50% des fois), faible variation
    if any(count > 10 for count in count_distribution):
        return False

    # Test 7 (PRNG6): Vérifier si la seed 10 ne génère pas une séquence suffisamment aléatoire
    prng6 = PRNG(10, 11)
    sequence5 = [prng6.next_int() for number in range(20)]  # Générer 20 nombres avec la seed 10

    # Test 7.1: Vérifier le nombre de nombres uniques dans la séquence
    unique_numbers_seed10 = len(set(sequence5))
    if unique_numbers_seed10 < 5:  # S'il y a moins de 5 nombres uniques, faible aléatoire
        return False

    # Test 7.2: Vérifier la distribution des nombres
    count_distribution_seed10 = [0] * 11  # Créer une liste pour compter l'occurrence de chaque nombre de 0 à 10
    for number in sequence5:
        count_distribution_seed10[number] += 1

    # Si un nombre apparaît trop souvent (plus de 10 fois), cela indique une faible variation
    if any(count > 10 for count in count_distribution_seed10):
        return False

    # Test 8 (PRNG2): Vérifier si la séquence générée forme un cycle
    prng7 = PRNG(33, 11)
    sequence6 = [prng7.next_int() for number in range(100)]  # Générer 100 nombres avec une seed

    # Stocker les sous-séquences déjà vues dans un ensemble (pour détecter les répétitions)
    seen_sequences = set()

    # Vérifier si une sous-séquence apparaît plus d'une fois
    for i in range(len(sequence6) - 10):  # Rechercher des cycles dans la séquence
        subsequence = tuple(sequence6[i:i + 10])  # Créer une sous-séquence de 10 nombres
        if subsequence in seen_sequences:  # Si la sous-séquence a déjà été vue, il y a un cycle
            return False
        seen_sequences.add(subsequence)

    # Si tous les tests sont réussis, le PRNG est considéré comme correct
    return True

print(f'Est-ce que la fonction is_correct(prng) retourne True?')
print(f'R: {is_correct(prng)}')
print()

# Test sequences differentes
prng1 = PRNG(33, 11)
prng2 = PRNG(34, 11)
prng3 = PRNG(35, 11)
prng4 = PRNG(36, 11)
prng5 = PRNG(37, 11)
prng6 = PRNG(38, 11)

limite = 20 #Vous pouvez choisir la limite que vous voulez
i = 0
print("Test sequences differentes")
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
while i != limite:
    l1.append(prng1.next_int())
    l2.append(prng2.next_int())
    l3.append(prng3.next_int())
    l4.append(prng4.next_int())
    l5.append(prng5.next_int())
    l6.append(prng6.next_int())
    i += 1

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)


# Test Séquences identiques
prng1 = PRNG(33, 11)
prng2 = PRNG(33, 11)
prng3 = PRNG(33, 11)
prng4 = PRNG(33, 11)
prng5 = PRNG(33, 11)
prng6 = PRNG(33, 11)

limite = 20 #Vous pouvez choisir la limite que vous voulez
i = 0
print()
print("Test sequences identiques")
l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
l6 = []
while i != limite:
    l1.append(prng1.next_int())
    l2.append(prng2.next_int())
    l3.append(prng3.next_int())
    l4.append(prng4.next_int())
    l5.append(prng5.next_int())
    l6.append(prng6.next_int())
    i += 1

print(l1)
print(l2)
print(l3)
print(l4)
print(l5)
print(l6)