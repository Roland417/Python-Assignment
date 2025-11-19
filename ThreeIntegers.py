
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a>b:
    largest = a
else:
    largest = b

if c > largest:
    largest = c

print("The largest is: ", largest)
