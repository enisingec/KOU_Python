def suzgec(x):
    liste = []
    for i in x:
        if not i.isdigit() and i.isalpha() :
            liste.append(i)
    liste = ''.join(liste)
    return liste

file = open("odev.txt", "r", encoding="utf-8")

liste_2 = []
for x in file:
    filtreli = suzgec(x)
    liste_2.append(filtreli)

file_2 = open('odev.txt', "w", encoding="utf-8")

for i in liste_2:
    file_2.write(i + "\n")