int(input("Enter weight (kg)"))
int(input("Enter height (meters:"))

BMI = "weight / height * height"

if BMI <= 18.5:
    print("Underweight: ")

if BMI > 18.5 >= 24.9:
    print("Normal: ")

if BMI > 25 <= 30:
    print("Overweight: ")

else:
    print("Obese")
