message = input("Tell me a secret? ")

secret = ""
for char in message:
    secret += chr(ord(char) + 1)
print(f"Your secret is safe with me: {secret}")
