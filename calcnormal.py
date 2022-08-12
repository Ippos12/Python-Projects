import math

print("Hello! Welcome to Krishna's Calculator. Please follow the instructions to use the calculator. If you would like to square root a number, please enter the number you would like to be square rooted as your first. What your second number is does not matter.")
while True:
    number1 = input("Enter your first number\n")

    try: 
        number1 = float(number1)
    except ValueError:
        print("Can you enter an actual number please")
        continue
        break

    operator = input("Enter your operator (+, -, /, *, sqrt, sqre)\n")
    if operator != "sqrt":
        while True:
            number2 = input("Enter your second number\n")
            try:
               number2 = float(number2)
            except ValueError:
                print("Can you enter an actual number please")
                continue
            break
    else:
        print(math.sqrt(float(number1)))

    while True:
        if operator == "+":
            print(float(number1)+ float(number2))
            break
        elif operator == "-":
            print(float(number1) - float(number2))
            break
        elif operator == "/":
            print(float(number1) / float(number2))
            break
        elif operator == "*":
            print(float(number1) * float(number2))
            break
        else:
            break
    replay = input("Press 1 to make another calculation, anything else to quit.\n")
    if replay == "1":
        continue