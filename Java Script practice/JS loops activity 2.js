// ask user to enter first Number
const numberForMultiplication = Number (window.prompt("Please type Number ",""));
// 
for( let i= 1; i <= 10; i++ ){ // body for the loop
    let result = numberForMultiplication *i; // making the multiplication and let =  to result 
    console.log (numberForMultiplication + "x" + i + "=" +result); // printing the result 
}