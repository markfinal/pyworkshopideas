def fibonacci(num):
    if num == 0:
        return 0
    if num < 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


print("This program calculates a sequence of Fibonacci numbers.")
print("A Fibonacci number is the sum of the previous two Fibonacci numbers.")
print("The first two Fibonacci numbers are 1 and 1.")

fibb_str = input("Which Fibonacci number? ")
fibb = int(fibb_str)
if fibb < 0:
    raise ValueError("Cannot ask for negative Fibonacci numbers")
for i in range(1, fibb + 1):
    print(f"{i:2}: {fibonacci(i)}")
