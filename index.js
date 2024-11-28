// creating a basic calorie counter in jacscript
// creat an input to enter foods with each gram of protein carbs and fat and optional waterweight of it so it can be calculated 
// after it show what is avalable in  a list format can do dropdown aswell
// make user select or type what he  ate and then calculate the calroies
// allso creat a function so user can select calaorie each day max and min and program upates real time to it if its over or under
// optional user can select min and max of each protein carbs and fatsb but can't exceed the calrie limit 
// also make it so it won't just ask for 100g  since everything is  in 100 grams so i need to divide it by 10 

let calroiesMax = 2000;
let calroiesMin = 1250;
let userCalories = 0;
let calorie = 0;
let userCarsbs = 0;
let userProteins = 0;
let userFats = 0;
let selectedFoods = document.getElementById("somth")
selectedFoods.innerHTML = "" 

const carbs = 4;
const proteins = 4;
const fats = 9;

// let food100g = [
//     "orange|12|0.9|0.2", 
//     "milk|5|3.4|3.3",    
//     "beef|0|26|15",      
//     "eggs|0.6|13|10"     
// ];// strcture is like this : Name|Carbs|Proteins|Fats

// let showitems = document.getElementById(`searchYeah`)

// let foods = food100g.map(food => food.split("|")[1]); // [to do[] make it so i can divide the carbs protiens and fats


// console.log(foods);

// okay i gonna do that i will put a picture and console log the carsb a person can eat in a day

calorie = (userCarsbs + userProteins + userFats)
let calvis = document.getElementById("calVisual")
calvis.innerHTML = `Calories ${calorie} \n Carbs ${userCarsbs}\n Proteins ${userProteins}\n fats ${userFats}`


let egg = document.querySelector("Egg");



function eggmae(){
    selectedFoods.innerHTML = "Egg" ;
    eggadd();

}


let Lunclyy = document.querySelector("Lunclly");
function Luncly(){
    selectedFoods.innerHTML = "luncly"
    Lunclyy1()
}

function eggadd() {
    // Update the user's macros
    userCarsbs += 0.5; // Add carbs for the egg
    userProteins += 6; // Add proteins for the egg
    userFats += 6; // Add fats for the egg

    // Calculate the updated calories dynamically
    userCalories = (userCarsbs * carbs) + (userProteins * proteins) + (userFats * fats);
    // Update the visual representation
    let calvis = document.getElementById("calVisual");
    calvis.innerHTML = `Calories: ${userCalories.toFixed(0)} <br> 
                        Carbs: ${userCarsbs.toFixed(1)}g <br> 
                        Proteins: ${userProteins.toFixed(1)}g <br> 
                        Fats: ${userFats.toFixed(1)}g`;
    // Optionally, log to the console for debugging
    console.log("Egg added. Updated values:");
    console.log(`Calories: ${userCalories}, Carbs: ${userCarsbs}, Proteins: ${userProteins}, Fats: ${userFats}`);
}



function Lunclyy1(){
    userCarsbs += 22;
    userProteins += 11;
    userFats += 12;
    userCalories = (userCarsbs * carbs) + (userProteins * proteins) + (userFats * fats);
    let calvis = document.getElementById("calVisual");
    calvis.innerHTML = `Calories: ${userCalories.toFixed(0)} <br> 
                        Carbs: ${userCarsbs.toFixed(1)}g <br> 
                        Proteins: ${userProteins.toFixed(1)}g <br> 
                        Fats: ${userFats.toFixed(1)}g`;
                        console.log("Lunchly added I got my drippy cheese. Updated values:");
                        console.log(`Calories: ${userCalories}, Carbs: ${userCarsbs}, Proteins: ${userProteins}, Fats: ${userFats}`);

}

























































// let numbs = [1,2,3,4,5,6,7,8,9];
// let evenumbs = numbs.filter(Iseven);
// let oddnumbs = numbs.filter(isodd);
// console.log(`${evenumbs}`);
// console.log(`${oddnumbs}`);

// function Iseven(element){
//     return  element % 2 === 0;
// }



// function isodd(element){
//     return element % 2 === 1;

// }