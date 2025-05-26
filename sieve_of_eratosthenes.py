numbers_used = []
primes_found = []

max_number_str = input("What is the hightest number? ")
max_number = int(max_number_str)

for i in range(2, max_number + 1):
    if i in numbers_used:
        continue

    primes_found.append(i)

    j = 1
    while True:
        multiple = j * i
        if multiple > max_number:
            break
        numbers_used.append(multiple)
        j += 1

print("Found primes:", primes_found)
