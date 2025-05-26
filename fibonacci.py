def fibonacci(num):
    if num == 0:
        return 0
    if num < 2:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


fibb_str = input("Which Fibonacci number? ")
fibb = int(fibb_str)
if fibb < 0:
    raise ValueError("Cannot ask for negative Fibonacci numbers")
for i in range(1, fibb + 1):
    print(f"{i:2}: {fibonacci(i)}")
