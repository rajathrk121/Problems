first=int(input("Enter First side of the triangle"))
second=int(input("Enter Second side of the triangle"))
third=int(input("Enter Third side of the triangle"))

if first==second==third:
    print("Equilatoral Triangle")
elif first==second or first==third or second==third:
    print("Isosceles triangle")
else:
    print("Scalene triangle")