kor = []

def evek():
    i = 0
    while i < 5:
        kora = int(input("Kérem adja meg az egyének korát (0, 120): "))
        kor.append(kora)
        i += 1
    i = 0
    print("II/A, B, C")
    while i < len(kor):
        if i < 4:
            print(f"\t{kor[i]}", end=":")
        if i == 4:
            print(kor[i])
        i += 1
    print("II/D")
    print(f"\tElső idős ember korának helye a listában: {elso_idos()}")
    f = open("oreg.txt", "a", encoding="utf-8")
    f.write(f"\tElső idős ember korának helye a listában: {elso_idos()}\n")
    f.close()


def elso_idos():
    i = 0
    legidosebb = 0
    while i < len(kor):
        if kor[i] > 70:
            legidosebb = i
            i = len(kor)-1
        i+=1
    return legidosebb