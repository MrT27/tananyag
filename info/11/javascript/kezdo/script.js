/* let js = "nagyszerű";
// if (js === "nagyszerű") alert("A JavaScript szórakoztató!");

console.log(40 + 8 + 23 - 10);

console.log("Jonas");
console.log(23);


// Változók elnevezése
let firstName = "Matilda"; // camelCase 
console.log(firstName);
console.log(firstName);
console.log(firstName);

let jonas_matilda = "JM";
let $function = 27;

let person = "jonas";
let PI = 3.1415;

let myFirstJob = 'Programozó';
let myCurrentJob = 'Tanár';

console.log(myFirstJob)


let country = 'Portugália';
let continent = 'Európa';
let population = 10;

console.log(country);
console.log(continent);
console.log(population); 
*/

// let javaScriptIsFun = true;
// console.log(javaScriptIsFun)

// console.log(typeof true);
// console.log(typeof javaScriptIsFun);
// console.log(typeof 23);
// console.log(typeof "Lajos");

// javaScriptIsFun = 'IGEN';
// console.log(typeof javaScriptIsFun);

// let year;
// console.log(year);
// console.log(typeof year);

// year = 1987;
// console.log(typeof year);

// console.log(typeof null);

// let age = 30;
// age = 31;

// const birthYear = 1991;
// birthYear = 1990;

// const job;

// var job = "programozó";
// job = "tanár";

// lastName = "Kecsege";
// console.log(lastName);

// const now = 2037;
// const ageJonas = now - 1991;
// const ageSara = now - 2020;
// console.log(ageJonas, ageSara);

// console.log(ageJonas * 2, ageJonas / 10, 2 ** 3)

// const firstName = "Jonas";
// const lastName = "Kecsege";
// console.log(firstName + " " + lastName)

// let x = 10 + 5; // 15
// x += 10; // x = x + 10
// x *= 4; // x = x * 4
// x++; // x = x + 1
// x--; // x = x - 1
// x--; 

// console.log(x)

// // Összehasonlító operátorok

// console.log(ageJonas > ageSara); // >, <, =>, =< 
// console.log(ageSara >= 18); // >, <, =>, =< 

// const isFullAge = ageSara >= 18;

// console.log(now - 1991 > now - 20218) // Honnan tudja, hogy előbb a matematikai műveleteket kell elvégezni?

// const now = 2037;
// const ageJonas = now - 1991;
// const ageSara = now - 2018;

// console.log(now - 1991 > now - 20218);

// console.log(25 - 10 - 5);

// let x, y;
// x = y = 25 - 10 -5;

// console.log(x , y)

// const averageAge = (ageJonas + ageSara) / 2;
// console.log(ageJonas, ageSara, averageAge)


// 1. kihívás

// const massMark = 78;
// const heightMark = 1.69;
// const massJohn = 92;
// const heightJohn = 1.95;


// const bmiJohn = massJohn / (heightJohn ** 2) 
// const bmiMark = massMark / (heightMark ** 2) 

// const markHigherBMI = bmiMark > bmiJohn;

// console.log(bmiMark)
// console.log(bmiJohn)
// console.log(markHigherBMI)

// const firstName = 'Jonas';
// const job = 'tanár';
// const birthYear = 1991;
// const year = 2037;


// const jonas = "A nevem " + firstName + ", " + (year - birthYear) + " éves " + job + "!"

// console.log(jonas)

//  const jonasNew = `${firstName} vagyok, ${year - birthYear} éves ${job}!`

// console.log(jonasNew)

// // Sok fejlesztő már így használja a sztringeke
// // backtick a neve AltGr + 7
// console.log(`Ez csak egy egyszerű sztring...`)

// console.log("Szöveg \n\
// több\n\
// sorban")

// console.log(`Szöveg
// több
// sorban`)

// const age = 15;
// const isOldEnough = age >= 18;

// if (isOldEnough) {
//     console.log(`Sarah elkezdheti a jogosítvány megszerzését 🚗`);
// } else {
//     const yearsLeft = 18 -age;
//     console.log(`Sarah még túl fiatal. Várnia kell még ${yearsLeft} évet. :)`)
// }


// const birthYear = 2012;

// let century;
// if(birthYear <= 2000) {
//     century = 20;
// } else {
//     century = 21;
// }

// console.log(century); // nem elérhető a blokkon kivül

// const massMark = 78;
// const heightMark = 1.69;
// const massJohn = 92;
// const heightJohn = 1.95;

// const BMIMark = massMark / (heightMark * heightMark);
// const BMIJohn = massJohn / (heightJohn * heightJohn);
// console.log(BMIMark, BMIJohn);

// if (BMIJohn > BMIMark) {
//     console.log(`John BMI-je (${BMIJohn}), magasabb Mark BMI-je (${BMIMark})`)
// } else {
//     console.log(`John BMI-je (${BMIJohn}), alacsonyabb Mark BMI-je (${BMIMark})`)
// }


// // típuskonverzió
// const inputYear = "1991";
// console.log(Number(inputYear), inputYear);
// console.log(Number(inputYear) + 18);

// console.log(Number("alma")); // NaN: nem szám 
// console.log(Number(typeof NaN)); 

// console.log(String(23), 23);

// automatikus típuskonverzió

// console.log("Én " + 23 + " éves vagyok");
// console.log("23" - "10" - 3);
// console.log("23" * "2");

// let n = '1' + 1;
// n = n - 1;
// console.log(n);

// 5 falsy érték: 0, "", undefined, null, NaN

// console.log(Boolean(0));
// console.log(Boolean("Alma"));
// console.log(Boolean(undefined));
// console.log(Boolean(null));
// console.log(Boolean(NaN));
// console.log(Boolean({}));


// const money = 10;

// if(money) {
//     console.log(`Ne költsd el az egészet ;)`);
// } else {
//     console.log(`Keress munkát! `);
// }

// let height = 123;
// if (height) {
//     console.log(`Hurrá! A magasság meg van adva`);
// } else {
//     console.log(`A magasság nincs megadva`);
// }

// const age = '18';

// if (age === 18) console.log(`Most lettél nagykorú :D (szigorú összehasonlítás)`);
// if (age == 18) console.log(`Most lettél nagykorú :D (laza összehasonlítás)`);



// Konvertálni kell számmá mert a bekért szám mindig string lesz és a === miatt nem irna ki


// const favorite = Number(prompt("Mi a kedvenc számod?"));

// console.log(favorite);
// console.log(typeof favorite);

// if (favorite === 23) {
//     console.log(`Szuper! A 23 nagyszerű szám"`);
// } else if(favorite === 7) {
//     console.log(`A 7 is jó szám`)
// } else if(favorite === 9) {
//     console.log(`A 9 is jó szám`)
// } else{console.log(`A szám se nem 7, se nem 23, se nem 9`)} 

// if (favorite !== 23) console.log(`Miért nem 23?`);

// const hasDriversLicence = true; // A
// const hasGoodVision = true; // B

// console.log(hasDriversLicence && hasGoodVision);
// console.log(hasDriversLicence || hasGoodVision);
// console.log(!hasDriversLicence);


// const shouldDrive = hasDriversLicence && hasGoodVision;

// if (shouldDrive) {
//     console.log(`Sarah vezethet!`);
// } else {
//     console.log(`Valaki más vezessen…`);
// }

// const isTired = true; // C

// const shouldDrive = hasDriversLicence && hasGoodVision && !isTired;

// if (shouldDrive) {
//     console.log(`Sarah vezethet!`);
// } else {
//     console.log(`Valaki más vezessen…`);
// }

// const scoreDolphins = (96 + 108 + 89) / 3;
// const scoreKoalas = (88 + 91 + 110) / 3;

// console.log(scoreDolphins, scoreKoalas)

// if (scoreDolphins > scoreKoalas) {
//     console.log(`A delfinek nyerik a trófeát 🏆`);
// } else if (scoreKoalas > scoreDolphins) {
//     console.log(`A koalák nyerik a trófeát 🏆`);
// } else {console.log(`Mindkét csapat nyer 🏆`)}


// const day = 'monday';

// switch(day) {
//     case 'monday': // day === 'monday' szigorú összehasonlítást végez
//         console.log(`A kurzus felépítésének megtervezése`);
//         console.log(`Részvétel egy programozói találkozón.`);
//         break;
//     case 'tuesday':
//         console.log(`Az elméleti videók előkészítése`);
//         break;
//     case 'wednesday':
//     case 'thursday':
//         console.log(`Kódpéldák írása`);
//         break;
//     case 'friday':
//         console.log(`Videók felvétele`);
//         break;
//     case 'saturday':
//     case 'sunday':
//         console.log(`Pihenés a hétvégén`);
//         break;
//     default: 
//         console.log(`Érvénytelen nap.`); 
// }


// if (day === 'monday') {
//     console.log(`A kurzus felépítésének megtervezése`);
//     console.log(`Részvétel egy programozói találkozón.`);
// } else if (day === 'tuesday') {
//     console.log(`Az elméleti videók előkészítése`);
// } else if (day === 'wednesday' || day === 'thursday') {
//     console.log(`Kódpéldák írása`);
// } else if (day === 'friday') {
//     console.log(`Videók felvétele`);
// } else if (day === 'saturday' || day === 'sunday') {
//     console.log(`Pihenés a hétvégén`);
// } else {
//     console.log(`Érvénytelen nap.`); 
// }

// 3 + 4 
// 1987
// true && false && !false

// if (23 > 10) {
//     const str = `A 23 nagyobb`;
// }

// const me = `Jonas`
// console.log(`${me} vagyok, ${2037 - 1987} éves`)

// const age = 23;

// age >= 18 ? console.log(`Szeretek bort inni 🍷`) : console.log(`Szeretek vizet inni 💧`);

// const drink = age >= 18 ? 'bor 🍷' : 'víz 💧';

// console.log(`Kedvenc italom: ${drink}`);

// let drink2;

// if ( age>=18 ) {
//     drink2 = 'bor 🍷';
// } else {
//     drink2 = 'víz 💧';
// }

// console.log(`Kedvenc italom: ${drink2}`);

// console.log(`Kedvenc italom: ${age > 18 ? 'bor 🍷' : 'víz 💧'}`)

// const bill = 510;

// console.log(`A számla: ${bill} a borravaló: ${bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2} a végösszeg: ${bill >= 50 && bill <= 300 ? bill + (bill * 0.15) : bill + (bill * 0.2)}`)

// const tip = bill >= 50 && bill <= 300 ? bill * 0.15 : bill * 0.2;
// const total = bill + tip;

// console.log(`A számla: ${bill} a borravaló: ${tip} a végösszeg: ${total}`)
