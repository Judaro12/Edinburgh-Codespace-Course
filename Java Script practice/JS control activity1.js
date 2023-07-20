// Ask user to enter three Numbers 
const number1 = Number (window.prompt("Please type First Number",""));
const number2 = Number (window.prompt("Please type Second Number",""));
const number3 = Number (window.prompt("Please type Third Number",""));
// first check if all numbers are Equal = true print result
if (number1 === number2 && number2 === number3) {
    console.log("All Numbers are Equal")
// checking if all numbers are different = true print result 
}else if (number1 !== number2 && number2 !== number3 && number1 !== number3){
    console.log("All Numbers are Different")
// checking the conditiona print result 
  }  else {
        console.log("Neither all are equal or Different")
}

