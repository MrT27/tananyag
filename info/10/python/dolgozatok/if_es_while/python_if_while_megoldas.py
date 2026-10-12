# Python dolgozat – Elágazások és while ciklus – Megoldás
# 10. évfolyam | 45 perc | 20 pont

# ==================================================
# 1. feladat – Egy szám vizsgálata – 3 pont
# ==================================================
# Kérj be egy egész számot!
# Írd ki, hogy a szám pozitív, negatív vagy nulla!
# ==================================================

szam = int(input("Adj meg egy egész számot: "))

if szam > 0:
    print("Pozitív.")
elif szam < 0:
    print("Negatív.")
else:
    print("Nulla.")


# ==================================================
# 2. feladat – Kedvezményes vásárlás – 3 pont
# ==================================================
# Kérd be egy vásárlás összegét egész forintban!
# Ha az összeg legalább 10 000 Ft, a vásárló 10% kedvezményt kap.
# Egyébként nem jár kedvezmény.
# Írd ki a fizetendő összeget!
#
# Példák:
# 12 000 Ft-os vásárlás esetén a fizetendő összeg 10 800 Ft.
# 8 000 Ft-os vásárlás esetén a fizetendő összeg 8 000 Ft.
# ==================================================

osszeg = int(input("Add meg a vásárlás összegét egész forintban: "))

if osszeg >= 10000:
    fizetendo = osszeg * 0.9
else:
    fizetendo = osszeg

print("A fizetendő összeg:", fizetendo, "Ft")


# ==================================================
# 3. feladat – Visszaszámlálás – 4 pont
# ==================================================
# Kérj be egy pozitív egész számot!
# While ciklussal írd ki a számokat a megadott számtól 1-ig,
# csökkenő sorrendben, mindegyiket külön sorba!
# A visszaszámlálás után írd ki: Indulás!
#
# Például, ha a megadott szám 3:
# 3
# 2
# 1
# Indulás!
# ==================================================

szam = int(input("Adj meg egy pozitív egész számot: "))

while szam >= 1:
    print(szam)
    szam = szam - 1

print("Indulás!")


# ==================================================
# 4. feladat – Megfelelő szám bekérése – 4 pont
# ==================================================
# Kérj be egy egész számot!
# Ha a szám kisebb mint 1 vagy nagyobb mint 10, írd ki:
# Hibás érték!
# Ezután kérj be új számot!
# A bekérést addig ismételd, amíg 1 és 10 közötti számot nem kapsz.
# Az 1 és a 10 is elfogadható.
# Az első megfelelő szám megadásakor a ciklus álljon le,
# és ne kérj be több számot!
# A ciklus után írd ki: Elfogadott szám:
# majd a szám értékét!
#
# Példa:
# Adj meg egy számot: 15
# Hibás érték!
# Adj meg egy számot: -2
# Hibás érték!
# Adj meg egy számot: 7
# Elfogadott szám: 7
# ==================================================

szam = int(input("Adj meg egy számot: "))

while szam < 1 or szam > 10:
    print("Hibás érték!")
    szam = int(input("Adj meg egy számot: "))

print("Elfogadott szám:", szam)


# ==================================================
# 5. feladat – Páros számok számlálása – 6 pont
# ==================================================
# Kérj be egész számokat egymás után!
# Az adatbekérés addig tartson, amíg a felhasználó 0-t nem ír be.
# A program számolja meg, hogy a megadott számok közül hány volt páros!
# A lezáró 0-t ne számold bele!
# A végén írd ki a páros számok darabszámát!
# Ha az első megadott szám 0, az eredmény 0.
#
# Példa:
# Adj meg egy számot: 5
# Adj meg egy számot: 8
# Adj meg egy számot: -4
# Adj meg egy számot: 7
# Adj meg egy számot: 0
# A páros számok darabszáma: 2
# ==================================================

paros_db = 0
szam = int(input("Adj meg egy számot: "))

while szam != 0:
    if szam % 2 == 0:
        paros_db = paros_db + 1
    szam = int(input("Adj meg egy számot: "))

print("A páros számok darabszáma:", paros_db)


