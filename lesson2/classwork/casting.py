num_string = "42"
num_integer = int(num_string)  # Convert string to integer
print(num_integer + 1)

float_string = "3.14"
num_float = float(float_string)  # Convert string to float
print(num_float + 2.19)

int_num = 7
float_num = float(int_num)  # Convert integer to float
print(float_num)

float_num2 = 9.99
int_num2 = int(float_num2)  # Convert float to integer (doesn't round, truncates decimal part)
print(int_num2)

num = 100
num_string2 = str(num)  # Convert integer to string
print(num_string2)