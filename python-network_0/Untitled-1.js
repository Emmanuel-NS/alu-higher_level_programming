// Prompt the user for input
const input = prompt("Enter any string:");

// Regular expression to check if input contains a number
const containsNumber = /\d/;

// Check if the input matches the regex
if (containsNumber.test(input)) {
    console.log("The input contains a number.");
} else {
    console.log("The input does not contain a number.");
}
