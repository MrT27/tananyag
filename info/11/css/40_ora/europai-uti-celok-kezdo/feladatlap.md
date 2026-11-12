# HTML/CSS gyakorlati számonkérés

## Hat európai úti cél

Készíts reszponzív, európai úti célokat bemutató weboldalt a kapott kezdőcsomagból.

## Kiindulási állapot

A kezdőcsomag tartalmazza:

- a hat úti cél szövegét;
- a képeket és a favicont;
- az `index.html` fájlt;
- a `style.css` fájlt;
- a `queries.css` fájlt.

Alakítsd át a nyers oldalt szemantikus, áttekinthető és reszponzív weboldallá.

## 1. HTML-szerkezet

1. Kapcsold a dokumentumhoz az `img/favicon-96x96.png` fájlt faviconként.
2. A `fejlec` osztályú `div` helyett használj `header` elemet.
3. A `navigacio` osztályú `div` helyett használj `nav` elemet.
4. Az `uti-celok` osztályú `div` helyett használj `main` elemet.
5. Mind a hat `kartya` osztályú `div` elemet alakítsd `article` elemmé.
6. A `lablec` osztályú `div` helyett használj `footer` elemet.

## 2. Alapformázás és dobozmodell

1. Készíts globális alaphelyzetbe állítást:
   - minden elem margója legyen `0`;
   - minden elem belső térköze legyen `0`;
   - a méretezéshez használj `border-box` értéket.
2. A `body` használjon:
   - Arial betűtípust;
   - jól olvasható sormagasságot;
   - sötét szövegszínt;
   - világos háttérszínt.
3. A fejléc, a fő tartalom és a lábléc:
   - legnagyobb szélessége legyen `1200px`;
   - kerüljön vízszintesen középre;
   - kapjon megfelelő belső térközt.
4. Adj megfelelő háttérszínt és szövegszínt a fejlécnek, a kártyáknak és a láblécnek.
5. A képek töltsék ki a kártyák szélességét, de ne torzuljanak és ne lógjanak ki.

## 3. Flexbox és Grid

1. A fejlécben Flexbox segítségével kerüljön a cím balra, a navigáció jobbra.
2. A navigáció hivatkozásai is Flexboxszal jelenjenek meg.
3. A navigáció elemei között használj `gap` térközt.
4. A fő tartalomban a hat kártyát CSS Griddel rendezd el.
5. Nagy képernyőn három egyforma szélességű oszlop legyen.
6. A kártyák között legyen jól látható, egyenletes térköz.

## 4. Reszponzív töréspontok

A médiakérdéseket a `queries.css` fájlban készítsd el.

### Kisebb laptop – `75rem` alatt

- A fejléc, a fő tartalom és a lábléc szélessége legyen rugalmasabb.
- Csökkentsd a belső térközöket.
- Csökkentsd a Grid elemei közötti térközt.

### Tablet – `59rem` alatt

- A fejléc elemei kerüljenek egymás alá.
- A hat kártya két oszlopban jelenjen meg.

### Mobiltelefon – `34rem` alatt

- A kártyák egy oszlopban jelenjenek meg.
- A navigáció hivatkozásai kerüljenek egymás alá.
- Csökkentsd tovább a külső és belső térközöket.

## Pontozás

| Terület              | Elvárás                                                                   |   Pont |
| -------------------- | ------------------------------------------------------------------------- | -----: |
| HTML-alapok          | Favicon; `header`, `nav`, `main`, `article` és `footer` helyes használata |      6 |
| Alapformázás         | Alaphelyzetbe állítás, tipográfia, színek, térközök és rugalmas képek     |      6 |
| Flexbox              | A fejléc és a navigáció elrendezése, igazítása és térközei                |      5 |
| Grid                 | Háromoszlopos alaprács, egyforma oszlopok és megfelelő `gap`              |      8 |
| `75rem`-es töréspont | Rugalmas konténer és csökkentett térközök                                 |      5 |
| `59rem`-es töréspont | Kétoszlopos kártyarendszer és átrendezett fejléc                          |      5 |
| `34rem`-es töréspont | Egyoszlopos kártyák és függőleges navigáció                               |      5 |
| **Összesen**         |                                                                           | **40** |
