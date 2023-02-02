def evek(kor):
    i = 0
    while i < 5:
        kora = int(input("Kérem adja meg az egyének korát (0, 120): "))
        kor.append(kora)
        i += 1
    i = 0
    print("II/A, B, C")
    while i < len(kor):
        if i < 4:
            print(f"{kor[i]}", end=":")
        if i == 4:
            print(kor[i])
        i += 1
    return kor


def elso_idos(kor):
    i = 0
    while i < len(kor) and kor[i] < 70:
        i += 1
    return i


def konzol_kiir(kor):
    print("II/D")
    print(f"\tElső idős ember korának helye a listában: {elso_idos(kor)}")

def fajl_kiir(kor):
    f = open("oreg.txt", "a", encoding="utf-8")
    f.write(f"\tElső idős ember korának helye a listában: {elso_idos(kor)}\n")
    f.close()