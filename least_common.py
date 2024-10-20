from factor_or_gcf import lcf

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
least_common_factor = lcf(num1,num2)
message = f"The least common factor of {num1} and {num2} is {least_common_factor}"
print(message)