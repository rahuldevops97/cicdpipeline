number = int(input("Enter a number to generate its multiplication table: "))


print("Multiplication table for", number, ":")
for i in range(1, 11):
    result = number * i
    print(number, "x", i, "=", result)
