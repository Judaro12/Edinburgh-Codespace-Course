# asking the user to input a number and canging it to INT
firstNumber = int(input("Please enter number:"))
secondNumber = int(input("Please enter number:"))
thirdNumber = int(input("Please enter number:"))


if firstNumber == secondNumber and secondNumber == thirdNumber: #check first condition if all are equal
    print("All Numbers are equal")
elif firstNumber != secondNumber and secondNumber != thirdNumber:#cehck second condition if all are diferent
    print("All Numbers are different")
else:
    print("Neithter all are equal or different") # if both are not true printing this



