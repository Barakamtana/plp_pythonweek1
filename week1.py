def Calculate():
    # Prompt for operator
    opperator = input("Enter an operator (+, -, *, /): ")

    num1 = float(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if opperator == "+":
       print(f' the sum of {num1} and {num2} is {sum(num1 + num2)} ')

    elif opperator == "-":
        print(f' the difference of {num1} and {num2} is {num1 - num2} ')

    elif opperator == "*":
        print(f' the product of {num1} and {num2} is {num1 * num2}')

    elif opperator == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return  
        else:
            print(f' the quotient of {num1} and {num2} is {num1 / num2}')


Calculate()