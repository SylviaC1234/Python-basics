firstNumber = int(input("Enter first number:"))
secondNumber = int(input("Enter second number:"))
thirdtNumber = int(input("Enter third number:"))

if firstNumber > secondNumber and firstNumber > thirdtNumber:
    print(firstNumber, "is the largest number")
elif secondNumber > firstNumber and secondNumber > thirdtNumber:
    print(secondNumber, "is the largest number")
else:
    print(thirdtNumber, "is the largest number")
