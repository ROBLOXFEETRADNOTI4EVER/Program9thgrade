// document.getElementById(`checkboxItself`).addEventListener('change',function(){
//     if (this.checked) {
//         window.location = "scam.html"
//     }
// })


// document.addEventListener('DOMContentLoaded', function () {
//     // Get the Send Code link
//     const sendCodeLink = document.getElementById('sendCodeLink');

//     // Add a click event listener
//     sendCodeLink.addEventListener('click', function(event) {
//         // Call your function here
//         sendCodeFunction();
//     });
// });

// // Example function to run when Send Code is clicked
// function sendCodeFunction() {
//     console.log('Send Code button clicked');
//     // Add any code you want to run here

   

// }
// const numbers = [1,2,3,4,5];

// const squares = numbers.map(square);

// const cubes = numbers.map(cube);

// console.log(cubes)

// function square(element){
//     return Math.pow(element,2)
// }

// function cube(element){
//     return Math.pow(element,3)
// }


// const students = ["Spongebob","Patric","Squidward","Sandy"]
// const studentsUpper = students.map(upperCase);
// const stundetslower = students.map(lowerCase)


// // console.log(studentsUpper);
// console.log(stundetslower);

// function upperCase(element){
//     return element.toUpperCase();
// }

// function lowerCase(element){
//     return element.toLowerCase();
// }

// const dates = ["2024-1-10", "2025-2-20", "2026-3-30"];

// const formattedDates = dates.map(formatDates);



// console.log(formattedDates);



// function formatDates(element){

//     const parts = element.split("-");

//     return `${parts[1]}/${parts[2]}/${parts[0]}`;

// }


const payments = ["50-2024.04.30-Bob","60-2008.04.05-Julia","6-222.04.6-Alen","734-2023.05.07-Milan"];

const F = payments.map(formatPamynets);

console.log(F.join(""));

function formatPamynets(element){
    const parts = element.split("-");
    return `\nUser:${parts[2]} paid, ${parts[0]} $bucks,${parts[1]}<-- tis time`;

}



const Immigrants = [
    "Migrant1-NH-Terrorist",
    "Migrant2-NH-GoatFucker",
    "Migrant3-NY-Thief",
    "Migrant4-CA-Scammer",
    "Migrant5-TX-Smuggler",
    "Migrant6-FL-Spy",
    "Migrant7-IL-CyberCriminal",
    "Migrant8-PA-Fraudster",
    "Migrant9-OH-HumanTrafficker",
    "Migrant10-MI-DrugDealer",
    "Migrant11-GA-Vandal",
    "Migrant12-NC-Burglar",
    "Migrant13-NJ-Kidnapper",
    "Migrant14-VA-Terrorist",
    "Migrant15-WA-GoatFucker",
    "Migrant16-AZ-Arsonist",
    "Migrant17-MA-Thief",
    "Migrant18-IN-Fraudster",
    "Migrant19-TN-Smuggler",
    "Migrant20-MO-CyberCriminal",
    "Migrant21-MD-DrugDealer",
    "Migrant22-WI-Spy",
    "Migrant23-CO-Burglar",
    "Migrant24-MN-HumanTrafficker",
    "Migrant25-SC-Kidnapper",
    "Migrant26-AL-Fraudster",
    "Migrant27-LA-Arsonist",
    "Migrant28-KY-Smuggler",
    "Migrant29-OR-Thief",
    "Migrant30-OK-Terrorist",
    "Migrant31-CT-Spy",
    "Migrant32-IA-DrugDealer",
    "Migrant33-MS-Burglar",
    "Migrant34-AR-Vandal",
    "Migrant35-NV-Kidnapper",
    "Migrant36-NM-CyberCriminal",
    "Migrant37-UT-HumanTrafficker",
    "Migrant38-WV-Fraudster",
    "Migrant39-HI-Smuggler",
    "Migrant40-ID-Arsonist",
    "Migrant41-ME-Thief",
    "Migrant42-MT-Vandal"
];

// const Muslims = Immigrants.map(GoatFuckers);
// console.log(Muslims.join("|-xx-|"));

// function GoatFuckers(element){
//     const  parts = element.split("-");
//     return `\nPeople :${parts[0]} Wantedfor: ${parts[2]} County${parts[1]}`;
// }


// // under me i will do Name religion Budget and pat 

// const Niggers = ["Bob|Chirstian|50$|Dog","Sam|Atheist|90$|None","smith|Budhism|44$|Parrot","spongabob|Muslim|84$|Sark"];


// const niggermigger = Niggers.map(DeportNigger);
// console.log(niggermigger.join("|here|"))


// function DeportNigger(element){
//     const Niglets = element.split("|");
//     return `Name ${Niglets[0]} Pet ${Niglets[3]} Religion ${Niglets[1]}, Money ${Niglets[2]}`;
    
// }

document.addEventListener('DOMContentLoaded', function () {
    const checkbox = document.getElementById('checkboxItself');

    // Add an event listener for the 'change' event
    checkbox.addEventListener('change', function () {
        if (checkbox.checked) {
            // Redirect to scam.html when the checkbox is checked
            window.location.href = 'scam.html';
        }
    });
});


function Game(){
    let Ongame = true;
    window.alert("Rock ,Paper, Scissors\n Ready ? Set NOW");

    while(Ongame){

        let userinput = window.prompt("Enter Rock,Paper,Scissors");
        userinput = userinput.toLowerCase();
        if (userinput == "rock" || userinput == "paper" || userinput == "scissors") {
            Ongame = false;
            playgame(userinput)

    }
    else{
        window.prompt(`You can't have ${userinput} must choose one  \n Rock, Paper, Scissors`);
        Ongame = true;
    }
    }

    
    
}

Game();


function playgame(userinput){
    window.alert("implaying");
    let Items = ["Rock","Paper","Scissors"];
    Items = Items.map(item => item.toLowerCase());
    let randomm = Math.floor(Math.random() * Items.length);
    let machinechoice = Items[randomm];
    window.alert(machinechoice);
    window.alert(`user input waasssss ${userinput} ANNND machine chooice wasss ${machinechoice}`);
    if (userinput === machinechoice) {
        window.alert("It's a tie!");
    } else if (
        (userinput === "paper" && machinechoice === "rock") ||
        (userinput === "rock" && machinechoice === "scissors") ||
        (userinput === "scissors" && machinechoice === "paper")
    ) {
        window.alert("You won!");
    } else {
        window.alert("You lost!");
    }
}
