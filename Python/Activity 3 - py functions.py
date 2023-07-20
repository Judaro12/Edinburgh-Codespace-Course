#asking user for a integer
pNumber = int(input("please enter a number: "))

#function to check if the number is prime
def is_prime(number):

    if number < 0: #checking if the number is negative
        print ("Negative numbers can not be prime")
        return

    if number <= 1:  #check if the number is 1 or less than 0
        print(number,"is not prime")
        return

    div = 2
    while div * div <= number: # loop to check if its divisible = 0
        if number % div == 0:
            print (number,"is not prime")
            return
        div += 1


    print (number,"is prime")


# calling the function
is_prime(pNumber)