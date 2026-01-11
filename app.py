intro = input("Please choose (add, subtract, multiply, divide): ")
first_number = float(input("Please enter your number: "))
second_number = float(input("Please enter your second number: "))

if intro == "add":
    result = first_number + second_number
    print(f"{first_number} + {second_number} = {result}")
elif intro == "subtract":
    result = first_number - second_number
    print(f"{first_number} - {second_number} = {result}")
elif intro == "multiply":
    result = first_number * second_number
    print(f"{first_number} * {second_number} = {result}")
elif intro == "divide":
    if second_number == 0:
        print("Error cannot divide by zero")
    else:
     result = first_number / second_number
    print(f"{first_number} / {second_number} = {result}")
else:
    print("Error please choose from add, subtract, multiply, divide")


