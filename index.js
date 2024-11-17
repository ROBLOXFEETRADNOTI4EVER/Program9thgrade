
// let day = 9;

// switch(day){
// 	case 1:
// 		console.log("it is monday");
// 		break;
// 	case 2:
// 		console.log("it is Tuesday");
// 		break;
// 	case 3:
// 		console.log("it is Wednesday");
// 		break;
// 	case 4:
// 		console.log("it is Thursday");
// 		break;
// 	case 5:
// 		console.log("it is Friday");
// 		break;
// 	case 6:
// 		console.log("it is Staturday");
// 		break;
// 	case 7:
// 		console.log("it is Sunday");
// 		break;			
// 	default:
// 		console.log(`${day} <-- is not a day`);				
// }

// let testscore = 32;
// let letterGrade;

// switch(true){
// 	case testscore >= 90:
// 		letterGrade = "A";
// 		break;
// 	case testscore >= 80:
// 		letterGrade = "B";
// 		break;
// 	case testscore >= 70:
// 		letterGrade = "C";
// 		break;
// 	case testscore >= 60:
// 		letterGrade = "D";
// 		break;
// 	default:
// 		letterGrade = "F";

// }
// console.log(letterGrade);





// let username = "dBaoloazsofffo";

// console.log(username.charAt(0));
// console.log(username.indexOf("o")); // it will return index of its currenct postion in rn at position 7

// console.log(username.lastIndexOf("o")); it will log the last one of the selected item in the string 

// console.log(username.length) // it will log out us the lenght of the current string 

// username = username.trim();
// console.log(username)

// username = username.toUpperCase();
// console.log(username);

// username = username.toLocaleLowerCase();
// console.log(username);

// username = username.endsWith(""),("o");
// console.log(username)

// username = username.trim(username.repeat(3));

// console.log(username);

// // username = username.startsWith(" ");
// // console.log(username)
// let result = username.startsWith(" ");

// if(result){
// 	console.log("You are gay");
// }
// else{
// 	console.log("You are not gay");
// }


// let result = username.includes(" ");

// if(result){
// 	console.log("Your username can't incliude ' ' Spaces");

// }
// else{
// 	console.log(`Your username seems fine ${username}`)
// }


// let phonenumber = "123-335-32325";

// // phonenumber = phonenumber.replaceAll("-","");
// // console.log(phonenumber);

// // phonenumber = phonenumber.padStart(30, "0"); // this fills the front of the string with the other string until the character char is 15 characters long 

// // phonenumber = phonenumber.padEnd(30, "0"); // this  fillls the ond of the string with the other string until the character char is 15 characters long 

// console.log(phonenumber)

// const fullName = "Balazs Szabo";

// // let firtname = fullName.slice(0,6);
// // let lastname = fullName.slice(7,12);

// // let firstchar = fullName.slice(0,1);
// // console.log(firstchar);
// // let lastchar = fullName.slice(-1); // negativ index goes from back to front fucking usefull
// // console.log(lastchar);

// let firstName = fullName.slice(0, fullName.indexOf(" "));
// let lastname =  fullName.slice(fullName.indexOf(" ") + 1);
// console.log(firstName);
// console.log(lastname);


// const email = "brocolisex@gmail.com" ;

// let username = email.slice(0,email.indexOf("@"));
// let provider = email.slice(email.indexOf("@") + 1);
// console.log(provider)
// console.log(username);


// let username = window.prompt("Enter your username");

// // username = username.replaceAll(" ","");

// // username = username.trim();
// // let letter = username.charAt(0);
// // letter = letter.toUpperCase();
// // let extraChars = username.slice(1);
// // extraChars = extraChars.toLowerCase();
// // username = letter + extraChars;
// // console.log(username);


// username = username.trim().charAt(0).toUpperCase().replaceAll(" ","") + username.trim().slice(1).toLowerCase().replaceAll(" ","");
// console.log(username)

// const temp = 20;

// if(temp <= 0 || temp > 30){
    
//     console.log("Wheater is bad");
// }
// else{
//     console.log("the weeather is good");
// }

// const isSunny = true;

// if(!isSunny){
//     console.log("it is cloudy");

// }
// else{
//     console.log("it is sunny")
// }

//  = assigment operator 
//  == comparison operator (compare if values are equal)
//  === strict equality oprator ( compare if vaklues & datatype are equal)
//  != ineqality operator
//  !== strict inequality operator  (so a string with the same vlaue as a number can't be true  if the number isn't a string example "3.14" not qual to(!==) 3.14)






// const PI = 3.14;
 
// if(PI !== 3.14){
//     console.log("thats is not Pi");
// }
// else{
//     console.log("that is  pi")
// }

// let username;

// do{
//     username = window.prompt("enter your name");
// }while(username === "" || username === null)

// console.log(`Hello ${username}`);

// let loggedIN = false;
// let username;
// let password;

// while(!loggedIN){
//     username = window.prompt(`Enter your username`);
//     password = window.prompt(`Enter your password`);

//     if(username === "MyUS" && password === "Balazs1"){
//         loggedIN = true;
//         console.log("You are logged in!");szer
    
//     }
//     else{
//         console.log("invalid credentials! please try again");
//     }
// }


// for(let i = 10; i > 0; i-=3){
//     console.log(i)
// }
// console.log("Happy new year")

// for(let i = 1; i <= 22; i++){
//     if(i == 13){
//         continue;
//     }
//     else if(i == 21){
//         break;
//     }
//     else{
//         console.log(i);
//     }

  
// }
// startProgram();

// function startProgram(){
//     let username = "Bro";
//     let age = 21;

// happyBirthday(username,age);

// }


// function happyBirthday(username, age){
//     console.log("I hate niggers i hate them");
//     console.log("I hate niggers i hate them 2");
//     console.log("I hate niggers i hate them 3x as i hated them before","I", username ,age,"Years old");

// }


// const minNum = 1;
// const maxNum = 100;
// const answer = Math.round(Math.random() * (maxNum - minNum + 1 ));

// let attemps = 0;
// let guess;
// let running = true;

// while(running){

//     guess = window.prompt(`Guess a number betwen ${minNum} - ${maxNum}`)
//     guess = Number(guess);
//     if(isNaN(guess)){
//         window.alert("please enter a valid number");
//     }
//     else if(guess < minNum || guess >maxNum){
//         window.alert("Please enter a valid number");
//     }
//     else{
//         attemps++;
//         if(guess < answer){
//             window.alert("Your guess is to low");
//         }
//         else if(guess > answer){
//             window.alert("Your guess was to high");
//         }
//         else{
//             window.alert(`Your guess was right it took you ${attemps} to guess it `);
//             running = false;

//         }
//     }
// }



document.getElementById("submitButton").onclick = function(){

    let temp;

    if(document.getElementById("cButton").checked){
        temp = document.getElementById("textBox").value;
        temp = Number(temp);
        temp = toCelsius(temp);
        document.getElementById("tempLabel").innerHTML = temp + "°C";
    }
    else if(document.getElementById("fButton").checked){
        temp = document.getElementById("textBox").value;
        temp = Number(temp);
        temp = toFahrenheit(temp);
        document.getElementById("tempLabel").innerHTML = temp + "°F";
    }
    else{
        document.getElementById("tempLabel").innerHTML = "Select a unit";
    }
}

function toCelsius(temp){
    return (temp - 32) * (5/9);
}

function toFahrenheit(temp){
    return temp * 9 / 5 + 32;
}

// let name;
// let age;

// function happyBirthday(name, age){
//     console.log(`Happy birthday to ${name}`);
//     console.log(`Happy birthday to ${name}`);
//     console.log(`Happy birthday dear ${name}`);
//     console.log(`Happy birthday to ${name}`);
//     console.log(`You are ${age} years old`);
// }

// happyBirthday("Hitler", 4);


// function add(x, y){
//     let result = x + y;
//     return result;
// }

// let answer = add(2,3);
//     console.log(answer);

// // or use this

// function subtract(x,y){
//     return x - y;
// }

// function multiply(x,y){
//     return x * y;
// }

// function devide(x,y){
//     return x / y;
// }

// // console.log(add(5, 9));
// // console.log(subtract(3, 9));
// // console.log(multiply(3, 10));
// // console.log(devide(634284, 2));

// // checking if a number is even
// function isEven(number){
//     // if(number % 2 === 0){
//     //     return true; 
//     // }
//     // else{
//     //     return false;
//     // }

//     return number % 2 == 0 ? true : false;
// }
// console.log(isEven(2));


// function Email(email){
//     // if(email.includes("@")){
//     //     return true;
//     // }
//     // else{
//     //     return false;
//     // }

//     return  email.includes("@") ? true: false;
// }

// console.log(Email("niggerhate.com"))






let fruits = ["apple", "orange","banana"];


// fruits[3] = "coconut";

// fruits.push("coconut"); // this will push it to the end of the array
// fruits.pop(); // this will remove the last element of the array
// fruits.unshift("hitler"); //So it apends hitler to  index 0
// fruits.shift(); // so this removes hitler the first element

// console.log(fruits[0]);
// console.log(fruits[1]);
// console.log(fruits[2]);
// console.log(fruits[3]);

// fruits.push("pedofil")
// let numOfFruits = fruits.length;

// let index = fruits.indexOf("apple")
// // console.log(numOfFruits);
// console.log(index);


// for(let i = 0; i < fruits.length; i+=2){
//     console.log(fruits[i]);
// }

// for(let i = fruits.length -1 ; i  >= 0; i--){
//     console.log(fruits[i]);
// }

//  for(let fruist of fruits){
//     console.log(fruist);
// }

// fruits.sort(); normal sorting methrod
// fruits.sort().reverse(); // reverse sort

// for(let fuck of fruits){
//     console.log(fuck);
// }


// const matrix = [[1, 2, 3],
//                 [4, 5, 6],
//                 [7, 8 , 9],
//                 ["*",0,"#"]];


// let hitler = matrix[0][0];
// hitler = 'X';
// matrix[0][0] = 'X';
// console.log(hitler);

// for(let row of matrix){
//     const rowString = row.join(' ');
//     console.log(rowString);

// }


// let numbers = [1,2,3,4,5];
// let maximum = Math.max(...numbers); // NIGGA HOW THIS 3 dots unpack unbelivable


// console.log(maximum);

// let username = "Sarek Gergő";
// let letters = [...username];
// console.log(letters.join('-'));

// let fruit = ["Apple", "orange", "Banana"];
// let vegtables = ["carrots","celery","potatoes"];
// let foods = [...fruit, ...vegtables, "eggs", "milk"];

// console.log(foods.join('-'));


function generatePassword(length, includeLowercase, includeUppercase, includeNumbers, includeSymbols){



    const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";

    const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    const numberChars = "0123456789";

    const symbolChars = "!@#$%^&*()_+-=";



    let allowedChars = "";

    let password = "";



    allowedChars += includeLowercase ? lowercaseChars : "";

    allowedChars += includeUppercase ? uppercaseChars : "";

    allowedChars += includeNumbers ? numberChars : "";

    allowedChars += includeSymbols ? symbolChars : "";



    if(length <= 0){

        return `(password length must be at least 1)`;

    }

    if(allowedChars.length === 0){

        return `(At least 1 set of character needs to be selected)`;

    }



    for(let i = 0; i < length; i++){

        const randomIndex = Math.floor(Math.random() * allowedChars.length);

        password += allowedChars[randomIndex];

    }



    return password;

}



const passwordLength = 0;

const includeLowercase = true;

const includeUppercase = true;

const includeNumbers = true;

const includeSymbols = true;



const password = generatePassword(passwordLength, 

                                 includeLowercase, 

                                 includeUppercase, 

                                 includeNumbers, 

                                 includeSymbols);



console.log(`Generated password: ${password}`);