from Gombak_oszt import jatekosok

gomba = []


def beolvas(fajlnev):
    fajlom = open(fajlnev, "r", encoding='UTF-8')
    fejlec = fajlom.readline().strip()
    sorok = fajlom.readlines()
    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("@")
        gomba.append(jatekosok(sor))
        i += 1
    fajlom.close()
    print("III/A,B")
    print(f"\tA gombák száma: {gombak_szama()}")
    print("III/C")
    print(f"\tAz első papsapkagomba neve: {gomba[papsapka()].neve}")
    print("III/D")
    print(f"\tA tinóru gombák száma: {tinoru()}")

def gombak_szama():
    i = 0
    db = 0
    while i < len(gomba):
        db += 1
        i +=1
    return db

def papsapka():
    i = 0
    elso = 0
    while i < len(gomba):
        if gomba[i].nemzettseg == "papsapkagombák":
            elso = i
            i = len(gomba)-1
        i += 1
    return elso


def tinoru():
    i = 0
    db_tinoru = 0
    while i < len(gomba):
        if gomba[i].nemzettseg == "tinóru":
            db_tinoru += 1
        i += 1
    return db_tinoru