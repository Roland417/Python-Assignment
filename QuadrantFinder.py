first_integer_x = int(input("Enter first integer: "))
second_integer_y = int(input("Enter second integer: ")) 
if first_integer_x > 0 and second_integer_y > 0:
    print("Q1") 

elif first_integer_x < 0 and second_integer_y > 0:
    print("Q2")

elif first_integer_x < 0 and second_integer_y < 0:
    print("Q3")

elif first_integer_x > 0 and second_integer_y < 0:
    print("Q4")

elif first_integer_x == 0 and second_integer_y == 0:
    print("Origin")

elif first_integer_x != 0 and second_integer_y == 0:
    print("X-axis")

elif first_integer_x == 0 and second_integer_y != 0:
    print("Y-axis")
