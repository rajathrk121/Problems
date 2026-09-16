unit=int(input("Input the units consumed: "))
price=0
if unit<0 :
    print("Enter a valid number")
elif unit <=100:
    price=unit*5
elif unit<=200:
    price=unit*7
else:
    price=unit*10

print(price)
