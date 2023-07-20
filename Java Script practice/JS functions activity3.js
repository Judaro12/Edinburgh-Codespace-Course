function primeN(num){
    if (num === 1){
        console.log(num + " is either")
    }
    if ( num > 0){
        for (let i = 2 ; i < num ; i++){
            let rem = num % i
            if (rem === 0){
                console.log(num + " is not a Prime Number");
                return;
            }
            else{
                console.log(num + " is a Prime Number");

                return;
            }

        }
    
        
    } else {
        console.log (num + " is a negative Number");
    }
    }
primeN(197);
primeN(-5);
primeN(23);
primeN(66);
primeN(1);