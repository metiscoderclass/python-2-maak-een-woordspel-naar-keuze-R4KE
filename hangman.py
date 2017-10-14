import time
import math
import random
import os

#Gemaakt door Jurre
#Copyright reserved
#versie 1.2 (ALPHA)


#List met woorden, goedmeldingen en foutmeldingen.
woorden = ["informaticadocent", "technologie", "automerk", "vrachtwagen", "fragment", "boot", "chloorfluorkoolwaterstofverbinding", "huiswerk", "zelfmoordterrorist", "vogel", "leven", "constructie", "toetsenbord", "god", "potlood", "moskee", "kerk", "kapmes", "afairre", "etiquette", "blokje", "religie", "frequentie", "zelfmoord", "audiofragment", "rechtbank", "papier", "wifi", "graden", "leraar", "muziek", "hoi", "beeldscherm", "geweer", "zwaard", "vuurbal", "armoede", "periferie", "soldaat", "galgje", "moordenaar", "verlamdheid", "winkeloverval", "bekeuring", "massamoord", "executie", "militair", "marine", "onthoofding", "marsmannetje", "universum", "vakgebied", "Geneesmiddelenvergoedingssysteem", "Medeverantwoordelijkheidsheffing", "accountantadministratieconsulent", "karaat", "telefoon", "koolstofdioxide", "hexadecimaal",  "installering", "kwadraat", "zeeslag", "pantservoertuig", "laptop", "wiskunde", "banaan", "drol", "computer", "muismat", "bureaublad", "kabouter", "wapenstilstand", "terrorist", "aanslag", "waterstof", "animatie"]
compliment = ["Topper!", "Goed!", "Juist!", "Dat is correct!", "Helemaal top!", "Perfect!", "Mooizo!!", "Goedzo!", "Goed!!!!!", "Helemaal correct!", "Top!", "Scheepsrecht!"]
vernedering = ["Helaas...", "Onjuist!", "Fout!", "JAMMER!", "Jammer...", "Fout en niet goed!", "Slecht!", "Fout...", "Niet goed!", "Niet correct!", "Fout geraden!"]

#Begin scherm
os.system('cls')
time.sleep(0.3)
print(" _____   ___   _      _____    ___  _____")
print("|  __ \ / _ \ | |    |  __ \  |_  ||  ___|")
print("| |  \// /_\ \| |    | |  \/    | || |__ ")
print("| | __ |  _  || |    | | __     | ||  __|")
print("| |_\ \| | | || |____| |_\ \/\__/ /| |___")
print(" \____/\_| |_/\_____/ \____/\____/ \____/")
print("")
time.sleep(0.3)
print("")
print("Regels:")
print("")
time.sleep(1)
print(" • Het doel van het spel is om het juiste woord te raden.")
time.sleep(1)
print(" • Elke beurt moet je steeds een letter opgeven, totdat het woord volledig is.  ")
time.sleep(1)
print(" • Maar... na 5 keer raden, is het spel over. ")
time.sleep(1)
print(" • Als je het woord denkt te weten, type '?'. ")
time.sleep(3)
print("")
print("Klik op enter om het spel te starten.")

Start = input("")
if Start == "":
    print("")


#De game
while True:
    os.system('cls')
    for x in range(0, 10):
        time.sleep(0.03)
        os.system('cls')
        print("  _____   ___   _      _____    ___  _____")
        print("|  __ \ / _ \ | |    |  __ \  |_  ||  ___|")
        print("| |  \// /_\ \| |    | |  \/    | || |__ ")
        print("| | __ |  _  || |    | | __     | ||  __|")
        print("| |_\ \| | | || |____| |_\ \/\__/ /| |___")
        print(" \____/\_| |_/\_____/ \____/\____/ \____/")
        print("")
        time.sleep(0.03)
        os.system('cls')
        print(" _____   ___   _      _____    ___  _____")
        print(" |  __ \ / _ \ | |    |  __ \  |_  ||  ___|")
        print("| |  \// /_\ \| |    | |  \/    | || |__ ")
        print("| | __ |  _  || |    | | __     | ||  __|")
        print("| |_\ \| | | || |____| |_\ \/\__/ /| |___")
        print(" \____/\_| |_/\_____/ \____/\____/ \____/")
        print(" ")
        time.sleep(0.03)
        os.system('cls')
        print(" _____   ___   _      _____    ___  _____")
        print("|  __ \ / _ \ | |    |  __ \  |_  ||  ___|")
        print(" | |  \// /_\ \| |    | |  \/    | || |__ ")
        print("| | __ |  _  || |    | | __     | ||  __|")
        print("| |_\ \| | | || |____| |_\ \/\__/ /| |___")
        print(" \____/\_| |_/\_____/ \____/\____/ \____/")
        print(" ")
        time.sleep(0.03)
        os.system('cls')
        print(" _____   ___   _      _____    ___  _____")
        print("|  __ \ / _ \ | |    |  __ \  |_  ||  ___|")
        print("| |  \// /_\ \| |    | |  \/    | || |__ ")
        print(" | | __ |  _  || |    | | __     | ||  __|")
        print("| |_\ \| | | || |____| |_\ \/\__/ /| |___")
        print(" \____/\_| |_/\_____/ \____/\____/ \____/")
        print(" ")
        time.sleep(0.03)
        os.system('cls')
        print(" _____   ___   _      _____    ___  _____")
        print("|  __ \ / _ \ | |    |  __ \  |_  ||  ___|")
        print("| |  \// /_\ \| |    | |  \/    | || |__ ")
        print("| | __ |  _  || |    | | __     | ||  __|")
        print(" | |_\ \| | | || |____| |_\ \/\__/ /| |___")
        print(" \____/\_| |_/\_____/ \____/\____/ \____/")
        print(" ")
        time.sleep(0.03)
        os.system('cls')
        print(" _____   ___   _      _____    ___  _____")
        print("|  __ \ / _ \ | |    |  __ \  |_  ||  ___|")
        print("| |  \// /_\ \| |    | |  \/    | || |__ ")
        print("| | __ |  _  || |    | | __     | ||  __|")
        print("| |_\ \| | | || |____| |_\ \/\__/ /| |___")
        print("  \____/\_| |_/\_____/ \____/\____/ \____/")
        print(" ")
    woord = random.choice(woorden)
    letters = len(woord)
    streepjes = []
    for i in range(letters):
        streepjes.append("_")
    fout = ""
    goed = ""
    perfect = 0
    foutenteller = 0
    while True:
        correct = random.choice(compliment)
        onjuist = random.choice(vernedering)
        os.system('cls')
        print(" _____   ___   _      _____    ___  _____")
        print("|  __ \ / _ \ | |    |  __ \  |_  ||  ___|")
        print("| |  \// /_\ \| |    | |  \/    | || |__ ")
        print("| | __ |  _  || |    | | __     | ||  __|")
        print("| |_\ \| | | || |____| |_\ \/\__/ /| |___")
        print(" \____/\_| |_/\_____/ \____/\____/ \____/")
        print("")
        print("")
        if foutenteller == 0:
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print("")
            print(" ___")
        if foutenteller == 1:
            print("")
            print("")
            print("")
            print("")
            print("")
            print(" |")
            print(" |")
            print(" |___")
        if foutenteller == 2:
            print("")
            print("")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |___")
        if foutenteller == 3:
            print(" _______")
            print(" |/")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |___")
        if foutenteller == 4:
            print(" _________")
            print(" |/       |")
            print(" |       ( )")
            print(" |")
            print(" |")
            print(" |")
            print(" |")
            print(" |___")
        if foutenteller == 5:
            print(" _________")
            print(" |/       |")
            print(" |       ( )")
            print(" |       -|-")
            print(" |       | |")
            print(" |")
            print(" |")
            print(" |___")
                   
        print("")
        for i in range(letters):
            print(streepjes[i], end=" ")
        print("")
        print("")
        if foutenteller > 0:
            print("Foutgeraden letters: " + fout)
        print("")
        print("Geef een letter.")
        print("")
        reactie = input(" : ")
        print("")
        lettercount = len(reactie)

        #Ifjes die kijken naar wat je hebt ingevuld.
        if lettercount == 1:
            if "?" in reactie:
                os.system('cls')
                print(" _____   ___   _      _____    ___  _____")
                print("|  __ \ / _ \ | |    |  __ \  |_  ||  ___|")
                print("| |  \// /_\ \| |    | |  \/    | || |__ ")
                print("| | __ |  _  || |    | | __     | ||  __|")
                print("| |_\ \| | | || |____| |_\ \/\__/ /| |___")
                print(" \____/\_| |_/\_____/ \____/\____/ \____/")
                print("")
                print("")
                print("")
                print("Raad het woord.")
                print("")
                reactie = input(" : ")
                if reactie == woord:
                    for i in range(5):
                        time.sleep(0.2)
                        os.system('cls')
                        print(" _____  _____  _    _  _____  _   _  _   _  _____  _   _ ")
                        print("|  __ \|  ___|| |  | ||  _  || \ | || \ | ||  ___|| \ | |")
                        print("| |  \/| |__  | |  | || | | ||  \| ||  \| || |__  |  \| |")
                        print("| | __ |  __| | |/\| || | | || . ` || . ` ||  __| | . ` |")
                        print("| |_\ \| |___ \  /\  /\ \_/ /| |\  || |\  || |___ | |\  |")
                        print(" \____/\____/  \/  \/  \___/ \_| \_/\_| \_/\____/ \_| \_/")
                        print("")
                        time.sleep(0.2)
                        os.system('cls')
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                        print("")
                    os.system('cls')
                    print(" _____  _____  _    _  _____  _   _  _   _  _____  _   _ ")
                    print("|  __ \|  ___|| |  | ||  _  || \ | || \ | ||  ___|| \ | |")
                    print("| |  \/| |__  | |  | || | | ||  \| ||  \| || |__  |  \| |")
                    print("| | __ |  __| | |/\| || | | || . ` || . ` ||  __| | . ` |")
                    print("| |_\ \| |___ \  /\  /\ \_/ /| |\  || |\  || |___ | |\  |")
                    print(" \____/\____/  \/  \/  \___/ \_| \_/\_| \_/\____/ \_| \_/")   
                    print("")
                    time.sleep(0.2)
                    print("Het geheime woord was: " + woord)
                    time.sleep(1)
                    print("")
                    print("Klik op enter om opnieuw te spelen!")
                    Nieuw = input("")
                    if Nieuw == "":
                        break
                else:
                    print("")
                    time.sleep(1)
                    print("Helaas... je hebt het woord fout.")
                    time.sleep(1)
            
            elif reactie.isalpha():
                if not reactie in fout and not reactie in goed:
                    if (reactie) in woord:
                        for i in range(letters):
                            if reactie == woord[i]:
                                streepjes[i] = reactie
                                perfect = perfect + 1
                        print("")
                        print(correct)
                        goed = goed + reactie
                        goedteller = len(goed)
                        print("")
                        time.sleep(1)
                        if perfect == letters:
                            for i in range(5):
                                time.sleep(0.2)
                                os.system('cls')
                                print(" _____  _____  _    _  _____  _   _  _   _  _____  _   _ ")
                                print("|  __ \|  ___|| |  | ||  _  || \ | || \ | ||  ___|| \ | |")
                                print("| |  \/| |__  | |  | || | | ||  \| ||  \| || |__  |  \| |")
                                print("| | __ |  __| | |/\| || | | || . ` || . ` ||  __| | . ` |")
                                print("| |_\ \| |___ \  /\  /\ \_/ /| |\  || |\  || |___ | |\  |")
                                print(" \____/\____/  \/  \/  \___/ \_| \_/\_| \_/\____/ \_| \_/")
                                print("")
                                time.sleep(0.2)
                                os.system('cls')
                                print("")
                                print("")
                                print("")
                                print("")
                                print("")
                                print("")
                                print("")
                            os.system('cls')
                            print(" _____  _____  _    _  _____  _   _  _   _  _____  _   _ ")
                            print("|  __ \|  ___|| |  | ||  _  || \ | || \ | ||  ___|| \ | |")
                            print("| |  \/| |__  | |  | || | | ||  \| ||  \| || |__  |  \| |")
                            print("| | __ |  __| | |/\| || | | || . ` || . ` ||  __| | . ` |")
                            print("| |_\ \| |___ \  /\  /\ \_/ /| |\  || |\  || |___ | |\  |")
                            print(" \____/\____/  \/  \/  \___/ \_| \_/\_| \_/\____/ \_| \_/")   
                            print("")
                            time.sleep(0.2)
                            print("Het geheime woord was: " + woord)
                            time.sleep(1)
                            print("")
                            print("Klik op enter om opnieuw te spelen!")
                            Nieuw = input("")
                            if Nieuw == "":
                                break
                    else:
                        print("")
                        print(onjuist)
                        time.sleep(0.3)
                        fout = fout + reactie
                        
                        foutenteller = len(fout)
                        if foutenteller > 4:
                            time.sleep(1)
                            for i in range(5):
                                time.sleep(0.2)
                                os.system('cls')
                                print(" _____   ___  ___  ___ _____   _____  _   _  _____ ______ ")
                                print("|  __ \ / _ \ |  \/  ||  ___| |  _  || | | ||  ___|| ___ ")
                                print("| |  \// /_\ \| .  . || |__   | | | || | | || |__  | |_/ /")
                                print("| | __ |  _  || |\/| ||  __|  | | | || | | ||  __| |    / ")
                                print("| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ /| |___ | |\ \ ")
                                print(" \____/\_| |_/\_|  |_/\____/   \___/  \___/ \____/ \_| \_|")
                                print("")
                                time.sleep(0.2)
                                os.system('cls')
                                print(" _________")
                                print(" |/       |")
                                print(" |       ( )")
                                print(" |       -|-")
                                print(" |       | |")
                                print(" |")
                                print(" |")
                                print(" |___")
                            os.system('cls')
                            print(" _____   ___  ___  ___ _____   _____  _   _  _____ ______ ")
                            print("|  __ \ / _ \ |  \/  ||  ___| |  _  || | | ||  ___|| ___ ")
                            print("| |  \// /_\ \| .  . || |__   | | | || | | || |__  | |_/ /")
                            print("| | __ |  _  || |\/| ||  __|  | | | || | | ||  __| |    / ")
                            print("| |_\ \| | | || |  | || |___  \ \_/ /\ \_/ /| |___ | |\ \ ")
                            print(" \____/\_| |_/\_|  |_/\____/   \___/  \___/ \____/ \_| \_|")
                            print("")
                            time.sleep(0.2)
                            print("Het geheime woord was: " + woord)
                            time.sleep(1)
                            print("")
                            print("Klik op enter om het opnieuw te proberen.")
                            Nieuw = input("")
                            if Nieuw == "":
                                break
                        time.sleep(2)
                else:
                    print("")
                    print("Deze letter heb je al geraden")
                    time.sleep(1)
                    
            else:
                print("Gelieve een geldig teken in te voeren.")
                time.sleep(1)
        else:
            print("Gelieve 1 karakter in te vullen.")
            time.sleep(2)
    
