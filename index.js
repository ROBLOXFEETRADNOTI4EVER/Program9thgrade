
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

const isSunny = true;

if(!isSunny){
    console.log("it is cloudy");

}
else{
    console.log("it is sunny")
}