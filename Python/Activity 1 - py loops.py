# first we use create a variable for the first 2 numbers
number_1 = 0
number_2 = 1

#print the first number
print(number_1)

#loop to print the number
while number_2 <= 50:
    print(number_2)
    # updating the values for the next 2 numebers
    number_1, number_2 = number_2, number_1 + number_2


