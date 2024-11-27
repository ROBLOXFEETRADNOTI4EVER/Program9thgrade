// let h1lyrics = document.getElementById("Lyrics");
// let inputGuess = document.getElementById("inputGuess");
// let message = document.getElementById("message");

// let lyrics = [
//     "Kisses in the alley, where the sun don't shine|her shadow fades just like mine.",
//     "She wore regret like a second skin|but never let the sorrow in.",
//     "A Polaroid smile fades with time|just like your hand slipping out of mine.",
//     "I heard your laugh in an old tape hiss|like a memory I can't dismiss.",
//     "You left your name in the condensation|a fleeting ghost of conversation.",
//     "Echoes of goodbye haunt the payphone line|but I’m still waiting for a sign.",
//     "The party ended, but you're still dancing|lost in a song that's always chancing.",
//     "Love letters torn, scattered in the breeze|like secrets whispered to the trees."
// ];

// // to soterr ending of the lyrics
// let endings = lyrics.map(lyric => lyric.split("|")[1]);

// function selectlyrics() {
//     let randomIndex = Math.floor(Math.random() * lyrics.length);
//     let randomLyric = lyrics[randomIndex].split("|")[0]; // First part of disaplpy
//     currentEnding = lyrics[randomIndex].split("|")[1]; // end part of siplay
//     return randomLyric;
// }



// let currentEnding = "";

// let randomLyric = selectlyrics();

// h1lyrics.innerHTML = randomLyric;




// function submitGuess(event) {
//     event.preventDefault(); // prevent from resubmit and laoding
//     // users input
//     let userGuess = inputGuess.value.trim();

//     // compare useres shit wiht the lyrics end
//     if (userGuess === currentEnding.trim()) {
//         message.innerHTML = "Correct! Next lyric coming up...";
//         // after correc thos the lrycs
//         randomLyric = selectlyrics();
//         h1lyrics.innerHTML = randomLyric;
//         inputGuess.value = ""; // cls the input field
//     } else {
//         message.innerHTML = "Incorrect, try again!";
//     }
// }



// let numbers = [1,2,3,4,5,6,7,8,9];
// let evennumbs = numbers.filter(Iseven);

// function Iseven(element){
//     return element % 2  === 0;
// }

// console.log(evennumbs);

// let oddnumbs = numbers.filter(IsOdd);
// console.log(oddnumbs);

// function IsOdd(element){
//     return element % 2 === 1;
// }

// const ages = [16,17,18,18,19,20,60];
// let adults = ages.filter(isAdult);
// let under18 = ages.filter(Isudner18);

// console.log(` adults are ->${adults} & and under18 kids are ${under18}`);

// function isAdult(element){
//     return element >= 18;
// }

// function Isudner18(element){
//     return element < 18;
// }


const words = ["apple","Banana","Carrot","milk","children","bobasticsideeye"];
let under7 = words.filter(getShortwords);
console.log(under7);
let morethen7 = words.filter(getlongwords);
console.log(morethen7);

function getShortwords(element){
    return element.length < 7;
}
function getlongwords(element){
    return element.length > 7;
}