# 9. évfolyam – Programozási alapok

## Tanári projektleírás és fejlesztési irányelvek

**Tanév:** 2026/2027  
**Csoport:** 9TC szakm 2  
**Tanár:** Ungi Tamás  
**Heti óraszám:** 2  
**Alapdokumentum:** `Célok/Tanmenet.xlsx`

## 1. A dokumentum célja

Ez a fájl a 9. évfolyamos Programozási alapok tantárgy digitális tananyagának állandó tanári iránytűje. A fejlesztés folytatásakor először ezt és a tanmenetet kell áttekinteni. A dokumentum rögzíti a tantárgy célját, a tananyag felépítését, a módszertani döntéseket, az elkészült részeket és a következő fejlesztési lépéseket.

Nem diáktananyag, hanem belső tanári projektleírás. Minden jelentős tananyagbővítés után frissítendő.

## 2. A tantárgy átfogó célja

A tanulók gyakorlati, sikerélményre épülő feladatokon keresztül ismerjék meg a programozás és a webfejlesztés alapjait. Az év végére legyenek képesek:

- egyszerű algoritmusok megértésére és vizuális programozási környezetben történő megvalósítására;
- eseményvezérelt programok és egyszerű mobilalkalmazások készítésére;
- alapvető hardverközeli programozási feladatok elvégzésére;
- szabályos, többoldalas HTML-webhely létrehozására;
- a tartalom és a megjelenés elkülönítésére HTML és CSS használatával;
- egyszerű reszponzív oldal készítésére, majd Bootstrap-alapú felület összeállítására;
- a Git és a GitHub alapvető, biztonságos használatára;
- a böngésző fejlesztőeszközeinek és a HTML-validálásnak az alkalmazására;
- egy rövid JavaScript-program weboldalba illesztésére;
- munkájuk önálló ellenőrzésére, bemutatására és dokumentálására.

A cél nem a tagek és parancsok bemagoltatása, hanem annak megértése, hogy az egyes eszközök milyen problémát oldanak meg.

### Kiemelt eredményességi cél: sikeres ICDL Webszerkesztés vizsga

A tananyag fejlesztésének egyik elsődleges oka, hogy a korábbi tanévben a HTML-t tanuló kilencedikesek egy része nem tudott sikeres ICDL Webszerkesztés vizsgát tenni. Ez a 2026/2027-es tanévben nem ismétlődhet meg. A tananyag akkor tekinthető eredményesnek, ha a tanulók nemcsak ismerik a HTML-elemeket, hanem időkorlát mellett, segédeszköz nélkül is képesek egy hivatalos mintát követő vizsgafeladat önálló megoldására.

A 2026. október 30-án ellenőrzött hivatalos magyar ICDL-tájékoztató szerint a Webszerkesztés vizsga:

- manuális, 45 perces vizsga;
- előre elkészített munkafájlokra épül;
- 6 elméleti feleletválasztós kérdést és 15 gyakorlati részfeladatot tartalmaz;
- összesen 36 pontos;
- legalább 27 pont, vagyis 75% szükséges a sikerhez;
- segédeszköz nélkül teljesítendő.

Ezek ezért a tananyag kötelező tervezési paraméterei. Nem elegendő általános weboldalprojekteket készíteni: rendszeresen kell rövid, kötött utasításokat követő, munkafájlokból induló és időre végzett feladatokat is gyakorolni.

### ICDL-felkészültségi ellenőrzőpontok

1. **HTML-alapok után:** 45 perces alapszintű próba, amely méri a fájlkezelést, dokumentumszerkezetet, szövegelemeket, hivatkozásokat, képeket és listákat.
2. **Táblázatok és validálás után:** hivatalos felépítéshez közelítő részpróba, elméleti kérdésekkel és biztosított munkafájlokkal.
3. **CSS-alapok után:** HTML- és CSS-formázási feladat időre, javítókulccsal és részpontozással.
4. **Bootstrap előtt vagy annak elején:** teljes, 45 perces ICDL-próbavizsga.
5. **A tényleges vizsga előtt:** legalább két különböző teljes próbavizsga. Vizsgára az a tanuló tekinthető felkészültnek, aki legalább két alkalommal eléri a 27/36 pontot, és legalább egyszer 30 pontot vagy többet szerez.

Minden próbavizsga után feladattípusonként kell rögzíteni a hibákat. A gyenge területekhez célzott javítógyakorlat tartozik; az összpontszám önmagában nem elegendő visszajelzés.

## 3. Az éves tanmenet fő blokkjai

| Órák | Tanmeneti blokk | Fejlesztési cél |
|---:|---|---|
| 1–8. | Scratch és programozási alapok | Felület, események, mozgás, rajzolás, saját ötlet |
| 9–12. | Mobilalkalmazás-fejlesztés | Felület, eseménykezelés, saját alkalmazás |
| 13–20. | Robotika és jelenségalapú hét | Motorok, közlekedés, páros projekt |
| 21–24. | Ismétlés és számonkérés | Az első félévi alapok rendszerezése |
| 25–40. | HTML | Dokumentumszerkezet, szöveg, képek, linkek, listák, táblázatok, validálás, DevTools |
| 41–44. | Git és együttműködés | Helyi verziókezelés, GitHub, online csoportmunka |
| 45–60. | CSS és reszponzivitás | Szelektorok, dobozmodell, elrendezés, mértékegységek, media query |
| 61–68. | Bootstrap és űrlapok | Rácsrendszer, komponensek, reszponzív felület, számonkérés |
| 69–70. | JavaScript-bevezetés | Szerep, beágyazás, külső fájl, első program |
| 71–72. | Év végi összefoglalás | Rendszerezés és lezárás |

Az MI-tananyag külön, heti 0,5 órás tanmenet szerint fut. Kapcsolódhat a projektekhez, a forráskritikához, a dokumentáláshoz és a jelenségalapú héthez, de nem helyettesíti a programozási alapkészségek önálló elsajátítását.

## 4. A digitális tananyag jelenlegi szerkezete

### Scratch

Elkészült öt egység: alapok, mozgás és animáció, egyszerű játékok, Kajak projekt, Gyümölcstál számonkérés.

### Mobilalkalmazás-fejlesztés

A tényleges tananyag Thunkable-re épül. Tíz egység található a mappában az üdvözlő alkalmazástól a BMI-kalkulátoros számonkérésig.

### Robotika

Jelenleg egy micro:bit/MakeCode alapozó anyag érhető el. A tanmenetben szereplő LEGO-robot, motorhasználat és páros robotprojekt nincs még teljesen lefedve.

### HTML

Az elkészült tananyag:

1. A web működése és a HTML szerepe
2. Az első HTML-oldal elkészítése
3. Címsorok és címsorhierarchia
4. Bekezdések, szóközök és sortörések
5. Jelentéssel bíró szövegkiemelések
6. Hivatkozások és többoldalas webhely
7. Gyakorlati dolgozat I – HTML-alapok
8. Képek és alternatív szövegek
9. Kattintható képek és képes navigáció
10. Számozatlan és számozott listák
11. HTML-táblázatok
12. HTML-validálás és hibakeresés
13. Szemantikus HTML-oldalszerkezet

A 3–8. egységek közlekedés témájú példái a jelenségalapú tanulás hetéhez készültek. A 9. egységtől nem kötelező a közlekedési tematika.

### Mesterséges intelligencia

Tizenegy digitális tananyagegység és külön, tizennyolc órát tartalmazó tanmenet áll rendelkezésre. A témák között szerepel a promptolás, a tanuló modellek, a forráskritika, az MI története és etikája, a környezetvédelem, a kreatív MI, az adatelemzés és a projektmunka.

## 5. A HTML-tananyag fejlesztési célja

A HTML-szakasz egyszerre készítsen fel:

- a tanmenetben meghatározott iskolai követelményekre;
- az ágazati alapvizsgán elvárt gyakorlati weboldalkészítésre;
- az ICDL Webszerkesztés modul szemléletéhez kapcsolódó alapfeladatokra;
- a későbbi CSS- és Bootstrap-tanulásra.

A Udemy-kurzus és Jonas Schmedtmann anyaga forrásként és ötlettárként használható, de egyik kurzust sem kell változtatás nélkül követni. A videók leiratából önálló, magyar nyelvű, kilencedikeseknek megfelelő tananyagot kell készíteni. A pontatlan, elavult vagy rosszul fordított magyarázatokat javítani kell.

## 6. Kötelező módszertani és technikai elvek

- Elsődleges szerkesztő: Visual Studio Code.
- HTML5-szerkezetet használunk: `<!DOCTYPE html>`, `html`, `head`, `body`, `meta charset`, `meta viewport`, `title`.
- A címsorokat tartalmi hierarchia szerint használjuk, nem pusztán a betűméret miatt.
- Kiemeléshez jelentés szerint `strong` és `em` elemet tanítunk; a `b` és `i` nem ezek egyszerű helyettesítője.
- Térköz létrehozására nem használunk egymás után több `br` elemet.
- Külső hivatkozásoknál teljes `https://` címet használunk.
- A relatív útvonalakat, az almappákat és a `../` jelentését példákkal tanítjuk.
- Képnél mindig értelmezzük az `alt` attribútum szerepét. Díszítő képhez `alt=""` használható.
- Kattintható kép alternatív szövege a hivatkozás célját vagy funkcióját írja le.
- Lehetőség szerint helyi, jogtisztán használható képekkel dolgozunk, nem idegen szerverről történő képbehúzással.
- A `target`, `href`, `src`, `alt`, `width` és `height` attribútum, nem tag.
- Az ágazati alapvizsga szóhasználatát követjük: `ul` számozatlan lista, `ol` számozott lista, `li` listaelem. A rendezetlen/rendezett szinonimákat is megemlítjük.
- A HTML tartalmi szerkezetét és a CSS megjelenési szabályait fokozatosan elkülönítjük.
- A tanulók személyes adatot, saját jelszót vagy érzékeny információt nem tesznek a feladatokba.
- Az MI használata megengedett lehet ötletelésre és ellenőrzésre, de a tanulónak értenie és indokolnia kell a beadott kódot.

## 7. Az órák ajánlott szerkezete

Egy tananyagegység lehet egy vagy több 45 perces óra. Az alapértelmezett szerkezet:

1. rövid problémafelvetés vagy valós példa;
2. új fogalom közös bemutatása;
3. rövid, másolható mintakód;
4. irányított gyakorlás;
5. önálló, fokozatosan nehezedő feladat;
6. gyakori hibák és ellenőrzési lista;
7. menthető vagy bemutatható órai produktum;
8. szükség esetén pluszfeladat a gyorsabban haladóknak.

A magyarázat legyen rövid, világos és kilencedikes szinten érthető. Egy órán ne jelenjen meg indokolatlanul sok új fogalom.

## 8. Értékelési alapelvek

- Elsősorban működő, saját készítésű produktumot értékelünk.
- A pontozás legyen előre ismert és ellenőrizhető.
- Külön értékelhető a fájl- és mappaszerkezet, a szabályos HTML, a tartalmi megfelelés, a működés és az önállóság.
- A formai hiba és a működést akadályozó hiba ne azonos súlyú legyen.
- A tanuló tudja bemutatni, hogy a kód mely része mit csinál.
- A gyakorlófeladat és a számonkérés feladattípusa legyen rokon, de a dolgozat ne legyen puszta másolás.

Az első HTML-alapdolgozat közvetlenül a 6. tananyagegység után következik. A 45 perces, 30 pontos feladat kizárólag a dokumentumszerkezetet, címsorokat, bekezdéseket, szemantikus kiemeléseket, belső és külső hivatkozásokat, valamint a relatív útvonalakat méri. A HTML-blokk teljes lezárásakor, még a CSS előtt külön záródolgozat szükséges. A tanári megoldások nem kerülhetnek a nyilvánosan elérhető tanulói mappába.

## 9. Tanmeneti eltérések és rendezendő döntések

Az alábbi eltéréseket a további fejlesztés során tudatosan kell kezelni:

1. **Brackets helyett VS Code:** a tanmenet szövegében még szerepel a Brackets, az eszközoszlop és a tényleges tananyag azonban már Visual Studio Code-ot használ. A digitális tananyagban a VS Code maradjon.
2. **App Inventor helyett Thunkable:** a tanmenet App Inventort nevez meg, a meglévő tananyag Thunkable-alapú. El kell dönteni, hogy a tanmenet szövege módosul-e Thunkable-re, vagy külön App Inventor-anyag készül.
3. **LEGO-robot és micro:bit:** a tanmenet LEGO-robotot, motorokat és robotprojektet ír elő, miközben jelenleg csak micro:bit-alapozás van. Ez tartalmi hiány.
4. **HTML-dolgozat helye:** a jelenlegi 10. anyag a listák után kér számon, míg a tanmenet a táblázatok után helyezi el a HTML-összefoglalást és számonkérést. A jelenlegi dolgozat tekinthető HTML-alapdolgozatnak; a táblázatok után szükséges lehet egy rövidebb kiegészítő számonkérés vagy komplex projekt.
5. **Git-parancsok korszerűsítése:** a tanmenetben szereplő `checkout` mellett a `switch` és `restore` parancsokat is érdemes bemutatni, a tanulói szinthez igazítva.
6. **Slack:** csak akkor legyen kötelező, ha az iskola ténylegesen használja. Máskülönben GitHub-alapú együttműködés vagy az intézményi kommunikációs felület válthatja ki.
7. **Elavult CSS-elemek:** a `float` és `clearfix` történeti és kiegészítő ismeretként szerepeljen; az alapvető modern elrendezést később Flexboxra és CSS Gridre érdemes építeni.

## 10. Következő fejlesztési lépések

### Közvetlenül következő HTML-anyagok

1. összetett HTML-gyakorlófeladat az eddig tanult elemekből;
2. teljes HTML-záródolgozat;
3. átvezetés a külső CSS-fájl használatához.

### Későbbi, tanmenet szerinti blokkok

- Git és GitHub alapok;
- CSS-szintaxis, szelektorok, öröklődés és kaszkád;
- tipográfia, színek, háttér, szegélyek;
- dobozmodell és `box-sizing`;
- modern elrendezés, különösen Flexbox és CSS Grid;
- reszponzív webdizájn, relatív mértékegységek és media query;
- Bootstrap konténerek, grid, komponensek és űrlapok;
- záró, komplex webhelyprojekt;
- rövid JavaScript-bevezetés.

## 11. Közzététel és fájlkezelés

- A fejlesztői/tanári mappa és a tanulóknak közzétett változat külön kezelendő.
- Tanári megoldókulcs, pontozólap és kész megoldás ne kerüljön a nyilvános webhelyre.
- A Móricz Cloudra csak ellenőrzött, tanulóknak szánt fájlok kerüljenek.
- Minden tananyagegység saját, egyértelműen elnevezett mappát kapjon.
- A mappanevekben lehetőleg ne legyen szóköz, ékezet vagy zavaró speciális karakter.
- A belső hivatkozásokat feltöltés előtt helyben ellenőrizni kell.
- A teljes tanári forrásról és a feltöltendő csomagról külön biztonsági másolat készüljön.

## 12. Fejlesztési napló

### 2026. október 30.

- A teljes 9. évfolyamos mappa és a 2026/2027-es tanmenet áttekintve.
- A HTML-tananyag 1–10. egysége elkészült.
- A 3–8. HTML-egység közlekedés témára lett igazítva.
- Elkészült az 1–6. egység után megírható első HTML-alapdolgozat és a kezdőfájl-csomag.
- Következő tervezett HTML-téma: táblázatok.
- A Brackets/VS Code, App Inventor/Thunkable, LEGO/micro:bit és a HTML-dolgozat helyének eltérése rögzítve.
- Elkészült a 11. HTML-táblázatok egység kezdőfájlokkal és ICDL-mini feladattal.
- A képeket és listákat tartalmazó korábbi dolgozat helyett a 7. egységbe kizárólag az 1–6. tananyag ismereteit mérő dolgozat került; a képek, kattintható képek és listák sorszáma 8–10-re változott.
- Elkészült a 12. HTML-validálás és hibakeresés egység hibás kezdőprojekttel, hibanaplóval, W3C HTML Checker- és Chrome DevTools-gyakorlattal.
- Elkészült a 13. Szemantikus HTML-oldalszerkezet egység a `figure`, `figcaption`, `div` és `span` elemekkel együtt.

---

**Frissítési szabály:** új tananyagegység, számonkérés, technológiai döntés vagy tanmeneti változtatás után a „jelenlegi szerkezet”, a „következő fejlesztési lépések” és a „fejlesztési napló” részt frissíteni kell.
