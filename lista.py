korok = [20, 34, 78, 83, 90]

def elso_idos(lista):
    i = 0

    while i < len(lista) and not lista[i] > 70:
        i += 1

    van = i < len(lista)
    # nincs = i >= len(lista)

    if van:
        return i
    else:
        return -1

print(elso_idos(korok))
