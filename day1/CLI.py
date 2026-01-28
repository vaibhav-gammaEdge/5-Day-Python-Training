print("Hey! Welcome to the calculator 😊")
print("You can use +  -  *  /")
print("-" * 30)

def get_number(message):
    while True:
        value = input(message)
        try:
            return float(value)
        except ValueError:
            print("That doesn’t look like a number. Try again.")

def get_operator():
    while True:
        op = input("Which operation do you want (+, -, *, /)? ")
        if op in ["+", "-", "*", "/"]:
            return op
        print("Hmm… that operator isn’t supported.")

num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
op = get_operator()

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 == 0:
        print("Oops! You can’t divide by zero.")
        exit()
    result = num1 / num2

print("-" * 30)
print(f"Your result is: {num1} {op} {num2} = {result}")
print("All done! Have a great day 👋")
