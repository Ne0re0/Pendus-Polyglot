from random import choice
import os
import string

with open("dictionnaire.txt") as d:
    dictionnaire = d.read().split("\n")

ANSI_RESET = "\u001B[0m"
ANSI_BLACK = "\u001B[30m"
ANSI_RED = "\u001B[31m"
ANSI_GREEN = "\u001B[32m"
ANSI_YELLOW = "\u001B[33m"
ANSI_BLUE = "\u001B[34m"
ANSI_PURPLE = "\u001B[35m"
ANSI_CYAN = "\u001B[36m"
ANSI_WHITE = "\u001B[37m"

def remplacer(motClaire, motCache, lettre):
        valide = False
        for index, car in enumerate(motClaire) :
            if car.upper() == lettre.upper() and motCache[index] == '_':
                if index == 0 :
                    motCache[index] = car.upper()
                else :
                    motCache[index] = car.lower()
                valide = True
        return valide

def banniere():
    print(
"""  ___      __________          __  .__                      ___         
 / _ \_/\  \______   \___.__._/  |_|  |__   ____   ____    / _ \_/\     
 \/ \___/   |     ___<   |  |\   __\  |  \ /  _ \ /    \   \/ \___/     
            |    |    \___  | |  | |   Y  (  <_> )   |  \               
            |____|    / ____| |__| |___|  /\____/|___|  /               
                      \/                \/            \/                
                                                        """, end="")

penduFinal = r"""
--------------
    |        |
    |        |
    |       / \
    |       \_/
    |      __|__
    |        |
    |        |
    |       / \
   /|\     /   \
  / | \
 /  |  \
~~~~~~~~~~~~~~~~~~~~~
"""
penduNumero = r"""
--------------
    |        1
    |        1
    |       2 2
    |       222
    |      55344
    |        3
    |        3
    |       6 7
   /|\     6   7
  / | \
 /  |  \
~~~~~~~~~~~~~~~~~~~~~
"""

def asciiArtPendu(nbErreur, penduFinal = penduFinal, penduNumero = penduNumero):
        for index,element in enumerate(penduNumero) :
            try :
                element = int(element)
                if element > nbErreur :
                    print(" ", end="")
                else :
                    print(penduFinal[index],end="")
            except : 
                print(penduFinal[index],end="")
        
        
        
        
        
if __name__ == '__main__':
    motClaire = choice(dictionnaire)
    while " " in motClaire : 
        motClaire = choice(dictionnaire)
    motCache = ['_' for k in range(len(motClaire))]
 
    nbErreur = 0
    os.system("clear")
    print(ANSI_CYAN)
    banniere()
    print(ANSI_RESET)
    print(' '.join(motCache))
    asciiArtPendu(nbErreur)
    while '_' in motCache and nbErreur < 8 :
        essai = input("Saisissez une lettre : ")
        while len(essai) != 1 or essai.upper() not in string.ascii_uppercase :
            if len(essai) != 1 :
                essai = input("Saisissez " + ANSI_RED + "UNE" + ANSI_RESET + " lettre : ")
            else :
                essai = input("Saisissez une" + ANSI_RED + " LETTRE"+ ANSI_RESET + " : ")
        if not remplacer(motClaire, motCache, essai) :
            nbErreur += 1
        os.system("clear")
        print(ANSI_CYAN)
        banniere()
        print(ANSI_RESET)
        print(' '.join(motCache))
        asciiArtPendu(nbErreur)
        
    if nbErreur >= 8 : 
        print(ANSI_RED + "Raté, le mot était : " + motClaire + ANSI_RESET)
    else :
        
        print(ANSI_GREEN + "Bravo, " +  motClaire + " à été trouvé en " + str(nbErreur) + " erreur(s)" + ANSI_RESET)