


// i can make notes like this in js and C and C++


// console.log('Hello'); // to log something on the console
// console.log("I hate nigger");  // to log something on the console

// // window.alert('I am an alert'); // to creat an alert
// // window.alert('I hate niggers'); // to creat an alert

// // this is a command

// /*
// this is a 
// comment
// */


// document.getElementById('Hello').textContent = 'Hello World';
// document.getElementById('MyPenis').textContent = 'I hate niggers';


// let x = 100;
// console.log(x);
// let y;

// let age = 25;
// let price = 10.99;
// let gpa = 2.1;
// console.log(typeof price);
// console.log(`You are ${age} years old`); // ${} is like f strings in python
// console.log(`the price is $${price}`);
// console.log(`Your gpa is: ${gpa}`);



// let firstName = `Nigger`
// let favFod = 'KFC+Watermelon'
// let email = 'nigger1@gmail.com'; // can't use string from the nigger 1 to do maath

// console.log(`your name is ${firstName}`);
// console.log(`you like child and your favorite food is: ${favFod}`);
// console.log(`Your email is ${email}`)

// let gender = false; console.log(`${gender}`)
// console.log(typeof gender)



// if (gender === false){ // we use 3 to check type and value
//     console.log(`You are a woman`)
// }

// else if (gender === true){
//     console.log(`You are a man`)
// }


// let students = 30;

// students = students + 1; // to add 1 to the current like in python +=
// students = students - 1; // to remove 1 like in python
// students = students * 2; // tis multiplys
//students = students / 2; // this bassicly devides students by 2 
//students = students **2; // this gives the powerr of 2 so négyzet in hungaarian
// let Extrastudents = students % 3; // modulus  operator
// console.log(students);

// students += 1; // FUCKING EASIER THEN DOING THE WHOLE = AND = SHIT btw this gives + = 1 plush eaqucls 1
// students -= 1; // FUCKING EASIER THEN DOING THE WHOLE = AND = SHIT btw this gives - = 1 minus eaqucls 1
// students *= 2;
//students /= 2; // this devides by 2
//students **= 2; // this gives the powerr of 2 so négyzet in hungaarian
// students %= 2; // modulus



// students++; // this increments so it  only adds one its called increment operator
// students--; // this called decrement operaator so it removes 1 from current

// console.log(students);
/*
    Operator precedence
    1 parathethis ()
    2 exponents
    3 multiplication & division & modulo
    4 addition & substration

    in hungarian Müveletek sorendje
*/
// let result = 1 + 2 * 3 + 4 ** 2;
// let result =  12 % 5 + 8 / 2;
// let result = 6 / 2 ** (2 + 5);

// console.log(result);

// let username;
// let password;
// let gender = "";

// // username = window.prompt(`Whats your username?`); Easy way
// // console.log(username);

// document.getElementById(`mySubmit`).onclick = function(){
//     username = document.getElementById(`myText`).value;
//     console.log(username);
//     document.getElementById(`Header1`).textContent = `Hello ${username}`;
// }

// const input = document.querySelectorAll("input")
// const inputValue = input.value;
// console.log(inputValue);

// document.getElementById(`SBFORM`).onclick = function(){
//     const selectedGender = document.querySelector('input:checked').value;
//     console.log(selectedGender);

// }

// let age = window.prompt("how old are you?");
// age = Number(age); // data type we can change it here to a number
// age+=1;
// console.log(age, typeof age); // it will say its a number type since we changed it

// let x ;
// let y ;
// let z ;

// x = Number(x);
// y = String(y);
// z = Boolean(z);
// console.log(x,typeof x, y, typeof y,z, typeof z);



// const PI = 3.14159; // no variabls can be changed so like touple
// let radius;
// let circumference;






// document.getElementById("mySubmit").onclick = function(){
//     radius = document.getElementById("myText").value;
//     radius = Number(radius);
//     circumference = 2 * PI * radius;
//     document.getElementById("myH3").innerHTML = circumference

// }

// const decraseBtn = document.getElementById("decreaseBtn");
// const resetBtn = document.getElementById("resetBtn");
// const increaseBtn = document.getElementById("increaseBtn");
// const countLabel = document.getElementById("countLabel");

// let count = 0;



// increaseBtn.onclick = function(){
//     count++;
//     countLabel.textContent = count;
// }

// decraseBtn.onclick = function(){
//     count--;
//     countLabel.textContent = count;
// }


// resetBtn.onclick = function(){
//     count = 0;
//     countLabel.textContent = count;
// }


const btns = document.getElementsByClassName("btns");
const myText = document.getElementById("myText");

for(let btn of btns){
    btn.onclick = function(){
            if (btn.innerHTML == "Clear"){
                myText.value = "";
            }
            else if (btn.innerHTML == "="){
                myText.value = eval(myText.value)
            }
            // else if (btn.innerHTML == myText.value[myText.value.length -1]){
            //     console.log("s")
            // }
            else{
                myText.value += btn.innerHTML;
            }
        
    }
}



// let x = 3;
// let y = 2;
// let z = 1;

// // z = Math.round(x); // it will always round like normally
// // z = Math.floor(x); // it will walys round down
// // z = Math.ceil(x); // it will awlays round up

// // z = Math.trunc(x);
// // z = Math.pow(x,y)
// // z = Math.sqrt(81); // 9 
// // z = Math.log(x);
// // z = Math.sin(x);
// // z = Math.cos(x);
// // z = Math.tan(x);
// // z = Math.random(x);
// // z = Math.abs(x);
// // console.log(z);
// let max = Math.max(x,y,z)
// console.log(max)

// let min = Math.min(x,y,z)
// console.log(max)

// console.log(z);