# Tanári segédlet – MI és Google Térkép
## Honnan tudja a térkép, mikor érek oda?

**Évfolyam:** 9. osztály  
**Időtartam:** 45 perc  
**Kapcsolódás:** közlekedési témahét; hogyan tanul az MI; az adatok szerepe; forráskritika.  
**Óra jellege:** tanári bemutató, irányított beszélgetés, rövid páros vizsgálat. Külön tanulói munkalap és Gemini-fiók nem szükséges.

### Az óra célja

A tanulók értsék meg, hogy a gépi tanulás nem csak szöveges chatbotot jelent. A Google Térkép példáján különítsék el a térképi és menetrendi adatokat, az útvonalkeresést és a menetidő előrejelzését. Tudjanak megnevezni tanulási adatokat, valamint egy okot, amiért az előrejelzés eltérhet a valóságtól.

Ez az óra a korábbi Google Maps-órád folytatása. A nézeteket, a Street View-t, a mentést és a megosztást most csak szükség esetén idézd fel. A hangsúly az indulási idő beállításán és a várható menetidő értelmezésén van. A tokenizálás nem célja ennek az órának.

## Óra előtti előkészítés

- Nyisd meg a Google Térképet: https://www.google.com/maps
- Próbáld ki számítógépen az autós útvonaltervezést Kisújszállás vasútállomás és Debrecen Nagyállomás között. Ellenőrizd a kiválasztott helyeket.
- Válassz egy következő hétköznapot. Próbáld ki az indulási idő átállítását reggel 7:00-ra és este 21:00-ra. A felület elnevezése és az elérhető beállítás eszközönként eltérhet.
- Ments képernyőképet a két keresésről arra az esetre, ha az iskolai hálózaton nem működne a bemutató.
- Próbálj ki egy tömegközlekedési keresést ugyanezekkel az állomásokkal, ugyanarra a kiválasztott napra, 14:00 utáni indulással. Ellenőrzéshez nyisd meg a https://mavplusz.hu/ oldalt.
- Ne építs arra, hogy a két autós időpont feltétlenül eltérő eredményt ad. Ha nincs különbség, az is értelmezhető eredmény.

**Szükséges eszköz:** tanári számítógép, projektor, internet. A páros rész tanulói gépekkel is végezhető, de az egész óra megtartható közös kivetítéssel és szóbeli válaszokkal.

## 0–5. perc – Ráhangolás

**Ezt mondd:**

> A Google Térkép azt írja, hogy 80 perc múlva odaérek Debrecenbe. Honnan tudhatja ezt, ha még el sem indultam?

Gyűjts néhány választ a táblára. Várható ötletek: távolság, sebesség, útvonal, forgalom, korábbi utazások, GPS.

**Következő kérdés:**

> Ha az út hossza ugyanannyi, miért tarthat tovább reggel, mint este?

**Várható válasz:** torlódás, több jármű, lassabb haladás. Ha a diákok időjárást vagy balesetet említenek, fogadd el mint lehetséges befolyásoló tényezőt, de ne állítsd, hogy a bemutatott modell minden ilyen adatot közvetlenül felhasznál.

**Átvezetés:**

> A térképnek a távolságon kívül azt is meg kell becsülnie, milyen gyorsan tudunk majd haladni. Ebben segíthet a korábbi adatokból tanuló MI.

## 5–13. perc – Milyen MI van a Google Térképben?

Írd fel ezt a három kifejezést: **adat – útvonalkeresés – előrejelzés**.

### 1. Adat

**Magyarázat:**

> A térképen szerepelnek utak és megállók. A menetrendben szerepel, hogy egy járatnak mikor kell indulnia. Ezeket az adatokat a rendszer felhasználja.

A tárolt adat önmagában nem MI. A busz 14:35-ös menetrendi indulását nem a nyelvi modell találja ki.

### 2. Útvonalkeresés

**Magyarázat:**

> A rendszer megkeresi, milyen összeköttetéseken juthatunk el a célhoz. Tömegközlekedésnél számít az indulás, az érkezés és az átszállás is.

Az útvonalkereséshez hagyományos kereső és optimalizáló algoritmusok is használhatók. Ne nevezd automatikusan MI-nek az összes útvonalkeresést.

### 3. Előrejelzés gépi tanulással

**Ezt mondd:**

> Sok korábbi utazásból rendelkezésre áll, hogy egy adott útszakaszon, egy adott időpontban mennyi idő alatt haladtak végig a járművek. A modell ezekből összefüggéseket tanul. Új helyzetben a rendelkezésre álló adatok alapján menetidőt becsül.

A Google nyilvános leírása szerint a forgalom előrejelzésében korábbi forgalmi mintázatokat és aktuális forgalmi adatokat is felhasználnak.

**A tanulás bemutatása, egyszerűen:**

1. Bemenet: például útszakasz, napszak és forgalmi jellemzők.
2. Ismert eredmény a tanításkor: a ténylegesen megfigyelt menetidő.
3. A tanítás során a becslés hibája alapján módosítják a modellt.
4. A betanított modell új helyzetre is készít becslést.

**Ha megkérdezik a modell nevét:**

A Google és a DeepMind dokumentált gráfneurális hálózatot alkalmazó forgalom-előrejelzést. A gráf összekapcsolódó elemek hálózata: itt az útszakaszok kapcsolatai is fontosak. Egy torlódás a kapcsolódó utak haladását is befolyásolhatja. A szakkifejezés megtanulását ne kérd számon.

**Pontossági megjegyzés neked:** ezek nyilvánosan bemutatott technológiák, nem a Google Térkép teljes jelenlegi rendszerének leírásai. Nem igazolt, hogy egy konkrét kisújszállási busz késését ez a modell becsüli. Az autós menetidő vizsgálatából a diákok nem tudják elkülönítve megmérni az MI hozzájárulását.

## 13–25. perc – Tanári bemutató: ugyanaz az út, más időpont

### Kivetítendő keresés

- Kiindulás: Kisújszállás, vasútállomás.
- Cél: Debrecen, Nagyállomás.
- Közlekedési mód: autó.

### A bemutató lépései

1. Mutasd meg az azonnali indulásra kapott útvonalat és a menetidőt.
2. Kérj jóslatot: „Mit vártok, mit mutat majd egy hétköznap reggel 7 órás indulásnál?”
3. Állítsd be a kiválasztott hétköznapot és a 7:00-s indulást.
4. Írd fel a kijelzett időt vagy teljes időtartományt, a távolságot és az útvonal főbb útjait.
5. Ugyanarra a napra állíts be 21:00-s indulást, és rögzítsd az eredményt.
6. Ellenőrizd, hogy ugyanazt az útvonalat hasonlítjátok-e össze. Ha változik, ezt külön is beszéljétek meg.

### Kérdések és elvárt gondolatok

**„Mi változott a képernyőn?”**  
A diákok a ténylegesen látott adatokat nevezzék meg. Például: más menetidőtartomány vagy más útvonal.

**„Mi lehet a változás oka?”**  
Lehetséges magyarázat a napszaktól függő forgalom vagy az eltérő útvonal. Ez feltételezés, amíg nincs külön bizonyíték.

**„Miért adhat időtartományt?”**  
A jövőbeli menetidő bizonytalan, a tényleges körülmények eltérhetnek.

**„Biztos, hogy pontosan ennyi idő lesz?”**  
Nem. A becslés eltérhet a tényleges eredménytől, például váratlan torlódás miatt.

**Ha nincs különbség:**

> Ennél az útvonalnál és ezeknél a beállításoknál a kijelzett eredmény azonos. Ebből nem következik, hogy a rendszer nem használ előrejelzést. Most nem látunk különbséget.

**Ha nincs megfelelő időpontválasztó:** használd az előre mentett képernyőképeket. Ne tölts hosszú időt a felület keresésével.

## 25–35. perc – Alkalmazás: utazás megadott feltételekkel

**Ezt a helyzetet add szóban vagy vetítsd ki:**

> A kiválasztott hétköznapon Kisújszállás vasútállomástól Debrecen Nagyállomásig utazunk. Legkorábban 14:00-kor indulhatunk, és 17:00-ra szeretnénk megérkezni. Melyik tömegközlekedési lehetőséget választanátok?

### Ha vannak tanulói gépek

A párok keressenek egy megfelelő utazást. Jegyezzék fel füzetbe:

- az utazás dátumát;
- a járat azonosítóját és a pontos megállókat;
- az indulást és az érkezést;
- az átszállást és a gyaloglást, ha van;
- egy mondatot arról, miért megfelelő a lehetőség.

Ha több ajánlat van, hasonlítsanak össze kettőt. Ha nincs találat, ezt jelezzék, ne találjanak ki utazást.

### Ha csak tanári gép van

Válts tömegközlekedésre, kérd meg a diákokat, hogy diktálják a szükséges beállításokat. Két látható lehetőséget közösen értékeljetek. Ha csak egy van, azt vizsgáljátok.

### Ellenőrzés

A kiválasztott járatot keresd meg a MÁVPluszban ugyanarra a dátumra, azonos megállókkal és iránnyal. Egyezés és eltérés egyaránt megbeszélhető.

**Kérdezd meg:**

> Amit most látunk, az menetrendi idő vagy kifejezetten jelölt élő előrejelzés?

A felületen látható jelölés alapján válaszoljatok. Ha nem egyértelmű, mondjátok ki, hogy nem tudjátok biztosan. Egy késési adat megjelenése önmagában nem bizonyítja, hogy azt a Google saját MI-je számolta.

**Tanári következtetés:** a tömegközlekedési keresés elsősorban a menetrendi adatok gyakorlati felhasználását mutatja. Az MI-ről szóló magyarázatot az előző, forgalmi előrejelzési rész alapozza meg.

## 35–41. perc – Kapcsolat a Gemini-próbával

Idézd fel a korábbi, feltöltött menetrendes próbát. Ha az adott osztály még nem végezte el, rövid gondolatkísérletként mondd el: „Egy chatbotnak átadtuk a menetrendeket, és megkérdeztük, mivel utazzunk.”

**Kérdés:**

> Miért segíthet egy erre a feladatra készült útvonaltervező, ha egy chatbot már megkapta ugyanazokat a táblázatokat?

**Várható szempontok:**

- A menetrendben a járatot, az irányt és a közlekedési napot egyszerre kell helyesen kezelni.
- Az útvonaltervező a megállók és járatok kapcsolatait célzottan kezeli.
- A chatbot tévesen olvashat egy táblázatot vagy rosszul kapcsolhat össze adatokat.
- A célzott utazástervező is függ az adatok frissességétől és teljességétől.

**Ne ezt vond le:** „A Gemini alkalmatlan, a Térkép mindig igazat mond.”

**Ezt mondd:**

> A feladathoz megfelelő eszközt választunk. A nyelvi modell segíthet a kérés megfogalmazásában és a lehetőségek elmagyarázásában. A menetrendi összeköttetéseket célzott útvonaltervezővel keressük, és ellenőrizzük az utazás napját meg az adatokat.

**Rövid összekötés:** a chatbot a következő szövegelemet is előrejelzi, a forgalmi modell menetidőt becsül. Mindkettő használhat tanult mintázatokat, de más a feladata, a bemenete és a kimenete.

## 41–45. perc – Lezárás és értékelés

Kérj három rövid választ szóban vagy füzetbe:

1. Mondj egy példát olyan adatra, amelyből a menetidőt becslő modell tanulhat!
2. Mi a különbség a menetrendi indulás és az előrejelzett érkezés között?
3. Miért térhet el a becslés a tényleges utazási időtől?

### Elfogadható válaszok

1. Korábbi tényleges menetidő, útszakasz, napszak, forgalmi jellemzők.
2. A menetrend tervezett időt rögzít; az előrejelzés a várható teljesülést becsüli.
3. Például váratlan torlódás, útlezárás, megváltozott körülmény vagy hiányos adat.

### Javasolt „Megfelelt” feltétel

A tanuló részt vesz az útvonal vizsgálatában, legalább egy konkrét adattal indokolja a választást, megkülönbözteti a menetrendi adatot az előrejelzéstől, és megnevez egy okot a becslési hibára. A felület technikai hibáját ne értékeld tanulói teljesítményhibaként.

## Tartalék megoldás internetkimaradásra

Elsősorban az előre mentett képernyőképekkel dolgozz. Ha ezek sem állnak rendelkezésre, mutasd be ezt a **kitalált tanítási példát**, amely nem valódi Google- vagy menetrendi adat:

| Korábbi út | Indulás | Forgalmi helyzet | Tényleges menetidő |
|---|---|---|---|
| 1. | Hétköznap 7:00 | Erős forgalom | 90 perc |
| 2. | Hétköznap 7:10 | Erős forgalom | 86 perc |
| 3. | Hétköznap 21:00 | Gyenge forgalom | 68 perc |
| 4. | Hétköznap 21:10 | Gyenge forgalom | 70 perc |

Kérdezd meg: „Mit tippelnétek egy újabb hétköznap reggeli útra? Miért bizonytalan a válasz?”

Nincs egyetlen kötelező számszerű megoldás. A négy példa kevés, és nem tudjuk az összes körülményt. Ez csak a példákból következtetés szemléltetése; a valódi modell sokkal összetettebb, és nem egyszerűen ezt a négy értéket átlagolja.

## Háttérforrások a tanárnak

- Google Maps 101 – forgalmi mintázatok, aktuális adatok és gépi tanulás: https://blog.google/products-and-platforms/products/maps/google-maps-101-how-ai-helps-predict-traffic-and-determine-routes/
- DeepMind – dokumentált gráfneurális hálózat a forgalom előrejelzésében: https://deepmind.google/blog/traffic-prediction-with-advanced-graph-neural-networks/
- Google Research – buszkésések becslésének dokumentált példája: https://research.google/blog/predicting-bus-delays-with-machine-learning/
- Google Térkép útmutató: https://support.google.com/maps/answer/144339?hl=hu

A technológiai források 2019–2020-as nyilvános ismertetők. A leírt módszerek létezését támasztják alá, nem minden mai funkció részletes működését. A felületek és az adott helyen elérhető szolgáltatások változhatnak.
