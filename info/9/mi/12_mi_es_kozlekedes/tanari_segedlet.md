# Tanári segédlet – MI a közlekedésben
## Szövegértéstől az utazástervezésig

**9. évfolyam · közlekedési témahét · 45 perc**

Az óra sorrendje: **diasor és tokenizálás; közlekedési jelentés feldolgozása a Geminivel; menetrendek vizsgálata; ugyanaz az utazási feladat a Google Térképen.**

A segédlet tanári használatra készült. Tanári bemutatóval és közös kérdezéssel végigvezethető, külön diákfiók vagy munkalap nem szükséges.

## Az óra célja

A diákok megismerik a szöveg tokenekre bontásának alapgondolatát, kipróbálják a nyelvi modell információkinyerését, majd összehasonlítják a chatbotot egy célzott utazástervezővel. A fő kérdés: **melyik eszköz milyen feladatra használható, és miből tudjuk, hogy helyes a válasz?**

A közlekedési szöveg és a menetrend is szöveges bemenet lehet, de másféle feldolgozást igényel. A tokenizálás önmagában nem magyarázza meg, miért sikerül vagy hibás egy konkrét válasz.

## Előkészítés

Óra előtt nyisd meg:

- A meglévő „MI a szövegelemzésben” diasort.
- Az Esti Hírlap 2026. október 29-i közlekedési körképét: https://estihirlap.hu/kozlekedesi-korkep-2026-oktober-29-orszagos-budapest/
- A Geminit: https://gemini.google.com/
- A feltöltendő kisújszállási menetrendeket.
- A Google Térképet: https://www.google.com/maps
- Ellenőrzéshez a MÁVPluszt: https://mavplusz.hu/

Másold ki előre a cikk törzsszövegét, a címtől a forrásfelsorolásig. A menüket, reklámokat és ajánlott cikkeket hagyd ki. A cikk országos és budapesti híreket, továbbá reggeli, nappali és éjszakai változásokat is tartalmaz. Ez hasznos az időbeli szűrés gyakorlásához. Nem kizárólag reggeli pillanatkép.

A cikk egy adott napon megjelent sajtóösszefoglaló. Az órán a benne szereplő állítások feldolgozását vizsgáljátok, nem tekintitek mai, élő utazási tájékoztatásnak.

A menetrendekből keress ki előre egy ellenőrzött választ ugyanarra az utazási kérdésre, amelyet a Gemininek felteszel. A dátum, a közlekedési nap, az irány és a pontos megálló egyezzen. Készíts képernyőképet vagy jelöld meg a forrás sorát. A Google Térképen is próbáld ki a keresést, és ments képernyőképet tartaléknak.

## 0–10. perc – Diasor: természetes nyelvfeldolgozás és tokenizálás

### Menet

1. A diasor hiányos mondatos feladatával indíts. Kérj több lehetséges folytatást.
2. Röviden mondd el, hogy a természetes nyelvfeldolgozás szövegekkel és beszéddel kapcsolatos feladatokkal foglalkozik.
3. Mutasd meg a tokenizálásról szóló diákat.
4. A sok szövegből tanulást és a lehetséges tévedést foglald össze, a hosszabb beszélgetést hagyd a gyakorlati példákra.

### Ezt mondd a tokenizálásnál

> A modell a szöveget tokeneknek nevezett darabokkal dolgozza fel. Egy token lehet teljes szó, szórész vagy írásjel. A darabolás a használt tokenizálótól függ. A dián látható szavankénti bontás szemléltető példa.

Ne kérd a Geminitől a saját pontos tokenizálásának kiírását, és ne mutasd a kapott szótagolást valódi tokenizálási eredményként.

### Ezt mondd a folytatás előrejelzésénél

> A nyelvi modell a szövegkörnyezet és tanult mintázatok alapján állítja elő a következő tokeneket. A gördülékeny válasz önmagában nem bizonyítja, hogy a benne szereplő adat helyes.

A „nem érti, csak mintázatokat keres” megfogalmazás helyett ezt a működésre és ellenőrizhetőségre összpontosító magyarázatot használd.

### Átvezetés

> Nézzük meg, mit tud kezdeni egy ilyen rendszer egy hosszabb, valódi közlekedési jelentéssel!

## 10–23. perc – Közlekedési körkép feldolgozása a Geminivel

### A forrás átadása

Indíts új beszélgetést. Add át a linket, és ellenőrizd, hogy a Gemini valóban hozzáfért-e a cikkhez. Ha nem, vagy nem egyértelmű, másold be az előkészített törzsszöveget. A puszta link megléte nem bizonyítja, hogy a modell elolvasta az oldalt.

### Kezdő utasítás – másolható

> Az alábbi, 2026. október 29-i közlekedési körképből fogok kérdezni. Kizárólag a megadott szövegre támaszkodj. Minden válaszhoz idézz egy rövid bizonyító szövegrészt, vagy nevezd meg a megfelelő alcímet. Figyelj az időpontokra és az irányokra. Ha nincs elég információ, mondd meg, mi hiányzik. Ne egészítsd ki a jelentést kitalált útvonalakkal vagy időadatokkal.

A szöveg bemásolása után az alábbiakból négy kérdést válassz. Minden kérdés előtt kérj rövid tanulói tippet, utána együtt keressétek meg a forrásban az ellenőrző részletet.

### 1. kérdés – Egy konkrét utas helyzete

> Október 29-én reggel 8-kor az Örs vezér teréről Gödöllőre indulnék. Milyen változásra kell készülnöm a jelentés alapján?

**Ellenőrzési szempont:** a cikk szerint a H8/H9 helyett Örs vezér tere és Cinkota között pótlóbusz jár, a H8 Gödöllő és Cinkota között közlekedik. Pontos indulási időt a cikk nem ad; ilyet ne fogadjatok el belőle levezetett adatként.

### 2. kérdés – Időbeli csapda

> Este 22 órakor a 4–6-ossal utaznék. A jelentés szerint már a teljes vonalon éjszakai pótlóbusz jár? Indokold!

**Ellenőrzési szempont:** a cikkben az éjszakai pótlás kezdete 23:50, tehát a 22 órás időpontra ezt nem szabad alkalmazni. A nappali rendet a cikk külön írja le.

### 3. kérdés – Fontos fogalmi különbség

> Ha a jelentés szerint egy metróállomás nem akadálymentes, abból következik, hogy a metró nem áll meg ott?

**Elvárt gondolat:** nem. Az akadálymentes elérés korlátozása és a metró megállásának elmaradása külön állítás. Kérj példát a cikkből az irányhoz kötött korlátozásra is.

### 4. kérdés – Kérdezzen vissza!

> A jelentés alapján biztosan elérem a vonatomat a Keletiben? Mielőtt válaszolsz, kérdezd meg tőlem a szükséges adatokat!

**Elvárt gondolat:** indulóhely, utazási nap/idő és a vonat indulása nélkül nem dönthető el. A cikk önmagában a pontos eljutás kiszámításához sem ad teljes menetrendet.

### Tartalék kérdések, ha marad idő

- „Válogasd ki a reggel 8-kor Budapesten utazókat érintő információkat! Különítsd el a később kezdődő és a bizonytalan időbeliségű változásokat.”
- „Ugyanebből a szövegből emelj ki két fontos hírt egy autósnak és kettőt egy kerekesszékes utasnak! Indokold a választást!”
- „A megállási tilalom azt jelenti, hogy az adott útszakaszra behajtani is tilos?”

### Rövid következtetés

> Itt a szükséges információt többnyire mondatokból kellett kikeresni, majd a kérdés időpontjára és helyzetére alkalmazni. A válasz akkor használható, ha a forrás alátámasztja.

Ha hibázik, nevezzétek meg a hibát. Ha helyesen válaszol, ezt rögzítsétek eredményként.

## 23–33. perc – Menetrendek: boldogul-e az összetett feladattal?

Indíts külön beszélgetést, hogy a cikk korábbi állításai ne keveredjenek a menetrendekkel. Töltsd fel az előkészített táblázatokat és jelmagyarázatukat. Ez az óra néhány percét igénybe veheti, ezért a fájlok legyenek kéznél.

### A feladat megadása

Használj egy konkrét, előre kiválasztott, a menetrendek érvényességébe eső tanítási napot. Írd ki a dátumot a táblára. A szögletes zárójeleket a kérdés feltevése előtt töltsd ki.

> A feltöltött menetrendek alapján [pontos dátum]-án Kisújszállás, autóbusz-állomás megállóból Túrkeve, autóbusz-állomás megállóba utaznék. Legkorábban 14:20-kor indulhatok. Melyik a következő közvetlen járat? Add meg a vonalszámot, az indulást, az érkezést és a közlekedési nap jelölését. Nevezd meg a dokumentumot, amelyből dolgoztál. Ha valamelyik adat hiányzik vagy nem olvasható biztosan, jelezd.

Ha az általad feltöltött dokumentumokból ez az út nem ellenőrizhető, válassz másik, a fájlokban ténylegesen szereplő útvonalat. Az állomási indulási jegyzék önmagában nem feltétlenül adja meg a célállomási érkezést.

### Közös ellenőrzés

- A megfelelő induló- és célmegállót használta?
- A keresett napon közlekedik a járat? Helyesen olvasta a napjelölést és a lábjegyzetet?
- A járat 14:20-kor vagy később indul?
- Az indulás és az érkezés ugyanahhoz a járathoz tartozik?
- A forrásban valóban szerepel minden kiírt adat?

### Nehezítés, ha az első válasz jó

> Mi változik, ha ugyanezt az utazást a kiválasztott vasárnapon tervezem?

Vagy:

> Ha ezt a járatot lekésem, mikor indul a következő, és mennyivel később érkezem meg?

Az új nap is konkrét dátum legyen, a menetrend érvényességén belül.

### Mit mondj az eredményről?

Hiba esetén:

> A dokumentumban ott lehet minden szükséges adat, de a táblázat helyes olvasása, a napjelölés és az összetartozó időpontok kezelése külön feladat. A feltöltés még nem garantál helyes utazási tervet.

Helyes válasz esetén:

> Ezt a próbát megoldotta. Ebből még nem tudjuk, hogy minden más napot, járatot és csatlakozást is helyesen kezelne.

Ne rendezd meg előre a kudarcot. A cél a teljesítmény vizsgálata, nem annak bizonyítása, hogy a Gemini minden menetrendes feladatra alkalmatlan. Egyetlen hibából az okot sem lehet biztosan azonosítani.

## 33–42. perc – Ugyanaz az utazási kérdés a Google Térképen

### Első rész: célzott útvonalkeresés · kb. 5 perc

1. Add meg ugyanazt a kisújszállási indulómegállót és túrkevei célmegállót.
2. Válaszd a tömegközlekedést.
3. Állítsd be ugyanazt a konkrét dátumot és a 14:20-s indulást.
4. Nyisd le az ajánlat részleteit: megállók, járat, indulás, érkezés, gyaloglás és átszállás.
5. Hasonlítsátok össze a Gemini válaszával és az előre ellenőrzött menetrenddel. Ellenőrzéshez használhatod a MÁVPluszt.

Ha nincs megfelelő találat, ezt jelezd. Használd az előre elmentett példát, és ne minősítsd a találathiányt a járat biztos hiányának.

**Kérdés:**

> Miben segít, hogy ez az eszköz kifejezetten megállók, járatok és csatlakozások kezelésére készült?

**Várható válasz:** célzottan kezeli a közlekedési hálózatot, az időpontokat és az átszállásokat. Az eredménye ugyanakkor az adatok frissességétől és teljességétől is függ.

### Második rész: hol van ebben az MI? · kb. 4 perc

**Ezt mondd:**

> A Google Térkép több rendszer együttese. A menetrendi adatbázis és az útvonalkeresés önmagában nem bizonyít MI-használatot. A Google dokumentáltan gépi tanulást is használ a forgalom és a menetidő előrejelzésében.

Ha belefér, mutass egy autós útvonalat Kisújszállás és Debrecen között, jövőbeli indulási idővel. A kijelzett menetidő vagy időtartomány szemlélteti a becslés fogalmát. Nem szükséges két időpont hosszú összehasonlítása.

**Rövid magyarázat:**

> Sok korábbi út példájából rendelkezésre áll, hogy különböző körülmények között mennyi lett a menetidő. A modell tanításkor a becsléseit összeveti a tényleges eredményekkel. Új körülményekre is tud menetidőt becsülni, korábbi mintázatok és elérhető aktuális adatok alapján. A váratlan események miatt tévedhet.

**Ha megkérdezik, milyen modell:** a Google és a DeepMind nyilvánosan bemutatott gráfneurális hálózatot alkalmazó forgalom-előrejelzést. A gráf az összekapcsolódó útszakaszok hálózatát írhatja le; a kapcsolódó utak forgalma is számít. A név megtanulása nem követelmény.

**Tanári pontosság:** a dokumentált technológia nem a teljes mai rendszer leírása. Nem állíthatjuk, hogy az előbb látott kisújszállási buszajánlatot vagy késési adatot ez a modell állította elő. A megjelenített élő adat érkezhet a szolgáltatótól is.

## 42–45. perc – Lezárás

Kérj három gyors választ:

1. Mi az a token? **Elfogadható:** a szöveg feldolgozásához használt darab; lehet szó, szórész vagy írásjel.
2. Miért nem elég az, hogy a chatbotnak minden dokumentumot feltöltöttünk? **Elfogadható:** helyesen kell kinyernie és összekapcsolnia az adatokat, kezelnie az időbeli feltételeket; ebben hibázhat.
3. Mire használ gépi tanulást a Google Térkép a bemutatott magyarázat szerint? **Elfogadható:** a forgalom és a várható menetidő előrejelzésére.

### Zárómondat

> A jól megfogalmazott válasz még nem bizonyítja a helyességet. A feladathoz megfelelő eszközt választunk, és ellenőrizzük az eredményt.

### Javasolt értékelés: Megfelelt

A tanuló részt vesz a források ellenőrzésében, meg tud nevezni egy tokenizálással kapcsolatos alapfogalmat, és felismeri, hogy a nyelvi modell válaszát, a menetrendi adatot és az előrejelzést külön kell kezelni. A technikai elérési hibákat ne értékeld tanulói teljesítményhibaként.

## Ha csúszik az óra

- A cikkhez négy helyett három kérdést tegyél fel.
- A menetrendnél egy utazási helyzetet ellenőrizzetek, ne kezdjetek több átszállásos tervezésbe.
- A Google Térkép mögötti MI-t magyarázd el szóban; a külön autós bemutató elhagyható.
- A lezárásra mindenképpen maradjon két perc.

## Tartalék technikai terv

- Ha a Gemini nem nyitja meg a linket: másold be a cikk előre kimásolt szövegét.
- Ha a menetrendi feltöltés nem működik: mutasd meg az előre mentett választ és az ellenőrző menetrendi sort. Egyértelműen jelezd, hogy ez korábbi próba.
- Ha nincs internet: a mentett cikkrészletekkel, válaszokkal és térképes képernyőképekkel vezess közös ellenőrzést. Ne állítsd élő demonstrációnak.

## Források

- Feldolgozandó szöveg: Esti Hírlap, Közlekedési körkép – 2026. október 29.: https://estihirlap.hu/kozlekedesi-korkep-2026-oktober-29-orszagos-budapest/
- Google: a gépi tanulás szerepe a forgalom előrejelzésében: https://blog.google/products-and-platforms/products/maps/google-maps-101-how-ai-helps-predict-traffic-and-determine-routes/
- DeepMind: gráfneurális hálózatokkal készített forgalom-előrejelzés: https://deepmind.google/blog/traffic-prediction-with-advanced-graph-neural-networks/
- Google Research: buszkésések becslésének dokumentált példája: https://research.google/blog/predicting-bus-delays-with-machine-learning/
- Google Térkép használati útmutató: https://support.google.com/maps/answer/144339?hl=hu

A technológiai háttérforrások 2019–2020-as ismertetők: dokumentált módszereket mutatnak be, nem minden mai funkció részletes működését. Az órai kérdésekhez a jelentés szövege az ellenőrzés alapja, utazáshoz az aktuális hivatalos tájékoztatás szükséges.
