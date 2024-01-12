// script.js

// declare date variables
let currentDate = newDate();

let hour = currentDate.getHours();
let minute = currentDate.getMinutes();

// declare other variables
let testEmployeeNumber = 111111;

let employeeInput = [];

// Function to add two numbers
function addNumbers(num1, num2) {
    return num1 + num2;
  }

  // Event listener for the first number button
  document.getElementById("number1").addEventListener("click", function() {
    var num1 = prompt("Enter the first number:");
    document.getElementById("number1").textContent = "Number 1: " + num1;
  });

  // Event listener for the second number button
  document.getElementById("number2").addEventListener("click", function() {
    var num2 = prompt("Enter the second number:");
    document.getElementById("number2").textContent = "Number 2: " + num2;
  });

  // Event listener for the calculate button
  document.getElementById("calculate").addEventListener("click", function() {
    var number1 = parseInt(document.getElementById("number1").textContent.split(": ")[1]);
    var number2 = parseInt(document.getElementById("number2").textContent.split(": ")[1]);

    var sum = addNumbers(number1, number2);
    document.getElementById("result").textContent = "Sum: " + sum;
  });


function printHelloWorld() {
    var outputElement = document.getElementById("output");

    outputElement.innerHTML = "Hello World";
}

/*
 *
 *  Working on // Logic Test
 *
 */


function printNumber(number) {
    // Get the output element by its ID
    var outputElement = document.getElementById("output");
    var integerValue = parseInt(number, 10);

    // Push the integer value into the employeeInput array
    employeeInput.push(integerValue);

    // Update the content with all elements of the employeeInput array
    outputElement.textContent = "You clicked numbers: " + employeeInput.join(', ');
}





function collectemployeeID(){
}

function clockIn() {
    if(userInput == testEmployeeNumber) {
    }
}
