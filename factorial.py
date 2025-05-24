def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


number_str = input("Which factorial? ")
number = int(number_str)
print(factorial(number))
