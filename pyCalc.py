import time
name = input("Please enter your name: ")
time.sleep(3)
print("Hello %s and welcome to PyCalc v0.1!" % (name))
time.sleep(3)
print("This calculator supports 5 basic operations: ")
time.sleep(2)
print("Addition (+)")
time.sleep(1)
print("Subtraction (-)")
time.sleep(1)
print("Multiplication (*)")
time.sleep(1)
print("Division (/)")
time.sleep(1)
print("Exponentiation (**)")
time.sleep(3)

cont = "y"
while cont.lower() == "y":
    try:
        num1 = float(input("Please enter your first number: "))
    except ValueError:
        print("This is not a number!")
        continue
    try:
        num2 = float(input("Please enter your second number: "))
    except ValueError:
        print("This is not a number!")
        continue
    operation = input("Please select your desired operation (+, -, *, / or **): ")
    if operation == "+":
        print("The result is: %.2f" % (num1 + num2))
    elif operation == "-":
        print("The result is: %.2f" % (num1 - num2))
    elif operation == "*":
        print("The result is: %.2f" % (num1 * num2))
    elif operation == "/":
        print("The result is: %.2f" % (num1 / num2))
    elif operation == "**":
        print("The result is: %.2f" % (num1 ** num2))
    else:
        print("This is not a valid operation")
        continue
    time.sleep(1)
    cont = input("Would you like to restart the calculator? (y/n): ")
    if cont == "n":
        print("==============================================")
        print("Thank you for using PyCalc v0.1! See you soon!")
        print("==============================================")
        time.sleep(1)
        break
