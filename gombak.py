from Gombak_oszt import jatekosok

gomba = []


def beolvas(fajlnev, gomba):
    fajlom = open(fajlnev, "r", encoding='UTF-8')
    fejlec = fajlom.readline().strip()
    sorok = fajlom.readlines()
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("@")
        gomba.append(jatekosok(sor))
        i += 1
    fajlom.close()

    return gomba

def gombak_szama(gomba):
    i = 0
    db = 0
    while i < len(gomba):
        db += 1
        i +=1
    print("III/A,B")
    print(f"\tA gombák száma: {db}")

def papsapka(gomba):
    i = 0
    elso = 0
    while i < len(gomba):
        if gomba[i].nemzettseg == "papsapkagombák":
            elso = i
            i = len(gomba)-1
        i += 1
    print("III/C")
    print(f"\tAz első papsapkagomba neve: {gomba[elso].neve}")



def tinoru(gomba):
    i = 0
    db_tinoru = 0
    while i < len(gomba):
        if gomba[i].nemzettseg == "tinóru":
            db_tinoru += 1
        i += 1
    print("III/D")
    print(f"\tA tinóru gombák száma: {db_tinoru}")