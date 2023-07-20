#asking user for a integer
number = int(input("please enter a number: "))

# function for factoral of a number
def n_integer(n):
    if n < 0: # check if the number if negative
        print("Factoral is not defined by negative numbers")# printing the result

    elif n == 0: # check if the number is zero
        print ("the Factoral of Zero is: 1")# printing the result

    else:
        factoral_number = 1

        for number  in range(1, n+1): # calculating the factoral number using a loop
            factoral_number *= number

        print (factoral_number) # printing the result

n_integer(number) # calling the function