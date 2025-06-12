def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


print("This program a factorial number.")
print("A factorial is the number multiplied by the number minus 1, repeating the multiplication and subtraction down to 1.")
print("e.g. factorial(5) = 5 * 4 * 3 * 2 * 1")

number_str = input("Which factorial? ")
number = int(number_str)
print(factorial(number))
