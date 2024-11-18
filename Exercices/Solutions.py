# -*- coding: utf-8 -*-

#%% Ecrire Hello world
print("Hello Python!")


#%% Ecrire un programme permettant de calculer une vitesse d'un mobile. La distance et le temps parcouru servant à calculer la vitesse sont fournis au clavier. 
temps = int(input("Temps (sec): "))
distance = int(input("Distance (m): "))

print(f"Vitesse = {distance/temps} m/s")


#%% Ecrire un programme qui permute deux variables. Des valeurs pour les variables sont initialement hard-codées dans le programme  
a = 5
b = 6
print(f"a={a} b={b}")
a, b = b, a
print(f"a={a} b={b}")

# ou par une variable interfmédiaire 
a = 5
b = 6
c = a
a = b
b = c
print(f"a={a} b={b}")

#%% Ecrire un programme qui calcule l’aire et le périmètre d’un disque dont le rayon est encodé par l’utilisateur.  
import math
rayon = float(input("Rayon (cm) : "))
print(f"air={rayon**2*math.pi} cm²")
print(f"air={rayon*rayon*math.pi} cm²")




#%% Ecrire un programme qui calcule la pression exercée par une force sur une surface donnée (P=F/S). Les valeurs de la force et de la surface seront encodées par l’utilisateur.
force = float(input("Force : "))
surface = float(input("Surface : "))

print(f"Pression = {force/surface}")


#%% Ecrire un programme qui calcule les racines de l'équation du second degré
import math

# Demander à l'utilisateur d'entrer les coefficients a, b et c
a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

# Calculer le discriminant
discriminant = b**2 - 4*a*c

# Vérifier le signe du discriminant
if discriminant > 0:
    # Deux racines réelles distinctes
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Les racines sont réelles et distinctes : x1 = {x1}, x2 = {x2}")
elif discriminant == 0:
    # Une seule racine réelle
    x1 = -b / (2*a)
    print(f"Il y a une seule racine réelle : x1 = {x1}")
else:
    # Pas de racines réelles (racines complexes)
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
    print("Les racines sont complexes :")
    print(f"x1 = {real_part} + {imaginary_part}i")
    print(f"x2 = {real_part} - {imaginary_part}i")


#%% Ecrire un programme qui construit pour une chaîne de caractères un dictionnaire dont les clés sont les voyelles de la chaîne et les valeurs les fréquences d'apparition de ces voyelles dans la chaîne.  
chaine = "Ecrire un programme qui construit pour une chaîne de caractères un dictionnaire dont les clés sont les voyelles de la chaîne et les valeurs les fréquences d'apparition de ces voyelles dans la chaîne.  "
chaine = chaine.lower()
voyelles = "aeiouy"
dictionnaire = {}

for voyelle in voyelles:
    dictionnaire[voyelle] = chaine.count(voyelle)

print(dictionnaire)


#%% Ecrire un programme qui construit pour une chaîne de caractères un dictionnaire dont les clés sont les voyelles de la chaîne et les valeurs les fréquences d'apparition de ces voyelles dans la chaîne.  
# TENANT COMPTE DES CARACTERES SPECIAUX
chaine = "(âêîôûÿ) Ecrire un programme qui construit pour une chaîne de caractères un dictionnaire dont les clés sont les voyelles de la chaîne et les valeurs les fréquences d'apparition de ces voyelles dans la chaîne. "
chaine = chaine.lower()
voyelles = {
    'a': 'aàáâãäå',
    'e': 'eèéêë',
    'i': 'iìíîï',
    'o': 'oòóôõö',
    'u': 'uùúûü',
    'y': 'yýÿ'
}
dictionnaire = {}

for cle, caracteresAccentue in voyelles.items():
    dictionnaire[cle] = 0
    for voyelle in caracteresAccentue:
        dictionnaire[cle] += chaine.count(voyelle)

print(dictionnaire)


#%% Ecrire un script qui détermine si une séquence de caractères entrée par l’utilisateur est une séquence ADN valide (contient uniquement les caractères ACTG)
chaine = input("Entrer une chaine ADN :")
chaine = chaine.upper()
adn = "ACTG"
isvalid = True

for c in chaine: 
    if c not in adn:
        isvalid = False
        break

if isvalid:
    print(f"La chaine adn {chaine} est valide")
else:
    print(f"La chaine adn {chaine} n'est pas valide")


#%% Dans cet exercice, vous devez récupérer différents morceaux d'une liste grâce aux slices. 
liste=["Maxime","Martine","Christopher","Carlos","Michael","Eric"]

#Les trois premiers employés ("Maxime", "Martine" et "Christopher") dans une liste trois_premiers    
print(liste[0:4])

#Les trois derniers employés ("Carlos", "Michael" et "Eric") dans une liste trois_derniers    
print(liste[-3:])

#Tous les employés sauf le premier et le dernier dans une liste   
print(liste[1:-1])

#Le premier et le dernier employé dans une liste premier_dernier   
print(liste[0::len(liste)-1])


#%% Dans cet exercice, vous allez devoir récupérer des informations à l'intérieur de listes imbriquées.
#Vous devez récupérer dans les variables python, deux et sept, respectivement la chaîne de caractères 'Python' contenue dans la liste langages et les nombres 2 et 7 ; contenus dans la liste nombres. 
langages = [["Python", "C++"], "Java"]
print(langages[0][0])

nombres = [1, [4, [2, 3]], 5, [6], [[7]]]
print(nombres[1][1][0])
print(nombres[4][0][0])


#%% Ecrire un programme qui affiche les entiers pairs entre 0 et 20 compris  
for i in range(0,21,2):
    print(i)

print([*range(0,21,2)])


#%% Ecrire un programme qui construit pour une chaîne de caractères un dictionnaire dont les clés sont les mots de la chaîne et les valeurs les fréquences de ces mots dans la chaîne. La chaîne de caractères est entrée par l’utilisateur.
chaine = "Ecrire un programme qui construit pour une chaîne de caractères un dictionnaire dont les clés sont les mots de la chaîne et les valeurs les fréquences de ces mots dans la chaîne. La chaîne de caractères est entrée par l’utilisateur."
mots = chaine.split(" ")

dic = {}
for mot in mots:
    if mot not in dic:
        dic[mot] = 1
    else:
        dic[mot] += 1

print(dic)


#%% Ecrire un programme qui recherche la racine d'une fonction dans un intervalle [a,b] par la méthode de la dichotomie
def f(x):
    # Définissez votre fonction ici, par exemple : f(x) = x^3 - 4x^2 + 5x - 2
    return x**3 - 4*x**2 + 5*x - 2

def dichotomie(a, b, tolérance):
    if f(a) * f(b) >= 0:
        print("La méthode de la dichotomie ne peut pas être appliquée dans cet intervalle.")
        return None

    while (b - a) / 2.0 > tolérance:
        midpoint = (a + b) / 2.0
        print(f"Milieu : {midpoint}")
        if f(midpoint) == 0:
            return midpoint
        elif f(a) * f(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

    return (a + b) / 2.0

# Définissez l'intervalle [a, b] et la tolérance
a = 0.0
b = 7.5
tolérance = 1e-6

racine = dichotomie(a, b, tolérance)

if racine is not None:
    print(f"Une approximation de la racine est : {racine:.6f}")
else:
    print("La méthode de la dichotomie n'a pas pu trouver une racine dans cet intervalle.")


#%% Ecrire un script qui détermine si une séquence de caractères entrée par l’utilisateur est une séquence ADN valide (contient uniquement les caractères ACTG). Une fonction sera créée, elle validera ou non la chaine de caractères passés en paramètre.  
def est_sequence_adn_valide(sequence):
    caractères_valides = "ACTG"
    sequence = sequence.upper()

    for caractère in sequence:
        if caractère not in caractères_valides:
            return False  # Si un caractère invalide est trouvé, retourner False
    return True  # Si tous les caractères sont valides, retourner True

adn_sample = ["AAATTTGGGGGCCCCC", "CCCTTTTGGGG", "ABC"]
for sequence in adn_sample:
    if est_sequence_adn_valide(sequence):
        print(f"{sequence} est valide")
    else:
        print(f"{sequence} est non valide")


#%% Ecrire un programme qui calcule les racines de l'équation du second degré, en utilisant une fonction, la fonction retourne les racines  
import math

def calculer_racines(a, b, c):
    # Calculer le discriminant
    discriminant = b**2 - 4*a*c

    # Vérifier le signe du discriminant
    if discriminant > 0:
        # Deux racines réelles distinctes
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        # Une seule racine réelle
        x1 = -b / (2*a)
        return x1,
    else:
        # Pas de racines réelles (racines complexes)
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
        x1 = complex(real_part, imaginary_part)
        x2 = complex(real_part, -imaginary_part)
        return x1, x2

# Demander à l'utilisateur d'entrer les coefficients a, b et c
a = float(input("Entrez le coefficient a : "))
b = float(input("Entrez le coefficient b : "))
c = float(input("Entrez le coefficient c : "))

racines = calculer_racines(a, b, c)

if len(racines) == 2:
    print(f"Les racines sont réelles et distinctes : x1 = {racines[0]}, x2 = {racines[1]}")
elif len(racines) == 1:
    print(f"Il y a une seule racine réelle : x1 = {racines[0]}")
else:
    print(f"Les racines sont complexes : x1 = {racines[0]}, x2 = {racines[1]}")


#%% Convertir et afficher le vecteur suivant en entier ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] en utilisant les arrays numpy. 
import numpy as np
ar = np.array(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
print(ar.astype(int))


#%% A partir du np.array suivant : np.random.rand(6,7)*100, afficher la matrice, la moyenne, médiane de la matrice et la valeur maximum et minimum de la troisième ligne. 
import numpy as np
ar = np.array(np.random.rand(6,7)*100)
print(ar)
print(f"moyenne : {ar.mean()}")
print(f"medianne : {np.median(ar)}")
print(ar[2])
print(f"Maximum : {ar[2].max()}")
print(f"Minimum : {ar[2].min()}")


#%% A partir du np.array suivant : np.random.rand(6,7)*100, filtrer et afficher les éléments  > 90, avec where et l’interprétation du résultat 
import numpy as np
ar = np.array(np.random.rand(6,7)*100)
res = np.where(ar > 90)
print(res)
print(f"Nombre d'élément : {len(res[0])}")
for i in range(len(res[0])):
    print(f"Elément {ar[res[0][i],res[1][i]]} situé aux indices {res[0][i]}:{res[1][i]}")


#%% Créer un dataframe avec les données suivantes
import pandas as pd
exam_data  = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'], 
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19], 
    'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1], 
    'qualify': ['yes', 'no', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'no', 'yes']
    } 

labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'] 

df = pd.DataFrame(exam_data)
#Sélectionner les colonnes suivantes : « name et score » 
print(df[["name", "score"]])

#Sélectionner les colonnes suivantes par leur indice : 0 et 1 
print(df.iloc[:, [0,1]])

#Sélectionner les lignes pour lesquelles « qualify » = « yes » 
print(df.query("qualify == 'yes'"))

#Sélectionner les lignes pour lesquelles « score » est « nan » 
print(df.query("score.isnull()"))
print(df.query("score != score"))

#Sélectionner les lignes pour lesquelles « score » est entre 15 et 20 
print(df.query("score > 15 and score < 20"))

#Sélectionner les lignes pour lesquelles « attemps < 2 & score > 15 » 
print(df.query("attempts < 2 and score < 15"))

#Afficher la somme de « attempts » et la moyenne des « scores » 
print(f"Somme des tentatives : {df['attempts'].sum()}")
print(f"Moyenne des score : {df['score'].mean()}")

#Grouper les lignes par la colonne « qualify » et afficher le nombre de ligne  
grp = df.groupby(by="qualify")["qualify"].count()
print(grp)


#%% Ecrire une fonction dans un script qui écrit des donnés aléatoires dans un fichier CSV sous le format suivant : 
import random
from datetime import datetime

def writeHeader(filename, headers):
    header = ",".join(headers)
    file = open(filename, "w")
    file.write(header + "\n")
    file.close()
        
def appendData(filename, data):
    line = ",".join(data)
    file = open(filename, "a")
    file.write(line + "\n")
    file.close()

writeHeader("data.csv", ["date", "value"])
for i in range(5):
    appendData("data.csv", [datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f"), str(random.uniform(50,100))])


#%% Ecrire une fonction dans un script qui crée un dataframe avec les mêmes données aléatoires que l’exercice précédent et l’écrit dans un fichier CSV avec Pandas 
import pandas as pd

def createDataframe(headers):
    dic = {}
    for header in headers:
        dic[header] = []
    return pd.DataFrame(dic)

def addData(df, data):
    df.loc[len(df.index)] = data

df = createDataframe(["date", "value"])
for i in range(5):
    addData(df, [datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f"), random.uniform(50,100)])

df.to_csv("data.csv", header=True, index=False)


#%% Sur base du fichier CSV précédent, écrire une fonction qui afficher une courbe orange avec MatplotLib 
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")
df["date"] = pd.to_datetime(df.date) 
df = df.set_index("date")
df.plot()
plt.show()

fig, ax = plt.subplots(figsize=(5,5))
plt.plot(df, color="orange")
plt.show()


#%% Ajouter une colonne de données aléatoire dans le dataframe et faites apparaitre une seconde courbe dans matplotlib 
import pandas as pd

def createDataframe(headers):
    dic = {}
    for header in headers:
        dic[header] = []
    return pd.DataFrame(dic)

def addData(df, data):
    df.loc[len(df.index)] = data

df = createDataframe(["date", "value1", "value2"])
for i in range(50):
    addData(df, [datetime.now().strftime("%m/%d/%Y %H:%M:%S.%f"), random.uniform(50,100), random.uniform(200,250)])

df.to_csv("data.csv", header=True, index=False)

fig, ax = plt.subplots(figsize=(5,5))
plt.plot(df["value1"], color="red")
plt.plot(df["value2"], color="green")
plt.show()


#%% Mars Lander 
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)


    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    if abs(v_speed) > 30:
        print("0 4")
    else:
        print("0 0")


#%% Thor
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    print(f"light(x,y) = ({light_x},{light_y})", file=sys.stderr, flush=True)
    print(f"Thor(x,y) = ({initial_tx},{initial_ty})", file=sys.stderr, flush=True)
    print(f"remaining_turns = {remaining_turns}", file=sys.stderr, flush=True)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    delta_x = abs(light_x - initial_tx)
    delta_y = abs(light_y - initial_ty)

    cosine = math.atan2(light_y - initial_ty, light_x - initial_tx) * 180 / math.pi
    print(f"cosine = {cosine}", file=sys.stderr, flush=True)


    if cosine>=-22.5 and cosine<=22.5:
        print("E")
        initial_tx += 1
        initial_ty += 0
    elif cosine>=22.5 and cosine<=67.5:
        print("SE")
        initial_tx += 1
        initial_ty += 1
    elif cosine>=67.5 and cosine<=112.5:
        print("S")
        initial_tx += 0
        initial_ty += 1
    elif cosine>=112.5 and cosine<=157.5:
        print("SW") 
        initial_tx -= 1
        initial_ty += 1
    elif cosine>=157.5:
        print("W")
        initial_tx -= 1
        initial_ty += 0
    elif cosine<=-22.5 and cosine>=-67.5:
        print("NE")
        initial_tx += 1
        initial_ty -= 1
    elif cosine<=-67.5 and cosine>=-112.5:
        print("N")
        initial_tx += 0
        initial_ty -= 1
    elif cosine<=-112.5 and cosine>=-157.5:
        print("NW") 
        initial_tx -= 1
        initial_ty -= 1
    elif cosine<=-157.5:
        print("W")
        initial_tx -= 1
        initial_ty += 0


#%% The Descent
import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    montains = []
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain.
        montains.append(mountain_h)

    hi = montains.index(max(montains))
    # The index of the mountain to fire on.
    print(hi)


#%% Batman
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
minx = 0
miny = 0
maxx = w-1
maxy = h-1
x = x0
y = y0
print(f"x0:{x0}  y0:{y0}", file=sys.stderr, flush=True)
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(f"{bomb_dir} x:{minx}:{maxx}  y:{miny}:{maxy}", file=sys.stderr, flush=True)
    if bomb_dir == "U":
        maxy = y - 1 
    elif bomb_dir == "UR":
        maxy = y - 1 
        minx = x + 1
    elif bomb_dir == "R":
        minx = x + 1
    elif bomb_dir == "DR":
        minx = x + 1
        miny = y + 1
    elif bomb_dir == "D":
        miny = y + 1
    elif bomb_dir == "DL":
        miny = y + 1
        maxx = x - 1
    elif bomb_dir == "L":
        maxx = x - 1
    elif bomb_dir == "UL":
        maxy = y - 1
        maxx = x - 1 

    print(f"{bomb_dir} x:{minx}:{maxx}  y:{miny}:{maxy}", file=sys.stderr, flush=True)
    x = int(round(minx + (maxx-minx)/2,0))
    y = int(round(miny + (maxy-miny)/2,0))
    # the location of the next window Batman should jump to.
    print(f"{x} {y}")



