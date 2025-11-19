total_bill=int(input("Enter total_bill: "))
is_member=input("Enter yes / no: ").lower()

if total_bill >= 1000 and is_member == "yes":
    print("Discounted = 0.10:")

elif total_bill >= 1000 and is_member == "no":
    print("Discounted = 0.5:")

else:
    print("no_discount = 1000")



