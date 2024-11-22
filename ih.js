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
    return `\nUser:${parts[2]} paid, ${parts[0]} $bucks,${parts[1]}<-- tis time`

}