import os
import sys
#retourne l'alphabet obtenu à partir d'une lettre
def alphabet(c):
    dico = ""
    for i in range(ord(c),91,1):
        dico+=chr(i)
        if i == 90:
            i=65
            for i in range(i,ord(c),1):
                dico+=chr(i)
    return dico

#fonction qui crypte le message
def crypter(texte,cle,alphabets):
    messageCrypte=""
    alphabetNormal ={chr(i+65):i for i in range(0,26)} # associer à chaque lettre de l'alphabet sa position
    for i in range(0,len(texte),1):
        particuliers =[" ","\n","'"]
        if texte[i] in particuliers:
            messageCrypte+=texte[i]
        else:
            messageCrypte+=alphabets[i%len(cle)][alphabetNormal[texte[i]]]
    return messageCrypte
        

choix = sys.argv[1]

if choix == '1':  
    cle = sys.argv[3].upper() #recupperer la cle

    #trouver pour chaque lettre  de la cle l'alphabet correspondant et les stocker dans une liste
    alphabets = []
    for i in range(len(cle)):
        alphabets.append(alphabet(cle[i]))

    texte = sys.argv[2].upper() #recupperer le message en clair
    print("LE MESSAGE CHIFFRE EST:",crypter(texte,cle,alphabets))
    
if choix == '2':
    cle = sys.argv[3].upper() #recupperer la cle
    chemin = sys.argv[2].lower() #recupperer le chemin

    #trouver pour chaque lettre  de la cle l'alphabet correspondant et les stocker dans une liste
    alphabets = []
    for i in range(len(cle)):
        alphabets.append(alphabet(cle[i]))
    
    fichier = open(chemin,"r")
    lignes = fichier.readlines()
    crypte = []
    for ligne in lignes:
        crypte.append(crypter(ligne.upper(),cle,alphabets))
    fichier.close()

    fichierCrypte = open("chiffre_"+chemin,'w')
    fichierCrypte.writelines(crypte)
    fichierCrypte.close()  
    print("crypte avec succes")

os.system("pause")






