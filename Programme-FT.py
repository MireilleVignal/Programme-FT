Personnages = ["Natsu Dragneel","Happy","Elfman","Frosh","Sheria","Juvia"]

Citations = ["Je m'enflamme !","Aye !","C'est un hommes !","Fro pense la même chose.","C'est l'amour.","Grey-sama~"]

import random

def random_item(liste):
    rand_numb=random.randint(0,len(listes)-1)
    item=liste[random.randint]
    return item

def message(personnage,citation):
    return "{} a dit ; {}".format(personnage,citation)

user_answer=input("Tapez entrée si vous voulez une autre citation, ou X pour quitter le programme.")

while user_answer != "X":
    print(message(random_item(Personnages),random_item(Citations)))
    user_answer=input("Tapez entrée si vous voulez une autre citation, ou X pour quitter le programme.")
