import ApiCall
import AudioTrimmer
import csv
import os
Voix = []

dossier = r"temp"

for fichier in os.listdir(dossier):
    chemin_fichier = os.path.join(dossier, fichier)
    if os.path.isfile(chemin_fichier):
        os.remove(chemin_fichier)
        
print("⚠ Tous les fichiers temporaires ont été supprimés ! ⚠")

def Menu():
    print("""
          ----- Acapela Box CRACKED -----
          1) Choisir la voix
          2) Choisir le texte
          -------------------------------
          """)
    
    select = input("Selection : ")
    
    if select == "1":
        choixVoix()
        return None
    if select == "2":
        Texte()
        return None
    else:
        print("Choix invalide")
        Menu()
        return None
    
def choixVoix():
    global Voix
    listeVoix = []
    
    with open("voix.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for i in reader:
            listeVoix.append(i)
        f.close()
        
    print("Voix disponibles : ")
    
    for i in listeVoix:
        print(i[0])
    
    voice = input("Quel est la voix que tu vas choisir ? : ")
    
    for i in listeVoix:
        if i[0] == voice:
            Voix = i
            print(f"Voix sélectionnée : {i[0]} | Retour au menu...")
            Menu()
            return None
    
    print("voix invalide !")
    choixVoix()
    return None

def Texte():
    if len(Voix) == 0:
        print("Il faut choisir une voix avant d'écrire quelque chose !")
        Menu()
        return None
    
    texte = input("Qu'est ce que tu veux faire dire à la voix : ")
    
    if texte == "":
        print("Retour au menu")
        Menu()
        return None
    
    tempAudio = ApiCall.GetVoix(texte, voix=Voix[1])
    couper = None
    try:
        couper = AudioTrimmer.TrimAudio(tempAudio)
    except FileNotFoundError:
        print("Erreur : Le fichier n'est probablement pas ici.")
    else:
        print("Succès !")
        os.startfile(couper)
    Texte()
    
    
Menu()