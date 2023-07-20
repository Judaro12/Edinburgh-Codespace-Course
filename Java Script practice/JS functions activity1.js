const numbers = [10,2,3,3,7];
const testT= [19,20,1,4,8];

function prntontent(numbers) {
    let content = "The content of the array is: ";
  
    for (let i = 0; i < numbers.length; i++) {
      content += numbers[i];
  
      if (i !== numbers.length - 1) {
        content += ", ";
      }
    }
  
    console.log(content);
  }

function maxArray(abc) {
  let max = abc[0];
 
    for ( let i = 0; i < abc.length; i++) {
// checking if the current value is bigger than the max 
    if (abc[i] > max){
        max = abc[i];
    }
}
    return max;
   
}
prntontent(numbers);
console.log("The Max value in the array is:"+ maxArray(number));
console.log(maxArray(testT));

