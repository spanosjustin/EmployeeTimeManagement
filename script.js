// script.js

// declare date variables
let currentDate = newDate();

let hour = currentDate.getHours();
let minute = currentDate.getMinutes();

// declare other variables
let testEmployeeNumber = 111111;

let employeeInput = [];






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
