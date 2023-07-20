const numbers = [20,30,25,35,-16,60,-100,];// creattion of array values 
let sum = 0;
let nLenght = numbers.length;
// create a loop fot the array
for (let i = 0 ; i < nLenght ; i++){
   sum += numbers[i];   
}

const average = sum / nLenght;


// print the final resolt
console.log( average );

