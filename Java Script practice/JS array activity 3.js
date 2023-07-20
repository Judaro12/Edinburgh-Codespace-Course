const numbers = [25,14,56,15,36,56,77,18,29,49];
let max = numbers[0]
let min = numbers[0]
for ( let i = 0; i < numbers.length; i++){
// checking if the current value is bigger than the max 
    if (numbers[i] > max){
        max = numbers[i]
    }
 // checking if the current value in min than the min
    if (numbers[i] < min){
        min = numbers[i]}
}
console.log ("Origina array:" + numbers) // print just the array Numbers 
// print the max and min value for the array 
console.log ("Maximun value for the above array:" + max)
console.log ("Min value for the above array" + min)
