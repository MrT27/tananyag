# ==================================================
# Felkészülés a dolgozatra – Elágazások és while ciklus
# 10. évfolyam | Gyakorlóóra: 45 perc
# ==================================================
# Megoldások
# A megoldásokat a feladatleírások alá írd!
# A ciklusos feladatokat while ciklussal oldd meg!
# Feltételezheted, hogy a felhasználó a megadott típusú adatot írja be.
# Futtasd a programokat a feladatoknál megadott próbaadatokkal is!
# ==================================================

# ==================================================
# 1. feladat – Hőmérséklet vizsgálata
# ==================================================
# Kérj be egy egész számmal megadott hőmérsékletet!
# Ha a hőmérséklet 0 alatt van, írd ki: Fagy!
# Ha pontosan 0, írd ki: Fagypont!
# Ha 0 felett van, írd ki: Fagypont felett!
#
# Próbáld ki ezekkel az értékekkel: -5, 0, 12.
# ==================================================

homerseklet = int(input("Add meg a hőmérsékletet: "))

if homerseklet < 0:
    print("Fagy!")
elif homerseklet == 0:
    print("Fagypont!")
else:
    print("Fagypont felett!")


# ==================================================
# 2. feladat – Szállítási díj
# ==================================================
# Kérd be egy rendelés összegét egész forintban!
# Ha a rendelés összege legalább 15 000 Ft, a szállítás ingyenes.
# Egyébként a szállítás díja 1 500 Ft.
# Írd ki a szállítással együtt fizetendő teljes összeget!
#
# Példák:
# 12 000 Ft-os rendelés esetén a fizetendő összeg 13 500 Ft.
# 15 000 Ft-os rendelés esetén a fizetendő összeg 15 000 Ft.
# Próbáld ki 20 000 Ft-tal is!
# ==================================================

osszeg = int(input("Add meg a rendelés összegét egész forintban: "))

if osszeg >= 15000:
    fizetendo = osszeg
else:
    fizetendo = osszeg + 1500

print("A fizetendő összeg:", fizetendo, "Ft")


# ==================================================
# 3. feladat – Számolás felfelé
# ==================================================
# Kérj be egy pozitív egész számot!
# While ciklussal írd ki a számokat 1-től a megadott számig,
# a megadott számot is beleértve, mindegyiket külön sorba!
# A ciklus után írd ki: Kész!
#
# Például, ha a megadott szám 4:
# 1
# 2
# 3
# 4
# Kész!
# Próbáld ki az 1-et is!
# ==================================================

felso_hatar = int(input("Adj meg egy pozitív egész számot: "))
szam = 1

while szam <= felso_hatar:
    print(szam)
    szam = szam + 1

print("Kész!")


# ==================================================
# 4. feladat – Megfelelő életkor bekérése
# ==================================================
# Kérj be egy egész számmal megadott életkort!
# A program 14 és 18 közötti életkort fogadjon el.
# A 14 és a 18 is elfogadható.
# Ha a megadott életkor kisebb mint 14 vagy nagyobb mint 18,
# írd ki: Hibás életkor!
# Ezután kérj be új életkort!
# A bekérést addig ismételd, amíg megfelelő életkort nem kapsz!
# Az első megfelelő életkor megadásakor a ciklus álljon le,
# és ne kérj be több adatot!
# A ciklus után írd ki: Elfogadott életkor:
# majd az életkor értékét!
#
# Példa:
# Add meg az életkort: 12
# Hibás életkor!
# Add meg az életkort: 20
# Hibás életkor!
# Add meg az életkort: 16
# Elfogadott életkor: 16
# Próbáld ki úgy is, hogy az első megadott életkor 14 vagy 18!
# ==================================================

eletkor = int(input("Add meg az életkort: "))

while eletkor < 14 or eletkor > 18:
    print("Hibás életkor!")
    eletkor = int(input("Add meg az életkort: "))

print("Elfogadott életkor:", eletkor)


# ==================================================
# 5. feladat – Pozitív számok számlálása
# ==================================================
# Kérj be egész számokat egymás után!
# Az adatbekérés addig tartson, amíg a felhasználó 0-t nem ír be!
# Számold meg, hány pozitív számot adott meg!
# A negatív számokat és a lezáró 0-t ne számold bele!
# A végén írd ki a pozitív számok darabszámát!
# Ha az első megadott szám 0, az eredmény 0.
#
# Példa:
# Adj meg egy számot: 5
# Adj meg egy számot: -8
# Adj meg egy számot: 4
# Adj meg egy számot: -7
# Adj meg egy számot: 0
# A pozitív számok darabszáma: 2
# Próbáld ki csak negatív számokkal, majd lezáró 0-val is!
# ==================================================

pozitiv_db = 0
szam = int(input("Adj meg egy számot: "))

while szam != 0:
    if szam > 0:
        pozitiv_db = pozitiv_db + 1
    szam = int(input("Adj meg egy számot: "))

print("A pozitív számok darabszáma:", pozitiv_db)


