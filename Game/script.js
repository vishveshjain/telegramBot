function play(userChoice) {
    const choices = ['rock', 'paper', 'scissors'];
    const computerChoice = choices[Math.floor(Math.random() * 3)];

    const resultText = document.getElementById("result");
    resultText.innerHTML = `You chose: ${userChoice}<br>Computer chose: ${computerChoice}`;

    if (userChoice === computerChoice) {
        resultText.innerHTML += "<br>It's a tie!";
    } else if (
        (userChoice === "rock" && computerChoice === "scissors") ||
        (userChoice === "paper" && computerChoice === "rock") ||
        (userChoice === "scissors" && computerChoice === "paper")
    ) {
        resultText.innerHTML += "<br>You win!";
    } else {
        resultText.innerHTML += "<br>Computer wins!";
    }
}
