// asking the user for a number
const n= Number (window.prompt("Please type First Number",""));
//
function findFactoral(n) {
    if (n < 0) { // checking if the number is negative
        return "Factorial is not defined for negative numbers.";
    }

    let result = 1;
    for (i = 1; i <= n; i++) {// multiplying the result by each integer 
        result *= i

    }

return result;
}
// printing the result 
console.log (findFactoral(n))

