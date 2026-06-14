menu={"pizza":360,
      "popcorn":250,
      "burger":220,
      "roll":100,
      "noodles":340,}

print("-------MENU-------")
for key, value in menu.items():
    print(f"{key:10}:${value:.2f}")
print("------------------")

cart=[]
total=0

while True:
    food=input("Enter your food (press q to exit):").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("The Food you ordered:")
for x in cart:
    print(x)
for x in cart:
    total=total+menu.get(x)
print(f"Your Total amount is:{total}")
