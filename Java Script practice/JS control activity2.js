// Ask user to enter three Numbers 
const number1 = Number (window.prompt("Please type First Number",""));
const number2 = Number (window.prompt("Please type Second Number",""));
const number3 = Number (window.prompt("Please type Third Number",""));

// first check if the value is higher = true print result
if (number1 < number2 && number2 < number3) {
    console.log("Increasing Order")
// checking if the value are lower = true print result 
}else if (number1 > number2 && number2 > number3){
    console.log("Decreasing order")
// checking the conditiona print result 
  }  else {
        console.log("Neither increasing nor decreasing order")
  }

