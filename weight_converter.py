import math
kilo= float(input("Enter the weight in KGS:"))
unit= input("Enter the desired Unit:")
Pound= kilo* 2.20462
gram= round(kilo*1000)

if unit=="pound":
    print(f"The weight in pounds is:{Pound}")
elif unit=="gram":    
    print(f"The weight in grams is:{gram}")
else:
    print("Unit is not valid")