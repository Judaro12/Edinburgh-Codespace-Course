# asking the user to input a number and canging it to INT
firstNumber = int(input("Please enter number:"))
secondNumber = int(input("Please enter number:"))
thirdNumber = int(input("Please enter number:"))

if firstNumber > secondNumber > thirdNumber:
    print("Decreasing order")
elif firstNumber < secondNumber < thirdNumber:
    print("Increasing order")
else:
    print("Neither increasing or Decreasing")