from factor_or_gcf import factors

number = int(input("Enter a number: "))
factors_of_number = factors(number)
message = f"The factors of {number} are {factors_of_number[1:]}"
print(message)