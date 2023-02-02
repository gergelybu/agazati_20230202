import random

def rszam():
    szam = random.randint(1,50)
    print("I/A")
    print(f"\tA generált szám: {szam}")
    print("I/B")
    if szam % 5 == 0 and szam % 3 == 0:
        print("\tA szám öttel és hárommal is osztható!")
    elif szam % 5 == 0:
        print("\tA szám öttel osztható!")
    elif szam % 3 ==0:
        print("\tA szám hárommal osztható!")
    else:
        print("\tA szám nem osztható se hárommal, se öttel!")