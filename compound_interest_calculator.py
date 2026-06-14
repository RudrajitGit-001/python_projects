principal=float(input("Enter the principal balance:"))

while principal<0:
    if principal<0:
        print("Principal amount cannot be zero!")
    principal=float(input("Enter the principal balance:"))

interest=float(input("Enter the interest rate:"))
while interest<0:
    if interest<0:
        print("Interest cannot be zero!")
        interest=float(input("Enter the interest rate:"))

time=int(input("Enter the time period:"))
while time<0:
    if time<0:
        print("Time period cannot be less than or equal zero!")
    time=int(input("Enter the time period:"))

print(f"The princial amount is {principal}")
print(f"The interest amount is {interest}")
print(f"The time period is {time}")

final_amount=float(principal*pow((1+(interest/100)),time))
print(f"The final amount is {final_amount:.2f}")