def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


user_input = input("Enter a number: ")

# Try to convert the input to an integer
try:
    number = int(user_input)
    result = check_even_odd(number)
    print(f"{number} is {result}.")
except ValueError:
    print("Not a number")
