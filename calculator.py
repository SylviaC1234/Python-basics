#Write a simple calculator program
#When the program runs, it prompts the user to enter first no, operator and second no.
#Based on the operator entered ,it should provide the correct output
#operators to be used are (+, -, *, /) If any other operator is used it should display
#the message "provide the correct operator"
import operator

num1 = float(input("Enter first number: "))
operator = input("Enter operator: ")
num2 = float(input("Enter second number: "))


if operator == "+":
    print("The answer is:",num1 + num2)
elif operator == "-":
    print("The answer is:",num1 - num2)
elif operator == "*":
    print("The answer is:",num1 * num2)
elif operator == "/":
    print("The answer is:",num1 / num2)
else:
    print("Provide another operator, this one is not supported")