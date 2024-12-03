let userchoice = "";
let choices = ["rock", "paper", "scissors"];
let basicChoices = {
    1: "rock",
    2: "paper",
    3: "scissors"
};

const random = Math.floor(Math.random() * choices.length);

console.log(random, choices[random]);
bot = random;

console.log(bot);

let displayUserChoice = document.getElementById("userChoice");
let userChoicebyClick = "Select Something";
displayUserChoice.innerHTML = userChoicebyClick;
userChoicebyClick = "3";

function r1() {
    userChoicebyClick = "Rock";
    displayUserChoice.innerHTML = userChoicebyClick;
    userchoice = "0";
    gameOutput();
};

function p1() {
    userChoicebyClick = "Paper";
    displayUserChoice.innerHTML = userChoicebyClick;
    userchoice = "1";
    gameOutput();
};

function s1() {
    userChoicebyClick = "Scissors";
    displayUserChoice.innerHTML = userChoicebyClick;
    userchoice = "2";
    gameOutput();
};

function gameOutput() {
    let botChoice = Math.floor(Math.random() * choices.length);
    let wOL = document.getElementById("wOL");

    if (userchoice === botChoice.toString()) {
        wOL.innerHTML = "It's a tie.";
    } else if (
        (userchoice === "0" && botChoice === 2) ||
        (userchoice === "1" && botChoice === 0) ||
        (userchoice === "2" && botChoice === 1)
    ) {
        wOL.innerHTML = "You win.";
    } else {
        wOL.innerHTML = "You lose.";
    }

    // Clear the result after 4 seconds
    setTimeout(() => {
        wOL.innerHTML = "Play again!";
    }, 7000); // 4000 milliseconds = 4 seconds
};

