# input ALWAYS returns a string
user_input = input("Give me an integer: ")

# Error: cannot add an integer to a string
# print(user_input+1)

number = int(user_input)  # casting to an integer

# You can shorten this process:
user_number = int(input("Give me a number: "))
print(user_number + 1)